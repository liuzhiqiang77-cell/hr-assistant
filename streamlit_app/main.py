"""
初级 HR 助手 - 基于 High Output Management 的管理学 Skills
"""

import streamlit as st
import os
import glob
import yaml
import re
from pathlib import Path

# 页面配置
st.set_page_config(
    page_title="初级 HR 助手",
    page_icon="👥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 初始化 session state
if 'selected_skill' not in st.session_state:
    st.session_state.selected_skill = None
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Skills 目录
SKILLS_DIR = Path(__file__).parent.parent / "skills"

@st.cache_data
def load_all_skills():
    """加载所有 skills 的元数据"""
    skills = []
    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        try:
            content = skill_file.read_text(encoding='utf-8')
            # 解析 frontmatter
            if content.startswith('---'):
                _, frontmatter, body = content.split('---', 2)
                metadata = yaml.safe_load(frontmatter)
                skills.append({
                    'name': metadata.get('name', skill_file.parent.name),
                    'description': metadata.get('description', ''),
                    'folder': skill_file.parent.name,
                    'path': str(skill_file),
                    'body': body.strip()[:500] + "..." if len(body) > 500 else body.strip()
                })
        except Exception as e:
            continue
    return skills

def categorize_skills(skills):
    """按 HR 模块分类 skills"""
    categories = {
        "🎯 招聘面试": [],
        "📊 绩效管理": [],
        "🚀 职业发展": [],
        "💰 薪酬晋升": [],
        "🗣️ 一对一沟通": [],
        "📚 培训发展": [],
        "👥 员工关系": [],
        "🔄 管理流程": []
    }
    
    for skill in skills:
        name = skill['folder'].lower()
        if any(k in name for k in ['interview', 'candidate', 'hiring']):
            categories["🎯 招聘面试"].append(skill)
        elif any(k in name for k in ['performance', 'review', 'assessment']):
            categories["📊 绩效管理"].append(skill)
        elif any(k in name for k in ['career', 'promotion']):
            categories["🚀 职业发展"].append(skill)
        elif any(k in name for k in ['compensation', 'salary']):
            categories["💰 薪酬晋升"].append(skill)
        elif 'one-on-one' in name:
            categories["🗣️ 一对一沟通"].append(skill)
        elif any(k in name for k in ['training', 'teaching']):
            categories["📚 培训发展"].append(skill)
        elif any(k in name for k in ['employee', 'retention', 'relationship']):
            categories["👥 员工关系"].append(skill)
        else:
            categories["🔄 管理流程"].append(skill)
    
    return categories

# ============ 侧边栏 ============
with st.sidebar:
    st.title("👥 初级 HR 助手")
    st.markdown("---")
    st.markdown("**基于 Andy Grove《High Output Management》**")
    st.markdown("*管理学 Skills 知识库*")
    st.markdown("---")
    
    # 模块选择
    st.subheader("选择 HR 模块")
    
    all_skills = load_all_skills()
    categories = categorize_skills(all_skills)
    
    # 显示各模块数量
    for cat_name, cat_skills in categories.items():
        if cat_skills:
            with st.expander(f"{cat_name} ({len(cat_skills)})"):
                for skill in cat_skills[:5]:  # 只显示前5个
                    if st.button(f"📄 {skill['name'][:30]}...", key=f"btn_{skill['folder']}"):
                        st.session_state.selected_skill = skill
                if len(cat_skills) > 5:
                    st.caption(f"...还有 {len(cat_skills)-5} 个")

# ============ 主页面 ============
st.title("初级 HR 助手")

# 顶部标签页
tab1, tab2, tab3, tab4 = st.tabs(["🏠 首页", "📖 Skill 详情", "💬 模拟对话", "🔍 搜索"])

# ===== Tab 1: 首页 =====
with tab1:
    st.markdown("""
    ## 欢迎使用初级 HR 助手！
    
    本工具基于 **Andy Grove《High Output Management》** 的管理学框架，
    为初级 HR 和团队管理者提供专业的管理指导。
    
    ### 🎯 核心功能模块
    
    | 模块 | 功能 | Skills 数量 |
    |-----|------|-----------|
    | 🎯 招聘面试 | 面试技巧、候选人评估、背景调查 | {} 个 |
    | 📊 绩效管理 | 绩效评估、绩效面谈、问题诊断 | {} 个 |
    | 🚀 职业发展 | 职业规划、晋升管理、人才培养 | {} 个 |
    | 💰 薪酬晋升 | 薪酬设计、晋升决策、激励策略 | {} 个 |
    | 🗣️ 一对一沟通 | 高效一对一、会议技巧、沟通框架 | {} 个 |
    | 📚 培训发展 | 培训设计、经理培训、技能传授 | {} 个 |
    | 👥 员工关系 | 员工保留、关系管理、离职处理 | {} 个 |
    | 🔄 管理流程 | 管理杠杆、时间优化、决策流程 | {} 个 |
    
    ### 🚀 快速开始
    
    1. **从左侧选择模块** - 点击感兴趣的 HR 领域
    2. **查看 Skill 详情** - 了解具体的管理方法论
    3. **模拟对话练习** - 在实际场景中应用
    
    ---
    
    > 💡 **提示**: 左侧边栏显示了所有可用的管理 Skills，点击即可查看详细内容
    """.format(
        len(categories["🎯 招聘面试"]),
        len(categories["📊 绩效管理"]),
        len(categories["🚀 职业发展"]),
        len(categories["💰 薪酬晋升"]),
        len(categories["🗣️ 一对一沟通"]),
        len(categories["📚 培训发展"]),
        len(categories["👥 员工关系"]),
        len(categories["🔄 管理流程"])
    ))
    
    # 统计卡片
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("总 Skills 数", len(all_skills))
    with col2:
        st.metric("HR 模块", 8)
    with col3:
        st.metric("管理方法", "200+")
    with col4:
        st.metric("知识来源", "《High Output Management》")

# ===== Tab 2: Skill 详情 =====
with tab2:
    if st.session_state.selected_skill:
        skill = st.session_state.selected_skill
        st.header(f"📄 {skill['name']}")
        st.markdown(f"**文件夹**: `{skill['folder']}`")
        st.markdown("---")
        st.markdown("#### 描述")
        st.info(skill['description'])
        st.markdown("---")
        st.markdown("#### 内容预览")
        
        # 读取完整内容
        try:
            full_content = Path(skill['path']).read_text(encoding='utf-8')
            # 移除 frontmatter
            if full_content.startswith('---'):
                parts = full_content.split('---', 2)
                if len(parts) >= 3:
                    body = parts[2].strip()
                else:
                    body = full_content
            else:
                body = full_content
            
            st.markdown(body)
        except Exception as e:
            st.error(f"无法读取文件: {e}")
    else:
        st.info("👈 请从左侧选择一个 Skill 查看详情")

# ===== Tab 3: 模拟对话 =====
with tab3:
    st.header("💬 HR 场景模拟对话")
    
    # 场景选择
    scenarios = {
        "🎯 面试场景": [
            "如何设计有效的面试问题？",
            "候选人技术很强但沟通差，怎么评估？",
            "如何进行背景调查？",
            "面试中应该避免哪些偏见？"
        ],
        "📊 绩效场景": [
            "如何给表现不佳的员工反馈？",
            "绩效评估应该关注什么？",
            "员工绩效突然下降怎么办？",
            "如何区分'不能'vs'不愿'？"
        ],
        "🚀 发展场景": [
            "如何帮助员工规划职业发展？",
            "晋升决策应该考虑哪些因素？",
            "如何留住高绩效员工？",
            "新员工如何快速融入？"
        ],
        "🗣️ 沟通场景": [
            "一对一会议应该怎么开？",
            "员工抱怨薪资怎么处理？",
            "如何传达坏消息？",
            "团队冲突如何调解？"
        ]
    }
    
    selected_scenario = st.selectbox("选择场景类型", list(scenarios.keys()))
    
    if selected_scenario:
        question = st.selectbox("选择具体问题", scenarios[selected_scenario])
        
        if st.button("🤖 获取专业建议"):
            with st.spinner("正在分析相关的管理 Skills..."):
                # 根据问题匹配相关的 skills
                related_skills = []
                keywords = question.lower().split()
                
                for skill in all_skills:
                    score = sum(1 for kw in keywords if kw in skill['description'].lower())
                    if score > 0:
                        related_skills.append((skill, score))
                
                related_skills.sort(key=lambda x: x[1], reverse=True)
                top_skills = related_skills[:3]
                
                st.markdown("---")
                st.subheader("📚 相关的管理 Skills")
                
                for skill, score in top_skills:
                    with st.expander(f"📄 {skill['name']}"):
                        st.markdown(skill['description'])
                        st.caption(f"匹配度: {score}")
                
                st.markdown("---")
                st.info("💡 **提示**: 在 Kimi CLI 中使用这些 skills 可以获得更详细的交互式指导")

# ===== Tab 4: 搜索 =====
with tab4:
    st.header("🔍 搜索 Skills")
    
    search_query = st.text_input("输入关键词搜索", placeholder="例如：面试、绩效、晋升...")
    
    if search_query:
        results = []
        query_lower = search_query.lower()
        
        for skill in all_skills:
            score = 0
            if query_lower in skill['name'].lower():
                score += 3
            if query_lower in skill['description'].lower():
                score += 2
            if query_lower in skill.get('body', '').lower():
                score += 1
            
            if score > 0:
                results.append((skill, score))
        
        results.sort(key=lambda x: x[1], reverse=True)
        
        st.markdown(f"找到 **{len(results)}** 个相关 Skills")
        
        for skill, score in results[:10]:
            with st.container():
                col1, col2 = st.columns([4, 1])
                with col1:
                    st.markdown(f"**{skill['name']}**")
                    st.caption(skill['description'][:200] + "...")
                with col2:
                    if st.button("查看", key=f"search_{skill['folder']}"):
                        st.session_state.selected_skill = skill
                        st.rerun()
                st.divider()

# 底部
st.markdown("---")
st.caption("🎓 基于 Andy Grove《High Output Management》| 共 {} 个管理 Skills".format(len(all_skills)))
