# 🔧 API Key 调试指南

## 当前状态

❌ 两个 API Key 都返回 401 错误

## 可能原因

### 1. Key 根本未激活
Kimi 的 Key 有时需要审核或激活才能使用。

**检查步骤:**
1. 访问 https://platform.moonshot.cn/
2. 登录后查看 "API Key 管理"
3. 确认 Key 状态是 "正常" 而非 "待审核" 或 "已禁用"

### 2. 账户未完成验证
新注册账户可能需要：
- 手机验证
- 实名认证
- 绑定支付方式（即使有免费额度）

### 3. 使用错误的 API 端点
尝试其他端点：

```bash
# 测试 1: 标准端点
curl https://api.moonshot.cn/v1/models \
  -H "Authorization: Bearer $KIMI_API_KEY"

# 测试 2: 旧版端点
curl https://api.moonshot.cn/v1/chat/completions \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"moonshot-v1-8k","messages":[{"role":"user","content":"hi"}]}'
```

### 4. Key 复制错误
检查是否有：
- 额外空格
- 换行符
- 缺少前缀 `sk-kimi-`

---

## ✅ 解决方案

### 方案 A: 重新创建 Key（推荐）

1. 访问 https://platform.moonshot.cn/
2. 删除所有现有 Key
3. 点击 "创建 API Key"
4. **立即复制**（只显示一次）
5. 粘贴到终端测试：

```bash
export KIMI_API_KEY=你刚复制的_key
curl https://api.moonshot.cn/v1/models \
  -H "Authorization: Bearer $KIMI_API_KEY"
```

### 方案 B: 检查账户状态

在 https://platform.moonshot.cn/ 检查：
- [ ] 账户已实名认证
- [ ] 手机已绑定
- [ ] 有可用额度（> 0）
- [ ] 没有欠费

### 方案 C: 联系客服

如果以上都不行，联系 Kimi 客服：
- 平台内有在线客服
- 或发送邮件到 support@moonshot.cn

---

## 🚀 临时方案：使用轻量版

在解决 API Key 问题前，先用轻量版：

```bash
cd /Users/ZQ/Desktop/hr-assistant
python3 -m http.server 8080
# 访问 http://localhost:8080/smart.html
```

轻量版功能完整，无需 API Key！

---

## 📝 测试脚本

保存为 `check_key.sh`：

```bash
#!/bin/bash
KEY="$1"
if [ -z "$KEY" ]; then
    echo "用法: ./check_key.sh sk-kimi-xxxxx"
    exit 1
fi

echo "测试 API Key: ${KEY:0:10}..."

curl -s https://api.moonshot.cn/v1/models \
  -H "Authorization: Bearer $KEY" | jq .
```

运行：
```bash
chmod +x check_key.sh
./check_key.sh sk-kimi-xxxxx
```

---

## ❓ 常见问题

**Q: 为什么免费额度还报错？**
A: 免费额度需要账户验证后才能使用。

**Q: Key 刚创建的为什么无效？**
A: 可能需要几分钟激活，或账户未完成验证。

**Q: 可以用其他 LLM 吗？**
A: 可以！修改 `backend/hr_assistant.py` 中的 base_url 和 api_key：
- OpenAI: https://api.openai.com/v1
- Claude: https://api.anthropic.com
- 或其他兼容 OpenAI 格式的 API

---

请尝试重新创建 API Key 并立即测试！
