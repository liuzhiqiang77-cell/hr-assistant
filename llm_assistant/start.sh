#!/bin/bash

echo "🚀 启动 LLM HR 助手..."
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 需要 Python 3"
    exit 1
fi

cd "$(dirname "$0")"

# 检查虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
source venv/bin/activate

# 安装依赖
echo "📦 安装依赖..."
pip install -q -r backend/requirements.txt

# 检查环境变量
if [ -z "$KIMI_API_KEY" ]; then
    if [ -f "backend/.env" ]; then
        export $(grep -v '^#' backend/.env | xargs)
    else
        echo "⚠️  警告: KIMI_API_KEY 未设置"
        echo "请从 https://platform.moonshot.cn/ 获取 API Key"
        echo "然后运行: export KIMI_API_KEY=your_key"
        echo ""
    fi
fi

# 启动后端
echo "🌐 启动后端服务..."
echo "   API 地址: http://localhost:8000"
echo ""

# 在后台启动后端
cd backend
python main.py &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 3

# 打开前端
echo "🌍 打开前端界面..."
echo ""

if command -v open &> /dev/null; then
    open frontend/chat.html
elif command -v xdg-open &> /dev/null; then
    xdg-open frontend/chat.html
else
    echo "请手动打开: frontend/chat.html"
fi

echo "✅ LLM HR 助手已启动!"
echo ""
echo "后端 API: http://localhost:8000"
echo "前端界面: frontend/chat.html"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

# 等待后端进程
wait $BACKEND_PID
