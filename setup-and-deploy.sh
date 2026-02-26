#!/bin/bash
# HR 助手一键部署脚本 - liuzhiqiang77-cell 专用

set -e

GITHUB_USER="liuzhiqiang77-cell"
REPO_NAME="hr-assistant"
REPO_URL="https://github.com/$GITHUB_USER/$REPO_NAME.git"

echo "🚀 HR 助手部署脚本"
echo "=================="
echo "GitHub 用户: $GITHUB_USER"
echo "仓库名: $REPO_NAME"
echo ""

# 检查目录
cd "$(dirname "$0")"
echo "📁 当前目录: $(pwd)"

# 检查 Git
if ! command -v git &> /dev/null; then
    echo "❌ 请先安装 Git: https://git-scm.com/download/mac"
    exit 1
fi

# 初始化 Git
echo ""
echo "📦 步骤 1/5: 初始化 Git 仓库..."
if [ -d ".git" ]; then
    echo "   ✅ Git 仓库已存在"
else
    git init
    echo "   ✅ Git 初始化完成"
fi

# 配置 Git（如果需要）
if ! git config user.name &> /dev/null; then
    echo ""
    echo "⚠️  配置 Git 用户信息..."
    git config user.name "liuzhiqiang77-cell"
    git config user.email "liuzhiqiang77-cell@users.noreply.github.com"
fi

# 添加文件
echo ""
echo "📤 步骤 2/5: 添加文件到 Git..."
git add .
git commit -m "Initial commit: HR Assistant with DeepSeek AI" || echo "   ✅ 文件已是最新"

# 检查远程仓库
echo ""
echo "🔗 步骤 3/5: 配置远程仓库..."
if git remote -v > /dev/null 2>&1; then
    echo "   ✅ 远程仓库已配置"
    git remote -v
else
    echo ""
    echo "⚠️  请先创建 GitHub 仓库:"
    echo ""
    echo "   1. 访问: https://github.com/new"
    echo "   2. 仓库名: $REPO_NAME"
    echo "   3. 选择 Public"
    echo "   4. 不要勾选 'Add a README file'"
    echo "   5. 点击 Create repository"
    echo ""
    read -p "完成后按回车继续..."
    
    git remote add origin "$REPO_URL"
    echo "   ✅ 远程仓库已添加"
fi

# 推送代码
echo ""
echo "⬆️  步骤 4/5: 推送到 GitHub..."
git branch -M main
git push -u origin main && echo "   ✅ 推送成功!" || {
    echo ""
    echo "❌ 推送失败，可能原因："
    echo "   1. GitHub 仓库还未创建"
    echo "   2. 需要登录 GitHub 账号"
    echo "   3. 需要配置 Git 凭据"
    echo ""
    echo "尝试使用 HTTPS 凭据推送..."
    echo "请输入 GitHub 用户名和密码（或 Personal Access Token）:"
    git push -u origin main
}

echo ""
echo "✅ 代码已推送到 GitHub!"
echo "   仓库地址: $REPO_URL"

# Railway 部署提示
echo ""
echo "🚄 步骤 5/5: 部署到 Railway"
echo "=================="
echo ""
echo "请按以下步骤操作："
echo ""
echo "1. 访问: https://railway.app/"
echo "2. 点击 Login → Continue with GitHub"
echo "3. 点击 New Project → Deploy from GitHub repo"
echo "4. 选择: $GITHUB_USER/$REPO_NAME"
echo "5. 等待自动部署完成"
echo ""
echo "6. 配置环境变量:"
echo "   - 点击项目 → Variables"
echo "   - 添加以下变量:"
echo ""
echo "     LLM_PROVIDER=deepseek"
echo "     DEEPSEEK_API_KEY=sk-cd5df232af6a4fc188cbdea0e889659f"
echo "     DEEPSEEK_BASE_URL=https://api.deepseek.com/v1"
echo "     DEFAULT_MODEL=deepseek-chat"
echo ""
echo "7. 获取域名:"
echo "   - Settings → Domains"
echo "   - 复制类似 https://xxx.up.railway.app 的地址"
echo ""
echo "8. 更新前端 API 地址:"
echo "   - 编辑 llm_assistant/frontend/chat.html"
echo "   - 修改 API_BASE 为你的 Railway 域名"
echo "   - git add . && git commit -m 'Update API' && git push"
echo ""

# 询问是否打开浏览器
read -p "是否现在打开 Railway 网站? (y/n): " open_browser
if [ "$open_browser" = "y" ]; then
    open https://railway.app/
fi

echo ""
echo "🎉 部署准备完成!"
echo ""
echo "📖 详细文档: DEPLOY_FOR_LIUZHIQIANG.md"
echo ""
