#!/usr/bin/env python3
"""
测试 Kimi API Key 是否有效
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# 加载 .env
env_path = Path(__file__).parent / "backend" / ".env"
if env_path.exists():
    load_dotenv(env_path)
    print(f"✅ 已加载 .env 文件")
else:
    print(f"⚠️ 未找到 .env 文件: {env_path}")

api_key = os.getenv("KIMI_API_KEY")

if not api_key:
    print("❌ 错误: KIMI_API_KEY 未设置")
    print("\n请设置环境变量或创建 .env 文件:")
    print('echo "KIMI_API_KEY=your_key_here" > backend/.env')
    sys.exit(1)

print(f"✅ API Key 已设置 (长度: {len(api_key)})")
print(f"   前10位: {api_key[:10]}...")

# 测试 API
try:
    from openai import OpenAI
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.moonshot.cn/v1"
    )
    
    print("\n🔄 正在测试 API 连接...")
    
    response = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say 'API test successful' and nothing else."}
        ],
        max_tokens=20
    )
    
    result = response.choices[0].message.content
    print(f"\n✅ API 测试成功!")
    print(f"📝 响应: {result}")
    
except Exception as e:
    print(f"\n❌ API 测试失败: {e}")
    print("\n可能的原因:")
    print("1. API Key 已过期或被撤销")
    print("2. 账户没有可用额度")
    print("3. 网络连接问题")
    print("\n建议:")
    print("- 访问 https://platform.moonshot.cn/ 检查 API Key 状态")
    print("- 重新生成一个新的 API Key")
    sys.exit(1)
