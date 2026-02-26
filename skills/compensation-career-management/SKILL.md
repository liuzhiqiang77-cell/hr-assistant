---
name: Compensation and Career Management
description: Design compensation systems with base salary and performance bonuses, manage promotion performance cycles, execute employee recycling procedures for over-promoted staff, and develop strategies for retaining high achievers. Use when designing pay structures, evaluating promotion eligibility, dealing with chronically underperforming promoted employees, or planning talent development.
---

# Compensation and Career Management

## When to Use This Skill
- Designing or reviewing compensation structures for middle or senior managers
- Evaluating employees for promotion eligibility
- Dealing with employees promoted beyond their capability
- Planning career progression and talent development strategies

## Workflow 1: Compensation System Design

### Performance Bonus Design (Variable Pay)

**Determine Bonus Percentage based on Total Compensation:**
- Middle Manager: 10% to 25% of total compensation
- Senior Manager: Up to 50% of total compensation

**Rationale**: Higher earners have less material utility for incremental dollars; higher percentage needed for feedback while avoiding hardship from fluctuations.

**Define Bonus Factors (Scope):**
1. **Individual Performance** (judged by supervisor)
2. **Immediate Team Objective Performance** (e.g., department metrics)
3. **Overall Corporate Financial Performance**

**Recommended 3-Factor Split Example** (for 20% total bonus):
- Individual Performance: ~7-10%
- Team/Department Performance: ~7-10%
- Corporate Performance: ~3-5%

**Establish Timing:**
- Pay bonus close enough to work time so subordinate remembers why it was awarded
- Account for cause/effect time offsets (some results lag)

**Select Metrics:**
- Countable items (financial metrics)
- Measurable objectives (OKRs, KPIs)
- Subjective elements (use with caution—may lead to "beauty contest")

### Salary Administration (Base Pay)

**Select Administration Scheme:**

| Scheme | Approach | Pros | Cons |
|--------|----------|------|------|
| Experience-Only | Pay based strictly on time | Easiest, predictable | Ignores merit, no incentive |
| Merit-Only | Pay based on performance | Strong incentives | Hard to ignore experience |
| **Compromise (Recommended)** | "Family of curves" | Balances both factors | More complex |

**Compromise Implementation:**
- Start everyone at same salary level
- Individuals move up at different speeds based on performance
- Shape approximates experience-only curve but allows variance
- High performers reach higher levels faster

**Competitive Ranking (Required for Merit):**
- Accept that merit-based systems require competitive, comparative evaluation
- **Principle**: If someone is first, someone else must be last (similar to sports rankings)

## Workflow 2: Promotion Performance Cycle

**Purpose**: Align promotion decisions with actual performance ratings and prevent atrophy.

### The Cycle Process

1. **Initial State**: Employee at Job 1, performing at 'average' level = 'meets requirements'
2. **Improvement Phase**: With training and motivation, performance improves to 'above-average' = 'exceeds requirements'
3. **Promotion Trigger**: Once 'exceeds requirements', employee is 'promotable' → promoted to Job 2
4. **Performance Reset**: Upon entering Job 2, employee initially performs at 'meets requirements' (new challenges)
5. **Cycle Repetition**: With experience, employee improves to 'exceeds requirements' → another promotion
6. **Cycle Conclusion**: Cycle repeats until employee settles at 'meets requirements' (reaches 'level of incompetence')

### Critical Constraint
**If an employee 'exceeds requirements' but is NOT promoted**, they will:
- **Atrophy**: Performance permanently returns to 'meets requirements'
- **Result**: Lost potential and demotivation

### Decision Rule

| Performance Rating | Action |
|-------------------|--------|
| 'Exceeds requirements' | Evaluate for promotion immediately |
| 'Meets requirements' | Maintain current level, develop for improvement |
| Below requirements | Training, motivation, or performance improvement plan |

## Workflow 3: Employee Recycling (Demotion) Procedure

**Purpose**: Retain valuable employees who were promoted beyond their capability.

### When to Apply
- Employee has been promoted
- Employee performs below-average for extended time in new role
- Employee performed well in previous role

### The Recycling Process

1. **Identification**: Recognize employee is "so much over their head" they perform below-average
2. **Solution Selection**: Choose to 'recycle' rather than terminate
3. **Definition**: Put employee back into the job they did well before promotion
4. **Management Accountability**: Management admits fault for misjudging employee's readiness
5. **Implementation**: Take 'forthright and deliberate steps' to place person in job they can do
6. **Support System**: Support employee through likely 'embarrassment'
7. **Transparency**: Execute recycling 'openly' to reduce stigma
8. **Expected Outcome**: Embarrassment is 'short-lived', employee regains confidence
9. **Future Value**: Once confidence regained, employee becomes 'excellent candidate for another promotion'

### Prohibited Action
**DO NOT**: Force employee to leave company
**Reject rationalization**: "It is better that we let him go, for his own sake"
**Reality**: Recycling retains talent and organizational knowledge

### Challenges
- **Societal stigma** regarding demotion
- **Management tendency** to view it as personal failure
- **Difficulty level**: High—requires overcoming social stigma

## Key Variables

| Variable | Type | Description |
|----------|------|-------------|
| `total_compensation` | Currency | Annual compensation of manager |
| `bonus_percentage_target` | Percentage | Target % of total comp for bonus (10-25% middle, up to 50% senior) |
| `performance_rating` | Score/Subjective | Supervisor's judgment of individual performance |
| `team_metric` | Objective/KPI | Measurable performance of immediate team/department |
| `corporate_financial_result` | Currency/Percentage | Overall financial performance of company |
| `performance_rating` | String | 'meets requirements' or 'exceeds requirements' |
| `job_level` | Integer | Current tier/difficulty of assigned role |
| `performance_duration` | Duration | Time spent performing below average in new role |
| `previous_role_success` | Boolean | Confirmation of success in prior role |

## Constraints
- Do not pay out lavishly if company is going bankrupt
- Finite money resource requires allocation choices
- Performance is hard to assess precisely for middle managers (not paid by piece, woven into team)
- Does not apply to 'noncompetitors' with no motivation to do more
- Recycling requires overcoming significant social and cultural barriers