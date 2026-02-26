# 📤 使用 Git 命令行上传（解决文件太多问题）

## 问题
GitHub 网页上传限制：
- 最多 100 个文件
- 不能保留目录结构
- 我们的项目有 800+ 个文件

## 解决方案：使用 Git 命令行

### 步骤 1：打开终端

Mac: 打开 "终端" (Terminal) 应用
Windows: 打开 "Git Bash" 或 "命令提示符"

### 步骤 2：进入项目文件夹

```bash
cd /path/to/hr-assistant  # 替换为实际路径

# 例如：
cd ~/Desktop/hr-assistant
```

### 步骤 3：配置 Git（如果第一次使用）

```bash
git config --global user.name "liuzhiqiang77-cell"
git config --global user.email "liuzhiqiang77-cell@users.noreply.github.com"
```

### 步骤 4：初始化并上传

```bash
# 1. 初始化 Git 仓库
git init

# 2. 添加所有文件（包括子目录）
git add .

# 3. 提交
git commit -m "Initial commit: HR Assistant with 287 skills"

# 4. 连接远程仓库
git remote add origin https://github.com/liuzhiqiang77-cell/hr-assistant.git

# 5. 推送到 GitHub
git branch -M main
git push -u origin main
```

### 步骤 5：输入凭据

如果提示输入用户名和密码：
- **用户名**: `liuzhiqiang77-cell`
- **密码**: 使用你的 GitHub Personal Access Token
  - 即：`【你的 GitHub Personal Access Token】`

---

## 🖥️ 使用 GitHub Desktop（图形界面）

如果不习惯命令行，使用 GitHub Desktop 更简单：

### 1. 下载安装
https://desktop.github.com/

### 2. 登录
打开 GitHub Desktop，用 GitHub 账号登录

### 3. 添加本地仓库
- File → Add local repository
- 选择解压后的 `hr-assistant` 文件夹
- 点击 Add

### 4. 提交并推送
- 在 Summary 输入：`Initial commit`
- 点击 **Commit to main**
- 点击 **Publish repository**
- 选择 `liuzhiqiang77-cell/hr-assistant`
- 点击 **Publish**

---

## ✅ 验证上传成功

上传完成后，访问：
```
https://github.com/liuzhiqiang77-cell/hr-assistant
```

应该能看到：
- 📁 llm_assistant/
- 📁 skills/
- 📁 data/
- 📄 index.html
- 等等...

---

## 🚀 然后回到 Railway

1. 刷新 Railway 页面
2. 点击 **New Project**
3. 选择 **Deploy from GitHub repo**
4. 选择 `hr-assistant`
5. 点击 **Deploy**

这次应该正常了！
