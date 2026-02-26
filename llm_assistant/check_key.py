#!/usr/bin/env python3
"""检查 Kimi API Key 状态"""

import requests
import sys

API_KEY = "sk-kimi-g944cWemMxbkVjEntamPK472hFEgTCU1u52slrKLk6kXYI1KqV5Wjyj2lXZWceOQ"

print(f"🔍 检查 API Key: {API_KEY[:15]}...")
print(f"   长度: {len(API_KEY)}")
print()

# 测试 1: 获取模型列表
print("测试 1: 获取模型列表...")
try:
    resp = requests.get(
        "https://api.moonshot.cn/v1/models",
        headers={"Authorization": f"Bearer {API_KEY}"},
        timeout=10
    )
    print(f"   状态码: {resp.status_code}")
    print(f"   响应: {resp.text[:200]}")
except Exception as e:
    print(f"   错误: {e}")

print()

# 测试 2: 简单对话
print("测试 2: 简单对话...")
try:
    resp = requests.post(
        "https://api.moonshot.cn/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "moonshot-v1-8k",
            "messages": [{"role": "user", "content": "hi"}],
            "max_tokens": 10
        },
        timeout=10
    )
    print(f"   状态码: {resp.status_code}")
    print(f"   响应: {resp.text[:200]}")
except Exception as e:
    print(f"   错误: {e}")

print()
print("---")
print("如果都返回 401，说明 Key 确实无效")
print("请访问 https://platform.moonshot.cn/ 检查：")
print("  1. Key 是否已激活")
print("  2. 账户是否完成验证")
print("  3. 是否有可用额度")
