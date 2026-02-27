#!/bin/bash
# 修复启动脚本

cd llm_assistant/backend

# 确保数据文件路径正确
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# 启动服务
exec python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}