#!/usr/bin/env python3
"""
智能 HR 助手 - 命令行版本
使用方法: python ask.py "你的问题"
或者: python ask.py (进入交互模式)
"""

import sys
import json
from pathlib import Path
import os

# 添加 app 目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))
from intelligent_hr import IntelligentHRAssistant

def main():
    print("🚀 正在初始化智能 HR 助手...")
    assistant = IntelligentHRAssistant()
    
    # 检查是否有命令行参数
    if len(sys.argv) > 1:
        # 直接回答问题
        question = " ".join(sys.argv[1:])
        response = assistant.ask(question)
        print_response(response)
    else:
        # 进入交互模式
        interactive_mode(assistant)

def print_response(response):
    """格式化输出回答"""
    print("\n" + "="*70)
    print("📋 回答")
    print("="*70)
    print(response['answer'])
    
    print("\n" + "="*70)
    print("✅ 建议行动清单 (TODO)")
    print("="*70)
    
    for i, todo in enumerate(response['todos'], 1):
        emoji = {'高': '🔴', '中': '🟡', '低': '🟢'}.get(todo['priority'], '⚪')
        print(f"\n{i}. {emoji} {todo['task']}")
        print(f"   优先级: {todo['priority']} | 建议时间: {todo['time']}")
    
    print("\n" + "="*70)

def interactive_mode(assistant):
    """交互模式"""
    print("\n" + "="*70)
    print("👋 欢迎使用智能 HR 助手 - 交互模式")
    print("输入您的管理问题，我会为您匹配最佳 Skills 并生成 TODO 清单")
    print("输入 'quit' 或 'q' 退出")
    print("="*70 + "\n")
    
    while True:
        try:
            question = input("💬 您的问题: ").strip()
            
            if question.lower() in ['quit', 'q', 'exit']:
                print("\n👋 再见！")
                break
            
            if not question:
                continue
            
            print("\n🤔 正在分析...\n")
            response = assistant.ask(question)
            print_response(response)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 再见！")
            break
        except Exception as e:
            print(f"❌ 出错了: {e}")

if __name__ == "__main__":
    main()
