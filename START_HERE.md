# 🚀 开始使用初级 HR 助手

## 📍 你在这里

```
hr-assistant/
├── START_HERE.md          ← 你现在在这里
├── README.md              ← 详细说明
├── FEATURES.md            ← 版本对比
├── QUICKSTART.md          ← 快速开始
│
├── 🤖 LLM 智能版（最强）
│   └── llm_assistant/
│       ├── start.sh
│       ├── backend/       ← FastAPI + Kimi API
│       └── frontend/      ← 聊天界面
│
├── 🔧 轻量问答版（无需 API）
│   ├── smart.html         ← 智能问答
│   └── ask.py             ← 命令行工具
│
├── 📚 浏览版
│   └── index.html         ← 浏览所有 Skills
│
└── 📦 data/
    └── skills.json        ← 287 个管理 Skills
```

---

## ⚡ 30 秒快速开始

### 有 Kimi API Key？用 LLM 智能版！

```bash
# 1. 获取 API Key (免费): https://platform.moonshot.cn/

# 2. 启动
cd llm_assistant
export KIMI_API_KEY=your_key
./start.sh

# 3. 浏览器自动打开，或手动打开 frontend/chat.html
```

### 没有 API Key？用轻量版！

```bash
./start.sh
# 访问 http://localhost:8080/smart.html
# 或直接双击打开 smart.html
```

---

## 🎯 功能对比

| 版本 | 核心技术 | 特点 | 适合场景 |
|-----|---------|------|---------|
| **🤖 LLM 智能版** | Kimi + RAG | 自然对话、多轮交流、个性化建议 | 复杂问题、深度咨询 |
| **🔧 轻量版** | 关键词匹配 | 即开即用、快速响应 | 标准问题、快速查询 |
| **📚 浏览版** | 静态展示 | 系统学习、完整查阅 | 研究学习、备课 |

---

## 💬 示例对话

**你**: 如何面试技术强但沟通能力一般的候选人？

**🤖 LLM 版**:
> 这是一个经典的"技术 vs 协作"权衡问题。基于 Andy Grove 的面试框架，我建议...
> [详细分析 + 具体问题建议 + TODO 清单]

**🔧 轻量版**:
> 匹配 Skills: interview-questioning-techniques
> [提取的 Skill 内容 + 预设 TODO]

---

## 📖 更多文档

- [详细说明](README.md)
- [功能对比](FEATURES.md) - 选择适合你的版本
- [快速开始](QUICKSTART.md) - 详细启动步骤
- [LLM 版文档](llm_assistant/README.md)

---

## ❓ 常见问题

**Q: 没有 API Key 怎么办？**
A: 使用轻量版（smart.html），无需 API Key，离线可用！

**Q: 如何获取 Kimi API Key？**
A: 访问 https://platform.moonshot.cn/，注册即有免费额度

**Q: 可以部署到服务器吗？**
A: 可以！llm_assistant/backend 是标准 FastAPI 应用

**Q: 数据安全吗？**
A: 所有数据本地处理，LLM 版仅调用 API，不存储对话

---

## 🎉 开始吧！

选择你的路径：

1. **[🤖 启动 LLM 智能版](llm_assistant/)** - 最强大的体验
2. **[🔧 使用轻量版](smart.html)** - 即开即用
3. **[📚 浏览所有 Skills](index.html)** - 系统学习

---

Made with ❤️ based on High Output Management
