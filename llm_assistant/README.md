# 🤖 LLM HR 助手

基于 **Kimi API** + **High Output Management Skills** 的智能 HR 助手

## ✨ 核心特性

| 特性 | 说明 |
|-----|------|
| 🤖 LLM 驱动 | 基于 Kimi API，自然语言理解 |
| 📚 RAG 增强 | 自动检索相关的 287 个管理 Skills |
| 💬 多轮对话 | 支持上下文理解，追问澄清 |
| ✅ 智能 TODO | 自动生成可执行的行动清单 |
| 🎯 精准匹配 | TF-IDF + 语义匹配 Skills |

## 🏗️ 架构

```
用户提问
    ↓
[Skills RAG] → 检索相关 Skills (Top 3)
    ↓
[Prompt 构造] → System Prompt + Skills Context + User Question
    ↓
[Kimi API] → 生成专业回答
    ↓
[TODO 生成] → 提取行动项
    ↓
用户获得：专业回答 + TODO 清单
```

## 🚀 快速启动

### 方案 1: DeepSeek（推荐 ⭐）

**无需复杂认证，注册即有 5000万 tokens 免费额度！**

```bash
# 1. 获取 DeepSeek API Key: https://platform.deepseek.com/

# 2. 启动
cd llm_assistant
export DEEPSEEK_API_KEY=sk-your_key
./start_deepseek.sh
```

详细步骤：[USE_DEEPSEEK.md](USE_DEEPSEEK.md)

### 方案 2: Kimi

```bash
# 1. 获取 Kimi API Key: https://platform.moonshot.cn/

# 2. 启动
cd llm_assistant
export KIMI_API_KEY=your_key
./start.sh
```

### 方案 3: 其他 OpenAI 兼容 API

支持 OpenRouter、SiliconFlow、Azure 等任何 OpenAI 格式 API。

编辑 `backend/.env`：
```
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
OPENAI_BASE_URL=https://api.openai.com/v1
DEFAULT_MODEL=gpt-3.5-turbo
```

或手动启动：

```bash
# 安装依赖
pip install -r backend/requirements.txt

# 启动后端
cd backend
python main.py

# 在另一个终端打开前端
open frontend/chat.html
```

### 4. 访问应用

- **前端界面**: `frontend/chat.html` (双击打开或拖入浏览器)
- **后端 API**: http://localhost:8000
- **API 文档**: http://localhost:8000/docs

## 💬 使用示例

### 示例 1：面试评估

**用户**: 我要面试一个技术很强但沟通能力一般的候选人，该怎么评估？

**系统**:
1. 匹配 Skills: `interview-questioning-techniques`, `comprehensive-candidate-evaluation`
2. LLM 生成专业回答：结构化面试问题、评估维度、决策建议
3. 生成 TODO:
   - 🔴 设计行为面试问题（重点关注协作场景）
   - 🔴 安排技术演示环节
   - 🟡 进行交叉面试

### 示例 2：绩效面谈

**用户**: 员工绩效突然下降，我该怎么跟他谈？

**系统**:
1. 匹配 Skills: `performance-review-framework`, `performance-diagnosis`
2. LLM 分析可能原因，给出面谈策略
3. 生成 TODO:
   - 🔴 收集近期工作数据
   - 🔴 准备开放式问题清单
   - 🟡 预约一对一会议

## 📡 API 接口

### 对话接口

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "如何进行绩效面谈？",
    "history": [],
    "stream": false
  }'
```

**响应**:
```json
{
  "response": "专业的回答内容...",
  "skills_used": [
    {
      "name": "Performance Review Framework",
      "category": "绩效管理",
      "description": "..."
    }
  ]
}
```

### 流式对话

```bash
curl -X POST http://localhost:8000/chat/stream \
  -H "Content-Type: application/json" \
  -d '{
    "message": "如何进行绩效面谈？",
    "stream": true
  }'
```

### 生成 TODO

```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -d '{
    "context": "用户要进行绩效面谈..."
  }'
```

## 🔧 技术栈

- **后端**: FastAPI + OpenAI SDK
- **LLM**: Kimi (Moonshot AI)
- **检索**: TF-IDF + 倒排索引
- **前端**: Vanilla JS + SSE
- **数据**: 287 个结构化 Skills

## 📁 目录结构

```
llm_assistant/
├── backend/
│   ├── main.py              # FastAPI 服务
│   ├── hr_assistant.py      # LLM + RAG 核心
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   └── chat.html            # 聊天界面
├── start.sh                 # 启动脚本
└── README.md
```

## 🎯 与简单版的区别

| 功能 | 简单版 (smart.html) | LLM 版 (llm_assistant) |
|-----|-------------------|----------------------|
| 核心技术 | 关键词匹配 | Kimi LLM + RAG |
| 回答质量 | 模板化 | 智能生成，个性化 |
| 多轮对话 | ❌ | ✅ |
| 上下文理解 | ❌ | ✅ |
| 追问澄清 | ❌ | ✅ |
| 需要 API Key | ❌ | ✅ |

## 🔒 隐私说明

- 所有数据本地处理，不保存对话历史
- API Key 仅在本地使用，不会上传
- Skills 数据完全离线

## 🐛 故障排除

**问题**: 后端启动失败
```bash
# 检查 API Key
export KIMI_API_KEY=your_key

# 检查端口占用
lsof -i :8000
```

**问题**: 前端无法连接后端
```bash
# 检查后端是否运行
curl http://localhost:8000/health

# 检查 CORS 配置
# 确保后端允许前端域名
```

**问题**: LLM 回答慢
- 这是正常的，LLM 需要思考时间
- 使用流式输出可以看到实时生成过程

---

Powered by Kimi + High Output Management
