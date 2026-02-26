# 🚀 HR 助手部署指南（liuzhiqiang77-cell 专用）

GitHub 用户名: `liuzhiqiang77-cell`
预计仓库地址: `https://github.com/liuzhiqiang77-cell/hr-assistant`

---

## 第一步：在 GitHub 创建仓库

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `hr-assistant`
   - **Description**: 基于 Andy Grove《High Output Management》的智能 HR 助手
   - **Public** ✅ （免费）
   - **Add a README**: ❌ （不勾选，我们已有 README）
3. 点击 **Create repository**

---

## 第二步：推送代码到 GitHub

在项目目录运行以下命令：

```bash
cd /Users/ZQ/Desktop/hr-assistant

# 初始化 Git 仓库
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: HR Assistant with DeepSeek AI"

# 添加远程仓库（用你的用户名）
git remote add origin https://github.com/liuzhiqiang77-cell/hr-assistant.git

# 推送代码
git branch -M main
git push -u origin main
```

---

## 第三步：部署到 Railway

### 3.1 登录 Railway

1. 访问 https://railway.app/
2. 点击 **Login** → **Continue with GitHub**
3. 授权 Railway 访问你的 GitHub 仓库

### 3.2 创建项目

1. 点击 **New Project**
2. 选择 **Deploy from GitHub repo**
3. 找到并选择 `liuzhiqiang77-cell/hr-assistant`
4. 点击 **Deploy**

Railway 会自动开始部署！

### 3.3 配置环境变量

部署完成后：

1. 点击项目进入 Dashboard
2. 点击顶部 **Variables** 标签
3. 点击 **New Variable** 添加以下变量：

```
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-cd5df232af6a4fc188cbdea0e889659f
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEFAULT_MODEL=deepseek-chat
```

4. Railway 会自动重新部署

### 3.4 获取域名

1. 点击 **Settings** 标签
2. 在 **Environment** 下方找到 **Domains**
3. 复制生成的域名，例如：
   ```
   https://hr-assistant-production.up.railway.app
   ```

---

## 第四步：更新前端 API 地址

### 4.1 修改配置文件

编辑 `llm_assistant/frontend/chat.html`：

找到第 525 行附近：
```javascript
const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://hr-assistant-production.up.railway.app';  // ← 改成你的实际域名
```

### 4.2 提交更改

```bash
cd /Users/ZQ/Desktop/hr-assistant

git add llm_assistant/frontend/chat.html
git commit -m "Update API endpoint for production"
git push
```

Railway 会自动重新部署！

---

## 第五步：访问你的应用

### 后端 API
```
https://你的域名.railway.app
```

测试：
```bash
curl https://你的域名.railway.app/health
```

### 前端界面
打开本地文件：
```
/Users/ZQ/Desktop/hr-assistant/llm_assistant/frontend/chat.html
```

前端会自动连接到线上后端！

---

## 第六步：部署前端到 GitHub Pages（可选）

如果你想让前端也在线：

### 6.1 创建 gh-pages 分支

```bash
cd /Users/ZQ/Desktop/hr-assistant
git checkout -b gh-pages
```

### 6.2 创建前端部署文件

```bash
# 复制前端文件到根目录
cp llm_assistant/frontend/chat.html index.html
cp -r llm_assistant/frontend/data . 2>/dev/null || true

# 修改 index.html 中的 API 地址
# 把 API_BASE 改成你的 Railway 域名

# 提交
git add index.html
git commit -m "Add GitHub Pages frontend"
git push origin gh-pages
```

### 6.2 启用 GitHub Pages

1. 访问 https://github.com/liuzhiqiang77-cell/hr-assistant/settings/pages
2. **Source**: 选择 "Deploy from a branch"
3. **Branch**: 选择 "gh-pages" → "/ (root)"
4. 点击 **Save**

等待几分钟后，访问：
```
https://liuzhiqiang77-cell.github.io/hr-assistant
```

---

## 📋 部署检查清单

- [x] GitHub 仓库已创建: `liuzhiqiang77-cell/hr-assistant`
- [x] 代码已推送到 GitHub
- [ ] Railway 项目已创建
- [ ] 环境变量已配置
- [ ] 域名已获取
- [ ] 前端 API 地址已更新
- [ ] 测试对话功能正常
- [ ] （可选）GitHub Pages 已启用

---

## 🌐 最终访问地址

| 服务 | 地址 | 状态 |
|------|------|------|
| 后端 API | `https://xxx.railway.app` | 部署后获取 |
| 前端 (GitHub Pages) | `https://liuzhiqiang77-cell.github.io/hr-assistant` | 可选 |
| 前端 (本地) | `file://.../frontend/chat.html` | ✅ 可用 |

---

## 🆘 故障排除

### Q: GitHub 推送失败？
A: 检查是否已添加 SSH Key 或使用 HTTPS 凭据
```bash
git remote set-url origin https://liuzhiqiang77-cell:你的token@github.com/liuzhiqiang77-cell/hr-assistant.git
```

### Q: Railway 部署失败？
A: 检查日志：
- Railway Dashboard → 项目 → Deployments → 查看最新日志

### Q: API 调用跨域错误？
A: 确保前端域名在 backend/main.py 的 CORS 配置中

### Q: DeepSeek API 调用失败？
A: 检查 Railway 环境变量是否正确设置

---

## 🎉 完成！

部署成功后，你可以：
- 分享链接给团队使用
- 在手机上访问
- 添加自定义域名

需要帮助随时告诉我！
