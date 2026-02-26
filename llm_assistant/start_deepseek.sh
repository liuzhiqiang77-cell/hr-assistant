#!/bin/bash

echo "🚀 启动 LLM HR 助手 (DeepSeek 版)..."
echo ""

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 需要 Python 3"
    exit 1
fi

cd "$(dirname "$0")"

# 激活虚拟环境
if [ ! -d "venv" ]; then
    echo "📦 创建虚拟环境..."
    python3 -m venv venv
fi
source venv/bin/activate

# 安装依赖
echo "📦 安装依赖..."
pip install -q -r backend/requirements.txt

echo ""
echo "🔧 配置 DeepSeek API..."

# 检查 DeepSeek API Key
if [ -z "$DEEPSEEK_API_KEY" ]; then
    if [ -f "backend/.env" ]; then
        # 检查是否已有 DeepSeek 配置
        if grep -q "LLM_PROVIDER=deepseek" backend/.env; then
            export $(grep -v '^#' backend/.env | xargs)
        else
            echo "⚠️  未找到 DeepSeek 配置"
            echo ""
            echo "请提供 DeepSeek API Key："
            echo "1. 访问 https://platform.deepseek.com/ 获取"
            echo "2. 然后运行: export DEEPSEEK_API_KEY=your_key"
            echo "3. 或编辑 backend/.env 文件添加:"
            echo "   LLM_PROVIDER=deepseek"
            echo "   DEEPSEEK_API_KEY=your_key"
            exit 1
        fi
    else
        echo "⚠️  未找到 .env 文件"
        echo ""
        echo "请先配置 API Key："
        echo "export DEEPSEEK_API_KEY=your_deepseek_api_key"
        exit 1
    fi
fi

echo "✅ API Key 已配置"
echo ""

# 启动后端
echo "🌐 启动后端服务..."
echo "   API 地址: http://localhost:8000"
echo ""

cd backend
LLM_PROVIDER=deepseek python main.py &
BACKEND_PID=$!
cd ..

# 等待后端启动
sleep 4

# 检查后端是否启动成功
if ! curl -s http://localhost:8000/health > /dev/null; then
    echo "❌ 后端启动失败，请检查配置"
    exit 1
fi

echo "✅ 后端服务已启动"
echo ""

# 打开前端
echo "🌍 打开前端界面..."
if command -v open &> /dev/null; then
    open frontend/chat.html
elif command -v xdg-open &> /dev/null; then
    xdg-open frontend/chat.html
else
    echo "请手动打开: frontend/chat.html"
fi

echo ""
echo "=========================================="
echo "✅ LLM HR 助手 (DeepSeek) 已启动!"
echo "=========================================="
echo ""
echo "后端 API: http://localhost:8000"
echo "前端界面: frontend/chat.html"
echo "API 提供商: DeepSeek"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

wait $BACKEND_PID
