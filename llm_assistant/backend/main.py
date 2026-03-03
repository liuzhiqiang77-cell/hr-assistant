"""
FastAPI 后端服务
提供 LLM 对话 API
"""

import os
from typing import List, Optional
from contextlib import asynccontextmanager

import os
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env 文件（仅在本地开发环境，Render 使用环境变量）
env_path = Path(__file__).parent / ".env"
if env_path.exists() and not os.getenv("RENDER"):
    load_dotenv(env_path)
    print(f"✅ 已加载 .env 文件: {env_path}")
elif os.getenv("RENDER"):
    print(f"✅ 运行在 Render 环境，使用环境变量")
else:
    print(f"⚠️ 未找到 .env 文件: {env_path}")

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from hr_assistant import assistant, SkillsRAG


# 请求模型
class ChatRequest(BaseModel):
    message: str
    history: Optional[List[tuple]] = []
    stream: bool = True


class ChatResponse(BaseModel):
    response: str
    skills_used: List[dict]


class TodoRequest(BaseModel):
    context: str


class TodoItem(BaseModel):
    task: str
    priority: str
    timeframe: str
    category: str


# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    print("🚀 启动 HR 助手后端...")
    # 预加载 skills
    print(f"✅ 已加载 {len(assistant.rag.skills)} 个 skills")
    yield
    print("👋 关闭服务")


app = FastAPI(
    title="LLM HR 助手 API",
    description="基于 Kimi API 和 High Output Management 的智能 HR 助手",
    version="1.0.0",
    lifespan=lifespan
)

# CORS 配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境应该限制域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件服务 - 前端界面
frontend_path = Path(__file__).parent.parent / "frontend"
if frontend_path.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_path)), name="static")


@app.get("/")
async def root():
    """返回前端界面"""
    chat_html = frontend_path / "chat.html"
    if chat_html.exists():
        return FileResponse(str(chat_html))
    return {
        "message": "LLM HR 助手 API",
        "version": "1.0.0",
        "endpoints": {
            "chat": "POST /chat",
            "chat_stream": "POST /chat/stream",
            "todos": "POST /todos",
            "skills": "GET /skills",
            "health": "GET /health"
        }
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "skills_loaded": len(assistant.rag.skills)
    }


@app.get("/skills")
async def get_skills(category: Optional[str] = None, search: Optional[str] = None, limit: int = 20):
    """获取 Skills 列表"""
    skills = assistant.rag.skills
    
    if category:
        skills = [s for s in skills if s.category == category]
    
    if search:
        skills = assistant.rag.search(search, top_k=limit)
    
    return {
        "total": len(skills),
        "skills": [
            {
                "name": s.name,
                "folder": s.folder,
                "description": s.description[:200],
                "category": s.category
            }
            for s in skills[:limit]
        ]
    }


@app.get("/skills/categories")
async def get_categories():
    """获取所有分类"""
    categories = {}
    for skill in assistant.rag.skills:
        cat = skill.category
        categories[cat] = categories.get(cat, 0) + 1
    return categories


@app.post("/chat")
async def chat(request: ChatRequest):
    """非流式对话"""
    try:
        # 获取相关 skills
        relevant_skills = assistant.rag.search(request.message, top_k=3)
        
        # 调用 LLM
        response_text = ""
        async for chunk in assistant.chat(
            request.message, 
            request.history, 
            stream=False
        ):
            response_text += chunk
        
        return {
            "response": response_text,
            "skills_used": [
                {
                    "name": s.name,
                    "category": s.category,
                    "description": s.description[:100]
                }
                for s in relevant_skills
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest):
    """流式对话"""
    async def generate():
        try:
            async for chunk in assistant.chat(
                request.message, 
                request.history, 
                stream=True
            ):
                yield chunk
        except Exception as e:
            yield f"[ERROR] {str(e)}"
    
    return StreamingResponse(
        generate(),
        media_type="text/plain",
        headers={"X-Accel-Buffering": "no"}
    )


@app.post("/todos")
async def generate_todos(request: TodoRequest):
    """生成 TODO 清单"""
    todos = await assistant.get_todos(request.context)
    return {"todos": todos}


@app.get("/stats")
async def get_stats():
    """获取统计信息"""
    categories = {}
    for skill in assistant.rag.skills:
        cat = skill.category
        categories[cat] = categories.get(cat, 0) + 1
    
    return {
        "total_skills": len(assistant.rag.skills),
        "categories": categories,
        "api_configured": bool(os.getenv("KIMI_API_KEY") or os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY"))
    }


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
