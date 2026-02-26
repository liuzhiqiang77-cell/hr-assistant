# 🚀 手动上传到 Railway 部署指南

## 准备文件

1. 将 `hr-assistant-deploy.zip` 解压到你的电脑
2. 进入解压后的 `hr-assistant` 文件夹

---

## 步骤 1：创建 GitHub 仓库（如果还没有）

1. 访问 https://github.com/new
2. 填写：
   - **Repository name**: `hr-assistant`
   - **Description**: 智能 HR 助手
   - 选择 **Public**
   - **不要勾选** "Add a README file"
3. 点击 **Create repository**

---

## 步骤 2：上传代码到 GitHub

### 方法一：GitHub 网页上传

1. 在新创建的仓库页面，点击 **"uploading an existing file"**
2. 将 `hr-assistant` 文件夹内的所有文件和文件夹拖放到上传区域
3. 点击 **Commit changes**

### 方法二：命令行（推荐）

```bash
cd hr-assistant
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/liuzhiqiang77-cell/hr-assistant.git
git push -u origin main
```

---

## 步骤 3：部署到 Railway

### 3.1 登录 Railway

1. 访问 https://railway.app/
2. 点击 **Login** → **Continue with GitHub**
3. 授权 Railway 访问你的仓库

### 3.2 创建新项目

1. 点击 **New Project**
2. 选择 **"Deploy from GitHub repo"**
3. 找到并选择 `liuzhiqiang77-cell/hr-assistant`
4. 点击 **Deploy**

Railway 会自动开始部署！

---

## 步骤 4：配置环境变量

部署完成后：

1. 点击项目进入 Dashboard
2. 点击顶部 **Variables** 标签
3. 点击 **New Variable**，逐个添加：

```
LLM_PROVIDER=deepseek
DEEPSEEK_API_KEY=sk-cd5df232af6a4fc188cbdea0e889659f
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEFAULT_MODEL=deepseek-chat
```

4. Railway 会自动重新部署

---

## 步骤 5：获取域名

1. 点击 **Settings** 标签
2. 在 **Environment** 下找到 **Domains**
3. 复制生成的域名，例如：
   ```
   https://hr-assistant-production.up.railway.app
   ```

---

## 步骤 6：更新前端 API 地址

### 6.1 修改代码

编辑 `llm_assistant/frontend/chat.html`：

找到第 525 行附近的代码：
```javascript
const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://hr-assistant-production.up.railway.app';  // ← 改成你的实际域名
```

### 6.2 重新上传

```bash
git add llm_assistant/frontend/chat.html
git commit -m "Update API endpoint for production"
git push
```

Railway 会自动重新部署！

---

## 步骤 7：访问你的应用

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
hr-assistant/llm_assistant/frontend/chat.html
```

---

## 常见问题

### Q: 部署失败？
A: 检查 Railway Dashboard 的 Logs 查看错误信息

### Q: API 调用失败？
A: 检查 CORS 配置和环境变量是否正确

### Q: 前端无法连接后端？
A: 确保前端代码中的 `API_BASE` 已更新为正确的域名

---

## 完成！

部署成功后，你可以：
- 分享链接给团队使用
- 在手机上访问
- 添加自定义域名

需要帮助随时联系我！
