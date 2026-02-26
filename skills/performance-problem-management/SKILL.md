---
name: performance-problem-management
description: Handle major performance problems requiring turnaround using the 'Blast' review process, and develop high achievers with future-oriented guidance. Use when dealing with employees at risk of termination, when subordinates are in denial or blaming others, or when developing high performers.
---

# Performance Problem Management

## When to Use This Skill
- A subordinate has a major performance problem requiring turnaround to avoid firing
- A subordinate is stuck in denial or blaming others for performance issues
- A subordinate is a high achiever and needs development guidance
- You need to create a corrective action program or development plan

## The 'Blast' Performance Review Process

### Resistance Cycle Stages

| Stage | Description | Type |
|-------|-------------|------|
| 1 | Ignore | Passive ignoring of the problem |
| 2 | Deny | Active denial of the problem's existence |
| 3 | Blame Others | Admits problem exists but blames others |
| 4 | Assume Responsibility | Admits "It is my problem" |
| 5 | Find Solution | Intellectual step to remedy the situation |

### Facilitating Progression

#### From Ignore to Deny
- Use facts and examples to demonstrate reality

#### From Deny to Blame Others
- Use evidence to overcome resistance

#### From Blame Others to Assume Responsibility (Critical Step)
- **This is an emotional step (hard)**
- Guide subordinate to realize: "If it is my problem, I have to do something about it"
- This implies work and unpleasantness

#### From Assume Responsibility to Find Solution
- **This is an intellectual step (easier)**
- Once responsibility is assumed, finding the solution is a shared task

### Possible Outcomes

| Outcome | Description |
|---------|-------------|
| 1 | Subordinate accepts assessment and recommended cure |
| 2 | Subordinate disagrees with assessment but accepts cure |
| 3 | Subordinate disagrees with assessment and does not commit |

### Fallback Procedure (If Stuck at 'Blame Others')

1. **Assume formal role** as supervisor endowed with position power
2. **State clearly**: "This is what I, as your boss, am instructing you to do."
3. **Acknowledge disagreement**: "I understand that you do not see it my way. You may be right or I may be right."
4. **Assert organizational requirement**: "I am not only empowered, I am required by the organization for which we both work to give you instructions, and this is what I want you to do."
5. **Secure commitment** to the course of action
6. **Monitor performance** against that commitment

### Constraints
- Process cannot proceed to solution-finding if subordinate is stuck in denial or blame stages
- Requires facts and examples to demonstrate reality

## High Achiever Development Strategy

### Common Pitfall
Supervisors often spend effort justifying the judgment of superior performance while giving little attention to how the subordinate could do even better.

### Contrast with Poor Performers
- Poor performers receive detailed "corrective action programs" (step-by-step affairs to meet minimum requirements)
- High achievers often lack future-oriented guidance

### Development Steps

1. **Analyze current review content** for the high achiever
2. **Identify if review is purely retrospective** (analyzing past performance) or focused on justifying a high rating
3. **Shift priority**: Define specific actions the subordinate needs to take to improve performance or maintain their current level
4. **Leverage principle**: High achievers account for a disproportionately large share of work. Improving them is a "high-leverage activity" where the impact on group output is very great.

### Constraints
- Does not apply to poor performers who require corrective action programs

## Variables

- `current_stage` (Enum): Ignore, Deny, Blame Others, Assume Responsibility, Find Solution
- `evidence_available` (Boolean): Whether manager has sufficient facts and examples
- `subordinate_performance_level` (Category): High Achiever, Poor Performer, etc.
- `review_focus` (String): Retrospective (past) or Developmental (future)

## Expected Outcomes
- Subordinate assumes responsibility and commits to a solution, OR
- Subordinate follows direct instructions under position power with performance monitoring
- A performance review for high achievers that includes specific steps for future improvement, not just past justification

## Key Distinction
- **Assuming Responsibility**: Emotional step (hard)
- **Finding Solution**: Intellectual step (easier)