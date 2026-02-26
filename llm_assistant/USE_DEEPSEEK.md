# 🚀 使用 DeepSeek API（推荐）

DeepSeek 是国内优秀的 AI 服务，**无需复杂认证**，注册即有免费额度！

---

## 📋 快速步骤

### 1. 获取 DeepSeek API Key（1分钟）

1. 访问 https://platform.deepseek.com/
2. 用手机号注册（秒完成）
3. 进入 "API Keys" 页面
4. 点击 "创建 API Key"
5. **立即复制**（只显示一次！）

**免费额度**：5000万 tokens（完全够用）

---

### 2. 配置并启动

**方式 A: 环境变量（推荐）**

```bash
cd /Users/ZQ/Desktop/hr-assistant/llm_assistant
export DEEPSEEK_API_KEY=sk-你的_deepseek_key
./start_deepseek.sh
```

**方式 B: 编辑配置文件**

```bash
cd /Users/ZQ/Desktop/hr-assistant/llm_assistant/backend
cp .env.deepseek .env
# 编辑 .env 文件，填入你的 Key
nano .env  # 或 vi .env
```

.env 文件内容：
```
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-你的_deepseek_key
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEFAULT_MODEL=deepseek-chat
```

然后启动：
```bash
cd /Users/ZQ/Desktop/hr-assistant/llm_assistant
./start_deepseek.sh
```

---

### 3. 测试 API

```bash
curl https://api.deepseek.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

---

## ✅ 优势对比

| 特性 | Kimi | DeepSeek |
|-----|------|----------|
| 注册难度 | 需要审核 | 手机注册，秒过 |
| 免费额度 | 较少 | 5000万 tokens |
| 实名认证 | 需要 | 不需要 |
| API 稳定性 | 一般 | 优秀 |
| 回答质量 | 很好 | 很好 |
| 速度 | 快 | 很快 |

---

## 🎯 获取 API Key 截图步骤

```
1. 打开 https://platform.deepseek.com/
   ↓
2. 点击 "注册" → 输入手机号 → 验证码
   ↓
3. 登录后点击左侧 "API Keys"
   ↓
4. 点击 "创建 API Key" 按钮
   ↓
5. 输入名称（如 "HR助手"）→ 确认
   ↓
6. ⚠️ 立即复制 Key（只显示一次！）
   ↓
7. 粘贴到终端设置环境变量
```

---

## 🆘 常见问题

**Q: 免费额度用完怎么办？**
A: 5000万 tokens 大约能对话 10-20 万次，用完后可以充值（很便宜）或注册新账号。

**Q: DeepSeek 和 Kimi 哪个好？**
A: 对于 HR 助手这个场景，两者都很好。DeepSeek 更稳定且免费额度更多。

**Q: 可以切换回 Kimi 吗？**
A: 可以！修改 backend/.env：
```
LLM_PROVIDER=kimi
KIMI_API_KEY=你的_kimi_key
```

**Q: 支持其他 API 吗？**
A: 支持！只要是 OpenAI 格式的 API 都可以（OpenRouter、SiliconFlow 等），修改配置即可。

---

## 🚀 现在就去注册！

👉 https://platform.deepseek.com/

注册后把 API Key 发给我，我帮你启动！
