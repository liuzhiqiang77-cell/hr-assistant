#!/bin/bash
# 一键部署到 Railway

echo "🚀 开始部署 HR 助手到 Railway..."
echo ""

# 检查依赖
if ! command -v git &> /dev/null; then
    echo "❌ 请先安装 Git"
    exit 1
fi

# 进入项目目录
cd "$(dirname "$0")"

# 1. 初始化 Git（如果需要）
if [ ! -d ".git" ]; then
    echo "📦 初始化 Git 仓库..."
    git init
    git add .
    git commit -m "Initial commit"
fi

# 2. 检查远程仓库
if ! git remote -v > /dev/null 2>&1; then
    echo ""
    echo "⚠️  请先创建 GitHub 仓库并添加远程地址："
    echo ""
    echo "1. 访问 https://github.com/new"
    echo "2. 创建新仓库（如 hr-assistant）"
    echo "3. 然后运行："
    echo "   git remote add origin https://github.com/你的用户名/hr-assistant.git"
    echo "   git branch -M main"
    echo "   git push -u origin main"
    echo ""
    exit 1
fi

# 3. 提交更改
echo "📤 推送代码到 GitHub..."
git add .
git commit -m "Prepare for deployment" || true
git push

echo ""
echo "✅ 代码已推送到 GitHub"
echo ""
echo "接下来："
echo ""
echo "1. 访问 https://railway.app/"
echo "2. 使用 GitHub 登录"
echo "3. 点击 'New Project' → 'Deploy from GitHub repo'"
echo "4. 选择你的仓库"
echo "5. 在 Variables 中添加："
echo "   LLM_PROVIDER=deepseek"
echo "   DEEPSEEK_API_KEY=sk-cd5df232af6a4fc188cbdea0e889659f"
echo "   DEEPSEEK_BASE_URL=https://api.deepseek.com/v1"
echo "   DEFAULT_MODEL=deepseek-chat"
echo ""
echo "6. 部署完成后，获取域名并更新 frontend/chat.html 中的 API_BASE"
echo ""
echo "📖 详细文档: DEPLOY.md"
