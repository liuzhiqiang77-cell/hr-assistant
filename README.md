# 👥 初级 HR 助手

基于 Andy Grove《High Output Management》的管理学 Skills 知识库，为初级 HR 和团队管理者提供专业指导。

## 📦 包含内容

- **287 个管理 Skills**，涵盖 8 大 HR 模块：
  - 🎯 招聘面试（面试技巧、候选人评估、背景调查）
  - 📊 绩效管理（绩效评估、面谈、问题诊断）
  - 🚀 职业发展（职业规划、晋升管理）
  - 💰 薪酬晋升（薪酬设计、激励策略）
  - 🗣️ 一对一沟通（高效会议、沟通框架）
  - 📚 培训发展（培训设计、经理培训）
  - 👥 员工关系（员工保留、关系管理）
  - 🔄 管理流程（杠杆、时间优化）

## 🚀 快速启动（三选一）

### 🌟 方案 1：LLM 智能对话版（最强 ⭐推荐⭐）

**真正的 AI 对话 + RAG 知识增强**

```bash
cd llm_assistant
export KIMI_API_KEY=your_api_key  # 从 platform.moonshot.cn 获取
./start.sh
```

功能：
- 💬 自然语言对话，理解上下文
- 🧠 Kimi LLM + 287 个 Skills 知识库
- 🎯 智能匹配相关 Skills
- ✅ 自动生成 TODO 清单

访问：`frontend/chat.html`

[📖 查看 LLM 版详细说明](llm_assistant/README.md)

---

### 方案 2：轻量智能问答版（无需 API Key）

**本地关键词匹配 + 模板回答**

```bash
./start.sh
# 访问 http://localhost:8080/smart.html
```

功能：
- 🔍 关键词匹配 Skills
- 📋 模板化回答
- ✅ 预设 TODO 清单
- 🚀 无需网络，即开即用

---

### 方案 3：浏览所有 Skills

```bash
./start.sh
# 访问 http://localhost:8080
```

功能：
- 📚 分类浏览 287 个 Skills
- 🔍 搜索功能
- 📖 查看详细内容

## 📖 使用指南

### 场景 1：准备面试
1. 选择"🎯 招聘面试"模块
2. 查看"面试技巧"相关 Skills
3. 学习如何设计面试问题、评估候选人

### 场景 2：绩效面谈
1. 选择"📊 绩效管理"模块
2. 了解绩效评估框架
3. 学习如何处理"不能"vs"不愿"的情况

### 场景 3：员工发展规划
1. 选择"🚀 职业发展"模块
2. 查看职业规划相关 Skills
3. 帮助员工制定发展计划

## 🔧 与 Kimi CLI 配合使用

这个应用可以与 Kimi CLI 无缝配合：

1. **在应用中查找知识** → 找到需要的 Skill
2. **在 Kimi CLI 中深入** → 获得交互式指导

启动 Kimi CLI：
```bash
kimi
```

然后询问具体的管理问题，Kimi 会自动触发相关的 Skills。

## 📚 知识来源

所有 Skills 均基于 **Andy Grove** 的经典管理学著作：
- 《High Output Management》（中文名：《格鲁夫给经理人的第一课》）

## 📝 项目结构

```
hr-assistant/
├── app/
│   └── main.py          # Streamlit 主应用
├── skills/              # 287 个 HR 管理 Skills
│   ├── candidate-interview-techniques/
│   ├── performance-review-framework/
│   └── ...
├── data/                # 数据文件
├── requirements.txt     # Python 依赖
├── start.py            # 启动脚本
└── README.md           # 本文件
```

## 🎯 适用人群

- 初级 HR 专员
- 新任团队经理
- 需要系统学习管理方法的职场人士
- 想要了解 Grove 管理思想的学习者

---

Made with ❤️ based on High Output Management
