# 🚀 快速开始指南

## 功能概述

**初级 HR 助手** - 基于 Andy Grove《High Output Management》的智能管理工具

### ✨ 核心功能

1. **🤖 智能问答** - 输入问题 → 自动匹配 Skills → 生成 TODO 清单
2. **📚 浏览 Skills** - 分类浏览 287 个管理 Skills
3. **💬 场景模拟** - 常见 HR 场景快速指导

---

## 🎯 使用方式（推荐顺序）

### 方式 1: 智能 Web 问答（最直观）

```bash
./start.sh
```

浏览器访问：**http://localhost:8080/smart.html**

**使用示例：**
1. 在输入框中描述你的问题：
   - "如何面试一个技术强但沟通能力一般的候选人？"
   - "员工绩效突然下降，我该怎么跟他谈？"
   - "新员工入职后如何帮助他快速融入？"

2. 点击"获取专业建议"

3. 获得：
   - 🔍 匹配的相关 Skills（1-3 个）
   - 💡 核心建议和行动指南
   - ✅ 具体的 TODO 清单（含优先级和时间建议）

---

### 方式 2: 命令行快速问答

```bash
# 直接提问（单次）
python ask.py "如何进行绩效面谈？"

# 进入交互模式
python ask.py
# 然后输入你的问题...
```

**示例输出：**
```
======================================================================
📋 回答
======================================================================
基于您的问题，我为您找到了 3 个相关的管理 Skills：

1. **performance-review-framework** (相关度: 85%)
2. **performance-diagnosis-can't-vs-won't** (相关度: 72%)
3. **one-on-one-meeting-protocol** (相关度: 68%)

---

### 💡 核心建议
[提取的关键内容]

======================================================================
✅ 建议行动清单 (TODO)
======================================================================

1. 🔴 收集员工绩效数据（产出、项目结果）
   优先级: 高 | 建议时间: 面谈前 1 周

2. 🔴 准备正面反馈和改进建议
   优先级: 高 | 建议时间: 面谈前 3 天

3. 🟡 预约一对一会议时间
   优先级: 中 | 建议时间: 面谈前 1 周
...
```

---

### 方式 3: 浏览所有 Skills

```bash
./start.sh
```

访问：**http://localhost:8080**

- 📂 按 8 大模块分类浏览
- 🔍 搜索任意关键词
- 📖 查看完整的 Skill 内容

---

## 📂 项目结构

```
hr-assistant/
├── smart.html          # 🌟 智能问答 Web 界面
├── index.html          # Skills 浏览器
├── ask.py              # 命令行问答工具
├── app/
│   ├── intelligent_hr.py   # 智能匹配算法
│   └── main.py            # Streamlit 版本
├── data/
│   └── skills.json        # 287 个 Skills 数据
├── skills/               # Skills 源文件
│   ├── candidate-interview-techniques/
│   ├── performance-review-framework/
│   └── ... (287 个)
├── start.sh              # 启动脚本
└── README.md
```

---

## 🎓 支持的问题类型

| 场景类型 | 示例问题 | 匹配 Skills |
|---------|---------|------------|
| 🎯 招聘面试 | "如何设计面试问题？" | candidate-interview-* |
| 📊 绩效管理 | "绩效面谈怎么做？" | performance-review-* |
| 🚀 职业发展 | "如何帮助员工规划职业？" | career-* |
| 💰 薪酬晋升 | "晋升决策要考虑什么？" | compensation-promotion-* |
| 🗣️ 一对一 | "一对一会议怎么开？" | one-on-one-* |
| 👥 员工关系 | "员工想离职怎么办？" | employee-retention-* |

---

## 💡 提示

1. **问题越具体，匹配越准确**
   - ✅ "如何面试一个技术强但沟通能力差的候选人"
   - ❌ "面试技巧"

2. **TODO 清单可以导出**
   - Web 版支持导出为文本文件
   - 方便打印或分享给团队

3. **配合 Kimi CLI 使用**
   - 本工具提供快速参考
   - 复杂问题可在 `kimi` CLI 中获得更深入指导

---

## 🔧 故障排除

**问题：无法加载数据**
```bash
# 确保 data/skills.json 存在
ls data/skills.json

# 如不存在，重新生成
cd /Users/ZQ/Desktop/myskill.pdf
python3 << 'EOF'
import json
# ... 生成脚本
EOF
```

**问题：端口被占用**
```bash
# 更换端口
python3 -m http.server 8081
# 然后访问 http://localhost:8081
```

---

开始您的智能 HR 之旅吧！🎉
