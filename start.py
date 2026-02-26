#!/usr/bin/env python3
"""
启动 HR 助手应用
"""

import subprocess
import sys
from pathlib import Path

def main():
    app_path = Path(__file__).parent / "app" / "main.py"
    
    print("🚀 启动 初级 HR 助手...")
    print(f"📁 应用路径: {app_path}")
    print("🌐 浏览器将自动打开")
    print("-" * 50)
    
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", str(app_path),
            "--server.headless=false",
            "--server.port=8501"
        ])
    except KeyboardInterrupt:
        print("\n👋 已停止 HR 助手")

if __name__ == "__main__":
    main()
