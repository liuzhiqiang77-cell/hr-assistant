#!/bin/bash
# 启动脚本

echo "🚀 启动 HR Assistant..."

# 切换到项目根目录
cd /opt/render/project/src || cd /app || cd .

# 设置 PYTHONPATH
export PYTHONPATH=/opt/render/project/src:/app:$PYTHONPATH

echo "📂 工作目录: $(pwd)"
echo "📂 内容: $(ls -la)"
echo "📂 data 目录: $(ls -la data/ 2>/dev/null || echo 'data not found')"

# 启动后端
cd llm_assistant/backend
exec python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}