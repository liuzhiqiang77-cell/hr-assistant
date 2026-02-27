"""
LLM 驱动的智能 HR 助手后端
基于 Kimi API + High Output Management Skills
"""

import os
import json
import re
from pathlib import Path
from typing import List, Dict, Optional, AsyncGenerator
from dataclasses import dataclass
from collections import Counter
import yaml

from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Skill:
    """Skill 数据类"""
    name: str
    folder: str
    description: str
    body: str
    category: str = ""


class SkillsRAG:
    """Skills 检索增强生成器"""
    
    def __init__(self, skills_path: str = "../../data/skills.json"):
        self.skills_path = Path(skills_path)
        self.skills: List[Skill] = []
        self.inverted_index: Dict[str, List[str]] = {}
        self.load_skills()
        self.build_index()
    
    def load_skills(self):
        """加载 Skills 数据"""
        if not self.skills_path.exists():
            # 尝试其他路径（本地开发环境）
            possible_paths = [
                Path(__file__).parent.parent.parent / "data" / "skills.json",
                Path.cwd() / "data" / "skills.json",
                Path(__file__).parent.parent.parent.parent / "data" / "skills.json",
                Path("/app/data/skills.json"),
                Path("/opt/render/project/src/data/skills.json"),
            ]
            for path in possible_paths:
                if path.exists():
                    self.skills_path = path
                    print(f"✅ 找到 skills 文件: {path}")
                    break
            else:
                print(f"⚠️ 警告: 找不到 skills.json 文件，已尝试路径: {possible_paths}")
                # 创建一个空的 skills 列表避免崩溃
                self.skills = []
                return
        else:
            print(f"✅ 使用默认路径: {self.skills_path}")
        
        with open(self.skills_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for item in data:
            self.skills.append(Skill(
                name=item.get('name', item['folder']),
                folder=item['folder'],
                description=item.get('description', ''),
                body=item.get('body', '')[:3000],  # 限制长度
                category=item.get('category', self._categorize(item['folder']))
            ))
        
        print(f"✅ Loaded {len(self.skills)} skills")
    
    def _categorize(self, folder_name: str) -> str:
        """分类 skill"""
        n = folder_name.lower()
        if any(k in n for k in ['interview', 'candidate', 'hiring']):
            return "招聘面试"
        elif any(k in n for k in ['performance', 'review', 'assessment']):
            return "绩效管理"
        elif any(k in n for k in ['career', 'promotion']):
            return "职业发展"
        elif any(k in n for k in ['compensation', 'salary']):
            return "薪酬晋升"
        elif 'one-on-one' in n:
            return "一对一沟通"
        elif any(k in n for k in ['training', 'teaching']):
            return "培训发展"
        elif any(k in n for k in ['employee', 'retention', 'relationship']):
            return "员工关系"
        else:
            return "管理流程"
    
    def tokenize(self, text: str) -> List[str]:
        """分词"""
        text = text.lower()
        english = re.findall(r'\b[a-z]+\b', text)
        chinese = re.findall(r'[\u4e00-\u9fff]{2,}', text)
        return english + chinese
    
    def build_index(self):
        """构建倒排索引"""
        for skill in self.skills:
            text = f"{skill.name} {skill.description} {skill.body}"
            tokens = set(self.tokenize(text))
            for token in tokens:
                if token not in self.inverted_index:
                    self.inverted_index[token] = []
                self.inverted_index[token].append(skill.folder)
    
    def search(self, query: str, top_k: int = 3) -> List[Skill]:
        """搜索相关 Skills"""
        query_tokens = self.tokenize(query)
        
        # 候选 skills
        candidates = {}
        for token in query_tokens:
            if token in self.inverted_index:
                for folder in self.inverted_index[token]:
                    candidates[folder] = candidates.get(folder, 0) + 1
        
        # 计算相似度
        results = []
        for skill in self.skills:
            score = candidates.get(skill.folder, 0)
            
            # 标题匹配加权
            title_tokens = set(self.tokenize(skill.name))
            title_matches = len(set(query_tokens) & title_tokens)
            score += title_matches * 2
            
            # 关键词加权
            category_keywords = {
                '面试': ['interview', 'candidate'],
                '绩效': ['performance', 'review'],
                '晋升': ['promotion', 'career'],
                '一对一': ['one-on-one'],
                '培训': ['training'],
                '离职': ['retention']
            }
            
            for keyword, terms in category_keywords.items():
                if keyword in query.lower():
                    skill_text = f"{skill.name} {skill.description}".lower()
                    if any(t in skill_text for t in terms):
                        score += 3
            
            if score > 0:
                results.append((skill, score))
        
        results.sort(key=lambda x: x[1], reverse=True)
        return [r[0] for r in results[:top_k]]


class LLMHRAssistant:
    """LLM 驱动的 HR 助手 - 支持多种 LLM 提供商"""
    
    def __init__(self):
        self.rag = SkillsRAG()
        
        # 检测 LLM 提供商
        provider = os.getenv("LLM_PROVIDER", "kimi").lower()
        
        if provider == "deepseek":
            # DeepSeek 配置
            api_key = os.getenv("DEEPSEEK_API_KEY")
            base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com/v1")
            default_model = "deepseek-chat"
            provider_name = "DeepSeek"
        elif provider == "openai":
            # OpenAI 配置
            api_key = os.getenv("OPENAI_API_KEY")
            base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
            default_model = "gpt-3.5-turbo"
            provider_name = "OpenAI"
        else:
            # Kimi 默认配置
            api_key = os.getenv("KIMI_API_KEY")
            base_url = os.getenv("KIMI_BASE_URL", "https://api.moonshot.cn/v1")
            default_model = "moonshot-v1-8k"
            provider_name = "Kimi"
        
        # 如果环境变量没有，尝试从 .env 文件加载
        if not api_key:
            env_path = Path(__file__).parent / ".env"
            if env_path.exists():
                with open(env_path) as f:
                    for line in f:
                        if provider == "deepseek" and line.startswith("DEEPSEEK_API_KEY="):
                            api_key = line.strip().split("=", 1)[1]
                        elif provider == "kimi" and line.startswith("KIMI_API_KEY="):
                            api_key = line.strip().split("=", 1)[1]
        
        if not api_key:
            print(f"⚠️ 警告: {provider_name} API Key 未设置，LLM 功能将不可用")
        else:
            print(f"✅ 使用 {provider_name} API")
        
        self.client = AsyncOpenAI(
            api_key=api_key,
            base_url=base_url
        )
        self.model = os.getenv("DEFAULT_MODEL", default_model)
        
        # System prompt 模板
        self.system_template = """你是「初级 HR 助手」，一位专业的 HR 和管理学顾问。

你的知识基于 Andy Grove 的经典著作《High Output Management》（高产出管理）。

## 你的职责
1. 理解用户的管理问题，提供专业、实用的建议
2. 基于提供的 Skills 知识，给出具体的操作指导
3. 生成清晰的 TODO 清单，帮助用户落地执行

## 回答风格
- 专业但易懂，避免过于学术化的表达
- 结构化输出，使用清晰的标题和列表
- 给出具体可执行的建议，而非空泛的理论
- 必要时追问细节，以提供更精准的建议

## 当前可参考的管理 Skills
{skills_context}

请基于以上知识，回答用户的问题。如果用户问题不够具体，请主动询问更多细节。"""
    
    def _format_skills_context(self, skills: List[Skill]) -> str:
        """格式化 Skills 上下文"""
        context_parts = []
        for i, skill in enumerate(skills, 1):
            context_parts.append(f"""
### Skill {i}: {skill.name}
**分类**: {skill.category}
**描述**: {skill.description}

**核心内容**:
{skill.body[:800]}
---""")
        return "\n".join(context_parts)
    
    async def chat(
        self, 
        user_message: str, 
        conversation_history: List[Dict] = None,
        stream: bool = True
    ) -> AsyncGenerator[str, None]:
        """
        对话主函数
        
        Args:
            user_message: 用户消息
            conversation_history: 对话历史 [("user", msg), ("assistant", msg), ...]
            stream: 是否流式输出
            
        Yields:
            生成的文本片段
        """
        # 1. 检索相关 Skills
        relevant_skills = self.rag.search(user_message, top_k=3)
        
        # 2. 构建 system prompt
        skills_context = self._format_skills_context(relevant_skills)
        system_prompt = self.system_template.format(skills_context=skills_context)
        
        # 3. 构建消息列表
        messages = [{"role": "system", "content": system_prompt}]
        
        if conversation_history:
            for role, content in conversation_history:
                messages.append({"role": role, "content": content})
        
        messages.append({"role": "user", "content": user_message})
        
        # 4. 调用 LLM
        try:
            if stream:
                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    stream=True,
                    temperature=0.7,
                    max_tokens=2000
                )
                
                async for chunk in response:
                    if chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content
            else:
                response = await self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    stream=False,
                    temperature=0.7,
                    max_tokens=2000
                )
                yield response.choices[0].message.content
                
        except Exception as e:
            yield f"抱歉，调用 LLM 时出错：{str(e)}\n\n请检查 KIMI_API_KEY 是否配置正确。"
    
    async def get_todos(self, context: str) -> List[Dict]:
        """
        基于对话内容生成 TODO 清单
        
        Args:
            context: 对话上下文
            
        Returns:
            TODO 列表
        """
        prompt = f"""基于以下对话内容，为用户生成一个具体的 TODO 行动清单。

对话内容：
{context}

请输出 JSON 格式的 TODO 清单：
[
  {{
    "task": "具体任务描述",
    "priority": "high/medium/low",
    "timeframe": "建议完成时间",
    "category": "准备/执行/跟进"
  }}
]

要求：
1. 任务要具体可执行
2. 高优先级的任务不要超过 3 个
3. 时间要合理
4. 输出纯 JSON，不要有其他文字"""

        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=1000
            )
            
            content = response.choices[0].message.content
            # 提取 JSON
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return []
        except:
            return []


# 全局实例
assistant = LLMHRAssistant()
