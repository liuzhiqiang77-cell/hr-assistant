"""
智能 HR 问答系统
基于 Skills 的语义匹配和 TODO 生成
"""

import json
import re
from pathlib import Path
from collections import Counter
import math
from typing import List, Dict, Tuple

class IntelligentHRAssistant:
    def __init__(self, skills_path: str = None):
        if skills_path is None:
            # 自动查找 skills.json 路径
            current_file = Path(__file__).resolve()
            possible_paths = [
                current_file.parent.parent / "data" / "skills.json",
                Path.cwd() / "data" / "skills.json",
            ]
            for path in possible_paths:
                if path.exists():
                    self.skills_path = path
                    break
            else:
                self.skills_path = possible_paths[0]
        else:
            self.skills_path = Path(skills_path)
        self.skills = []
        self.inverted_index = {}  # 倒排索引
        self.skill_vectors = {}   # Skill 向量
        self.idf = {}            # IDF 值
        self.load_skills()
        self.build_index()
    
    def load_skills(self):
        """加载 Skills 数据"""
        with open(self.skills_path, 'r', encoding='utf-8') as f:
            self.skills = json.load(f)
        print(f"✅ 已加载 {len(self.skills)} 个 Skills")
    
    def tokenize(self, text: str) -> List[str]:
        """分词（简单实现）"""
        # 转换为小写，提取关键词
        text = text.lower()
        # 提取英文单词
        english_words = re.findall(r'\b[a-z]+\b', text)
        # 提取中文字符（长度 >= 2 的词）
        chinese_chars = re.findall(r'[\u4e00-\u9fff]{2,}', text)
        return english_words + chinese_chars
    
    def build_index(self):
        """构建倒排索引和 TF-IDF"""
        # 收集所有文档的词频
        doc_freq = Counter()
        total_docs = len(self.skills)
        
        for skill in self.skills:
            # 合并标题、描述和内容
            text = f"{skill['name']} {skill.get('description', '')} {skill.get('body', '')}"
            tokens = self.tokenize(text)
            
            # 记录词频
            term_freq = Counter(tokens)
            self.skill_vectors[skill['folder']] = term_freq
            
            # 更新文档频率
            for term in set(tokens):
                doc_freq[term] += 1
                if term not in self.inverted_index:
                    self.inverted_index[term] = []
                self.inverted_index[term].append(skill['folder'])
        
        # 计算 IDF
        for term, freq in doc_freq.items():
            self.idf[term] = math.log(total_docs / (freq + 1)) + 1
        
        print(f"✅ 索引构建完成，共 {len(self.inverted_index)} 个词项")
    
    def calculate_similarity(self, query: str, skill: dict) -> float:
        """计算查询与 Skill 的相似度"""
        query_tokens = set(self.tokenize(query))
        skill_folder = skill['folder']
        
        # 获取 skill tokens
        skill_tokens = self.skill_vectors.get(skill_folder, Counter())
        if not skill_tokens:
            return 0.0
        
        skill_token_set = set(skill_tokens.keys())
        
        # 基础相似度：Jaccard 系数
        intersection = query_tokens & skill_token_set
        union = query_tokens | skill_token_set
        base_score = len(intersection) / (len(union) + 1)
        
        # 标题匹配加权
        title_tokens = set(self.tokenize(skill['name']))
        title_matches = query_tokens & title_tokens
        title_bonus = len(title_matches) * 0.5
        
        # 分类匹配加权
        category_bonus = 0
        category_keywords = {
            '面试': ['interview', 'candidate', 'hiring'],
            '绩效': ['performance', 'review', 'assessment'],
            '晋升': ['promotion', 'career'],
            '一对一': ['one-on-one'],
            '培训': ['training', 'teaching'],
            '离职': ['retention', 'departure']
        }
        
        query_lower = query.lower()
        for keyword, related_terms in category_keywords.items():
            if keyword in query_lower:
                skill_text = f"{skill['name']} {skill.get('description', '')}".lower()
                if any(term in skill_text for term in related_terms):
                    category_bonus += 0.3
        
        return base_score + title_bonus + category_bonus
    
    def match_skills(self, question: str, top_k: int = 3) -> List[Tuple[Dict, float]]:
        """
        匹配最相关的 Skills
        
        Args:
            question: 用户问题
            top_k: 返回前 K 个最相关的 Skills
            
        Returns:
            [(skill_dict, similarity_score), ...]
        """
        # 计算所有 skills 的相似度
        similarities = []
        for skill in self.skills:
            score = self.calculate_similarity(question, skill)
            if score > 0:  # 只保留有匹配度的
                similarities.append((skill, score))
        
        # 按相似度排序
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:top_k]
    
    def generate_response(self, question: str, matched_skills: List[Tuple[Dict, float]]) -> Dict:
        """
        生成回答
        
        Returns:
            {
                'question': 原始问题,
                'matched_skills': 匹配的 Skills,
                'answer': 综合回答,
                'todos': TODO 清单
            }
        """
        response = {
            'question': question,
            'matched_skills': [],
            'answer': '',
            'todos': []
        }
        
        # 构建匹配结果
        for skill, score in matched_skills:
            response['matched_skills'].append({
                'name': skill['name'],
                'folder': skill['folder'],
                'description': skill.get('description', '')[:200],
                'relevance': round(score * 100, 1)
            })
        
        # 生成综合回答
        if matched_skills:
            top_skill = matched_skills[0][0]
            response['answer'] = self._compose_answer(question, matched_skills)
            response['todos'] = self._generate_todos(question, top_skill)
        else:
            response['answer'] = "抱歉，没有找到相关的管理 Skills。请尝试用其他方式描述您的问题。"
        
        return response
    
    def _compose_answer(self, question: str, matched_skills: List[Tuple[Dict, float]]) -> str:
        """组合回答内容"""
        parts = []
        
        # 开头
        parts.append(f"基于您的问题，我为您找到了 {len(matched_skills)} 个相关的管理 Skills：\n")
        
        # 列出匹配的 Skills
        for i, (skill, score) in enumerate(matched_skills, 1):
            parts.append(f"\n{i}. **{skill['name']}** (相关度: {score*100:.1f}%)")
            parts.append(f"   - {skill.get('description', '')}")
        
        # 核心建议（基于最匹配的 Skill）
        if matched_skills:
            top_skill = matched_skills[0][0]
            parts.append(f"\n\n---\n")
            parts.append(f"### 💡 核心建议\n")
            
            # 提取关键段落
            body = top_skill.get('body', '')
            # 找包含关键词的段落
            key_paragraphs = self._extract_key_paragraphs(body, question)
            parts.append(key_paragraphs)
        
        return '\n'.join(parts)
    
    def _extract_key_paragraphs(self, text: str, question: str, max_chars: int = 800) -> str:
        """提取与问题相关的关键段落"""
        paragraphs = text.split('\n\n')
        query_tokens = set(self.tokenize(question))
        
        scored_paragraphs = []
        for p in paragraphs:
            if len(p.strip()) < 20:  # 跳过太短的段落
                continue
            p_tokens = set(self.tokenize(p))
            score = len(query_tokens & p_tokens)
            scored_paragraphs.append((p, score))
        
        # 按相关性排序，取前几个
        scored_paragraphs.sort(key=lambda x: x[1], reverse=True)
        
        result = []
        total_len = 0
        for p, score in scored_paragraphs[:3]:
            if total_len + len(p) > max_chars:
                break
            result.append(p.strip())
            total_len += len(p)
        
        return '\n\n'.join(result) if result else paragraphs[0][:max_chars] if paragraphs else ""
    
    def _generate_todos(self, question: str, skill: Dict) -> List[Dict]:
        """生成 TODO 清单"""
        todos = []
        
        # 根据问题类型推断 TODO
        question_lower = question.lower()
        
        # 面试相关问题
        if any(k in question_lower for k in ['面试', '候选人', '招聘', 'interview', 'candidate']):
            todos = [
                {'task': '明确岗位需求和胜任力模型', 'priority': '高', 'time': '面试前 1-2 天'},
                {'task': '设计结构化面试问题（行为面试法）', 'priority': '高', 'time': '面试前 1 天'},
                {'task': '审阅候选人简历，标注疑点', 'priority': '中', 'time': '面试前 30 分钟'},
                {'task': '准备面试评估表', 'priority': '中', 'time': '面试前'},
                {'task': '进行面试，记录关键信息', 'priority': '高', 'time': '面试中'},
                {'task': '填写面试评估，与其他面试官对齐', 'priority': '高', 'time': '面试后 24 小时内'},
                {'task': '进行背景调查（如进入终轮）', 'priority': '中', 'time': '发 offer 前'},
            ]
        
        # 绩效相关问题
        elif any(k in question_lower for k in ['绩效', 'performance', 'review', '评估']):
            todos = [
                {'task': '收集员工绩效数据（产出、项目结果）', 'priority': '高', 'time': '面谈前 1 周'},
                {'task': '准备正面反馈和改进建议', 'priority': '高', 'time': '面谈前 3 天'},
                {'task': '预约一对一会议时间', 'priority': '中', 'time': '面谈前 1 周'},
                {'task': '进行绩效面谈（倾听+反馈）', 'priority': '高', 'time': '面谈中'},
                {'task': '共同制定改进计划或发展目标', 'priority': '高', 'time': '面谈中'},
                {'task': '发送会议纪要和行动计划', 'priority': '中', 'time': '面谈后 24 小时'},
                {'task': '设置检查点，跟进进展', 'priority': '中', 'time': '面谈后 1 个月'},
            ]
        
        # 一对一会议
        elif any(k in question_lower for k in ['一对一', 'one-on-one', '1:1']):
            todos = [
                {'task': '收集近期工作进展和障碍', 'priority': '高', 'time': '会议前'},
                {'task': '准备开放性问题清单', 'priority': '中', 'time': '会议前 15 分钟'},
                {'task': '创建会议议程（员工主导+经理补充）', 'priority': '中', 'time': '会议前'},
                {'task': '专注倾听，做笔记', 'priority': '高', 'time': '会议中'},
                {'task': '识别需要解决的问题', 'priority': '高', 'time': '会议中'},
                {'task': '确定下一步行动和负责人', 'priority': '高', 'time': '会议结束前'},
                {'task': '跟进待办事项完成情况', 'priority': '中', 'time': '下次会议前'},
            ]
        
        # 晋升/职业发展
        elif any(k in question_lower for k in ['晋升', 'promotion', '职业发展', 'career']):
            todos = [
                {'task': '评估员工当前能力 vs 目标职级要求', 'priority': '高', 'time': '晋升讨论前'},
                {'task': '收集 360 度反馈', 'priority': '中', 'time': '晋升讨论前 2 周'},
                {'task': '与员工沟通职业发展意向', 'priority': '高', 'time': '晋升讨论中'},
                {'task': '识别能力差距和发展计划', 'priority': '高', 'time': '晋升讨论中'},
                {'task': '制定具体的成长路径和时间表', 'priority': '高', 'time': '晋升讨论后'},
                {'task': '安排导师或培训资源', 'priority': '中', 'time': '晋升讨论后 1 周'},
                {'task': '定期回顾发展进度', 'priority': '中', 'time': '每季度'},
            ]
        
        # 员工关系/离职
        elif any(k in question_lower for k in ['离职', 'retention', '保留', '辞职']):
            todos = [
                {'task': '安排离职面谈，了解真实原因', 'priority': '高', 'time': '收到离职申请后 24 小时'},
                {'task': '评估挽留的可能性和价值', 'priority': '高', 'time': '离职面谈后'},
                {'task': '如需挽留：准备 counter offer 或改进方案', 'priority': '高', 'time': '2-3 天内'},
                {'task': '启动知识转移和交接计划', 'priority': '高', 'time': '确定离职日期后'},
                {'task': '更新招聘需求和岗位描述', 'priority': '中', 'time': '确认离职后'},
                {'task': '进行团队影响评估和沟通', 'priority': '中', 'time': '适当时候'},
                {'task': '完善员工保留机制（长期）', 'priority': '中', 'time': '持续'},
            ]
        
        # 默认 TODO
        else:
            todos = [
                {'task': '深入理解当前问题的背景和具体情况', 'priority': '高', 'time': '立即'},
                {'task': '收集相关数据和信息', 'priority': '高', 'time': '1-2 天内'},
                {'task': '参考相关的管理 Skills 制定方案', 'priority': '高', 'time': '分析后'},
                {'task': '与相关方沟通并获得反馈', 'priority': '中', 'time': '方案制定后'},
                {'task': '执行计划并跟踪效果', 'priority': '高', 'time': '持续'},
                {'task': '复盘总结经验教训', 'priority': '低', 'time': '事件结束后'},
            ]
        
        return todos
    
    def ask(self, question: str) -> Dict:
        """
        主入口：用户提问，获取回答
        
        Args:
            question: 用户的问题
            
        Returns:
            包含回答和 TODO 的字典
        """
        # 匹配 Skills
        matched = self.match_skills(question, top_k=3)
        
        # 生成回答
        response = self.generate_response(question, matched)
        
        return response


# CLI 交互
if __name__ == "__main__":
    print("🚀 初始化智能 HR 助手...")
    assistant = IntelligentHRAssistant()
    
    print("\n" + "="*60)
    print("👋 欢迎使用智能 HR 助手！")
    print("输入您遇到的管理问题，我会为您匹配合适的 Skills 并给出 TODO 清单。")
    print("输入 'quit' 退出")
    print("="*60 + "\n")
    
    while True:
        question = input("💬 您的问题: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("👋 再见！")
            break
        
        if not question:
            continue
        
        print("\n🤔 正在分析...\n")
        
        response = assistant.ask(question)
        
        # 输出回答
        print("="*60)
        print("📋 回答")
        print("="*60)
        print(response['answer'])
        
        # 输出 TODO
        print("\n" + "="*60)
        print("✅ 建议行动清单 (TODO)")
        print("="*60)
        for i, todo in enumerate(response['todos'], 1):
            priority_emoji = {'高': '🔴', '中': '🟡', '低': '🟢'}.get(todo['priority'], '⚪')
            print(f"\n{i}. {priority_emoji} {todo['task']}")
            print(f"   优先级: {todo['priority']} | 时间: {todo['time']}")
        
        print("\n" + "="*60 + "\n")
