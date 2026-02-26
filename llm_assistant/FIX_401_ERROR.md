# 🔧 修复 401 认证错误

## 错误原因

`401 Invalid Authentication` 表示 API Key 无效或认证失败。

## 可能的原因

1. **API Key 已过期** - Kimi 的 Key 可能有有效期限制
2. **API Key 被撤销** - 可能已在平台上删除
3. **API 端点错误** - 可能需要使用不同的 base URL
4. **Key 格式问题** - 可能复制时包含了多余字符

---

## ✅ 解决方案

### 方案 1: 检查 API Key 状态

访问 https://platform.moonshot.cn/ 检查：
1. 你的 API Key 是否还在有效期内
2. 是否还有剩余额度
3. Key 是否被禁用或删除

### 方案 2: 重新生成 API Key

1. 登录 https://platform.moonshot.cn/
2. 进入 "API Key 管理"
3. 删除旧 Key，创建新 Key
4. 更新 `.env` 文件：

```bash
cd /Users/ZQ/Desktop/hr-assistant/llm_assistant/backend
echo "KIMI_API_KEY=你的新_api_key" > .env
```

### 方案 3: 使用轻量版（无需 API Key）

如果不想处理 API Key 问题，可以直接使用轻量版：

```bash
cd /Users/ZQ/Desktop/hr-assistant
./start.sh
# 访问 http://localhost:8080/smart.html
```

轻量版基于本地关键词匹配，无需 API Key，离线可用！

### 方案 4: 测试 API Key

使用 curl 测试 API Key 是否有效：

```bash
curl https://api.moonshot.cn/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KIMI_API_KEY" \
  -d '{
    "model": "moonshot-v1-8k",
    "messages": [{"role": "user", "content": "Hello"}]
  }'
```

如果返回 401，说明 Key 确实无效。

---

## 🚀 快速切换

如果你想立即使用，切换到轻量版：

```bash
# 1. 停止当前后端服务（按 Ctrl+C）

# 2. 启动轻量版
cd /Users/ZQ/Desktop/hr-assistant
./start.sh

# 3. 浏览器访问
open smart.html
```

轻量版功能：
- ✅ 关键词匹配 Skills
- ✅ 预设 TODO 清单
- ✅ 离线使用
- ✅ 快速响应

---

## 📝 获取新的 API Key

1. 访问 https://platform.moonshot.cn/
2. 注册/登录账号
3. 进入 "API Key 管理"
4. 点击 "创建 API Key"
5. 复制新 Key（只显示一次，请保存）
6. 更新 `.env` 文件
7. 重新启动服务

---

## 🔍 调试信息

当前配置：
- API Key 长度: 72 字符
- API 端点: https://api.moonshot.cn/v1
- 模型: moonshot-v1-8k

如需帮助，请检查 Kimi 平台的状态和文档。
