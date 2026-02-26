# 🚀 部署到线上指南

## 方案 1：Railway 部署（推荐 ⭐）

Railway 提供免费部署，支持自动 CI/CD。

### 步骤 1：准备代码

```bash
cd /Users/ZQ/Desktop/hr-assistant

# 创建 Git 仓库（如果还没有）
git init
git add .
git commit -m "Initial commit"
```

### 步骤 2：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 创建新仓库（如 `hr-assistant`）
3. 推送代码：

```bash
git remote add origin https://github.com/你的用户名/hr-assistant.git
git branch -M main
git push -u origin main
```

### 步骤 3：部署到 Railway

1. 访问 https://railway.app/
2. 使用 GitHub 登录
3. 点击 "New Project"
4. 选择 "Deploy from GitHub repo"
5. 选择你的 `hr-assistant` 仓库
6. 点击 "Deploy"

### 步骤 4：配置环境变量

在 Railway Dashboard 中：

1. 进入项目 → Variables
2. 添加以下变量：

```
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-cd5df232af6a4fc188cbdea0e889659f
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEFAULT_MODEL=deepseek-chat
```

### 步骤 5：更新前端 API 地址

修改 `llm_assistant/frontend/chat.html`：

```javascript
const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://你的railway域名.railway.app';
```

获取 Railway 域名：
- 在 Railway Dashboard → Settings → Domains
- 复制生成的域名（如 `hr-assistant-production.up.railway.app`）

### 步骤 6：重新部署

```bash
git add .
git commit -m "Update API endpoint"
git push
```

Railway 会自动重新部署！

### 步骤 7：访问

- 后端 API: `https://你的railway域名.railway.app`
- 前端: 直接打开本地 `frontend/chat.html`，或部署到 GitHub Pages

---

## 方案 2：Render 部署

### 后端部署

1. 访问 https://render.com/
2. 创建 New Web Service
3. 连接 GitHub 仓库
4. 配置：
   - **Name**: hr-assistant
   - **Environment**: Python 3
   - **Build Command**: `pip install -r llm_assistant/backend/requirements.txt`
   - **Start Command**: `cd llm_assistant/backend && python main.py`
5. 添加环境变量（同上）
6. 点击 "Create Web Service"

---

## 方案 3：Vercel + 后端分离

### 前端部署到 Vercel

```bash
# 安装 Vercel CLI
npm i -g vercel

# 部署前端
cd llm_assistant/frontend
vercel
```

### 后端部署

使用 Railway/Render 部署后端，然后在 Vercel 中配置 API 地址。

---

## 🔧 国内部署方案

### 阿里云/腾讯云/华为云

1. 购买轻量应用服务器（约 50元/月）
2. 安装 Python、Git
3. 上传代码
4. 使用 PM2 或 Supervisor 运行

```bash
# 服务器端部署脚本
sudo apt update
sudo apt install python3-pip git -y

git clone https://github.com/你的用户名/hr-assistant.git
cd hr-assistant/llm_assistant
pip3 install -r backend/requirements.txt

# 使用 PM2 运行
npm install -g pm2
pm2 start "cd llm_assistant/backend && python3 main.py" --name hr-assistant
```

---

## 📋 部署检查清单

- [ ] 代码已推送到 GitHub
- [ ] 环境变量已配置（API Key 等）
- [ ] 前端 API 地址已更新
- [ ] CORS 配置正确（允许前端域名）
- [ ] 健康检查接口可用 (`/health`)
- [ ] 测试对话功能正常

---

## 🆘 常见问题

### Q: 部署后 API 调用失败？
A: 检查 CORS 配置，确保后端允许前端域名访问。

### Q: 环境变量不生效？
A: 在 Railway/Render Dashboard 中设置，不要放在代码里。

### Q: 免费额度用完？
A: Railway 每月有 $5 免费额度，足够使用。超出后需要绑定信用卡。

### Q: 如何绑定自定义域名？
A: Railway/Render 都支持自定义域名，在 Settings → Domains 中配置。

---

## 🎉 完成！

部署成功后，你可以：
- 分享链接给团队使用
- 配置自定义域名
- 添加访问密码（如需）

需要我帮你选择最适合的部署方案吗？
