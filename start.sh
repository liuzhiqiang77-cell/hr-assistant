#!/bin/bash

# 初级 HR 助手启动脚本

echo "🚀 启动 初级 HR 助手..."
echo ""

# 检查 Python3
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    echo "❌ 未找到 Python，请手动在浏览器中打开 index.html"
    exit 1
fi

# 启动 HTTP 服务器
echo "📁 工作目录: $(pwd)"
echo "🌐 访问地址: http://localhost:8080"
echo ""
echo "按 Ctrl+C 停止服务器"
echo ""

$PYTHON -m http.server 8080
