#!/bin/bash
# Build script for Render

set -e

echo "🚀 开始构建 HR Assistant..."

# 安装根目录依赖
pip install -r requirements.txt

# 安装后端依赖
pip install -r llm_assistant/backend/requirements.txt

echo "✅ 构建完成！"