---
name: Performance Review Process
description: Execute performance reviews with integrity, handle employee resistance through the blast process, manage review delivery timing, and tailor development strategies for high achievers. Use when conducting scheduled reviews, addressing performance problems requiring turnaround, or developing high-performing employees.
---

# Performance Review Process

## When to Use This Skill
- Conducting scheduled performance review periods
- Subordinate has major performance problem requiring turnaround to avoid firing
- Managing high achievers who need future-focused development
- Planning review delivery and maintaining supervisor authority

## Fundamental Principles

### Core Purpose
The primary goal of any performance review is to **improve the subordinate's performance**. Secondary purposes include:
- Assessing work quality
- Providing feedback
- Justifying raises/rewards
- Discipline
- Direction setting
- Reinforcing culture

**Focus Areas:**
1. **Skill Level**: Identify missing skills and remediation methods
2. **Motivation**: Intensify motivation to move subordinate to higher performance curve

### Integrity of Judgment
- Preserve supervisor authority—never abdicate judgment to subordinates
- Make upfront assessment of performance without subordinate prompting
- If review lacks depth/analysis, insist on rewrite
- System integrity > subordinate's preference to save time

## Core Workflows

### 1. Review Integrity and Delivery Protocols

**Handling Self-Reviews:**
- **DO NOT** ask for self-review if you will simply reformat and return it
- If you rely on subordinate to tell you accomplishments, you appear unaware and they feel cheated
- **Rule**: Make your assessment BEFORE seeing subordinate's input

**Handling Upward Feedback:**
- May ask subordinate to evaluate your performance
- **Constraint**: Clearly state this has only "advisory status"
- **Constraint**: Never pretend you and subordinates are equals

**Delivery Timing:**

| Option | Approach | Risk | Recommendation |
|--------|----------|------|----------------|
| During Discussion | Hand review at start of meeting | Subordinate reads ahead, no time to process | **NOT Recommended** |
| After Discussion | Hand review after meeting | Subordinate finds phrases later, negative reaction | **NOT Recommended** |
| **Before Discussion** | Give review in advance, discuss later | None if done properly | **RECOMMENDED** |

**Recommended Approach**: Ensure subordinate has time to process content before discussion for a "good meeting of minds."

### 2. The 'Blast' Process for Major Performance Problems

**Purpose**: Guide subordinate from denial to action when termination risk exists.

**Resistance Cycle Stages:**
1. **Ignore**: Passive ignoring of the problem
2. **Deny**: Active denial of problem's existence
3. **Blame Others**: Admits problem but blames others
4. **Assume Responsibility**: Admits "It is my problem" ← **Critical emotional step**
5. **Find Solution**: Intellectual step to remedy situation ← Easier once responsibility accepted

**Procedure:**
1. Identify current stage using facts and examples
2. Facilitate progression:
   - Use facts to move from Ignore → Deny
   - Use evidence to move from Deny → Blame Others
   - Guide to **Assume Responsibility** (emotional breakthrough)
   - Collaborate on **Find Solution** (intellectual, easier)
3. Evaluate outcomes:
   - Accepts assessment and cure
   - Disagrees with assessment but accepts cure
   - Disagrees with assessment and does not commit

**Fallback Procedure (If stuck at 'Blame Others'):**
1. Assume formal supervisor role with position power
2. State clearly: "This is what I, as your boss, am instructing you to do."
3. Acknowledge disagreement: "I understand you do not see it my way. You may be right or I may be right."
4. Assert organizational requirement: "I am required by the organization to give you instructions, and this is what I want you to do."
5. Secure commitment
6. Monitor performance against commitment

### 3. High Achiever Development Strategy

**Problem**: Supervisors spend effort justifying high ratings but give little attention to how subordinate could do even better.

**Contrast**:
- Poor performers receive detailed corrective action programs
- High achievers often lack future-oriented guidance

**Procedure:**
1. Analyze current review content
2. Identify if purely retrospective (past-focused) or developmental (future-focused)
3. **Shift priority**: Define specific actions for improvement or maintaining excellence
4. **Rationale**: High achievers account for disproportionately large work share; improving them is "high-leverage activity"

## Constraints
- Blast process cannot proceed to solutions if subordinate is stuck in denial/blame stages
- High achiever strategy does not apply to poor performers requiring corrective action
- Self-reviews must not replace supervisor's independent judgment
- Upward feedback must never have equal status to supervisor's evaluation

## Key Variables
- `current_stage`: Enum [Ignore, Deny, Blame Others, Assume Responsibility, Find Solution]
- `evidence_available`: Boolean - sufficient facts/examples to demonstrate reality
- `review_focus`: String - retrospective vs. developmental
- `subordinate_performance_level`: Category - High Achiever, Average, Poor Performer