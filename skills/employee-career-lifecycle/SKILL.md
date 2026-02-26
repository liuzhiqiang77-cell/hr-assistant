---
name: employee-career-lifecycle
description: Manage employee career progression through promotion cycles and execute employee recycling procedures when promoted employees underperform. Use when evaluating employees for promotion or when a promoted employee performs below average for an extended period.
---

# Employee Career Lifecycle Management

## When to Use This Skill
- Evaluating employees for promotion based on performance ratings
- Managing an employee who was promoted but is now performing below average
- Determining whether to recycle (demote) or terminate an underperforming employee
- Designing career progression policies

## Promotion Performance Cycle Logic

### The Cycle Process

| Phase | Description | Performance Rating |
|-------|-------------|-------------------|
| Initial State | Employee starts at Job 1 performing at 'average' level | Meets requirements |
| Improvement Phase | Employee receives training and motivation, improves performance | Above average / Exceeds requirements |
| Promotion Trigger | Employee 'exceeds the requirements' and is considered 'promotable' | Exceeds requirements |
| Promotion Action | Employee promoted to Job 2 with new challenges | — |
| Performance Reset | Upon entering Job 2, initially performs at 'meets' due to new challenges | Meets requirements |
| Cycle Repetition | With experience, improves to 'exceeds', leads to another promotion | Exceeds requirements |

### Cycle Conclusion
The cycle repeats until the employee:
- Settles at a 'meets requirements' level
- Is no longer promoted (reaching their 'level of incompetence')

### Critical Constraint: The Atrophy Risk
**IF** an employee 'exceeds the requirements' but is **NOT promoted** to greater challenges:

**THEN** they will **'atrophy'** and performance will permanently return to 'meets requirements'.

### Variables
- **performance_rating**: Current assessment ('meets requirements' or 'exceeds requirements')
- **job_level**: Current tier or difficulty of assigned role

### Output Template
**Promote employee to next job level** OR **maintain current level if performance is 'meets requirements'**

## Employee Recycling Procedure

### When to Execute
- Employee has been promoted
- Employee is performing **below average for extended period**
- Employee is 'so much over his head' in the new role
- Employee previously performed well in the prior role

### Step 1: Identification
Recognize that the person has been promoted beyond their current capability.

### Step 2: Choose Recycling Over Termination
**Decision**: 'Recycle' the employee rather than terminate them.

### Step 3: Define Recycling
Put the employee back into the job they did well before the promotion.

### Step 4: Management Accountability
**Management must admit** it was 'at fault for misjudging the employee's readiness' for more responsibility.

### Step 5: Implementation
Take 'forthright and deliberate steps' to place the person in a job they can do.

### Step 6: Support System
Support the employee in the face of likely **'embarrassment'**.

### Step 7: Transparency
Execute the recycling **'openly'** to reduce stigma.

### Step 8: Expected Outcome
- The embarrassment will be **'short-lived'**
- The employee will regain confidence
- Once confidence is regained, the employee becomes an **'excellent candidate for another promotion'** at a later time and is likely to succeed

### Prohibited Action
**DO NOT** force the employee to leave the company.

**Reject the rationalization**: "It is better that we let him go, for his own sake."

### Variables
- **performance_duration**: Time spent performing below average in the new role
- **previous_role_success**: Confirmation that the employee performed well in the prior role

### Output Template
Employee is demoted to previous successful role with management support, retaining them for future success.

## Key Challenges

### Societal Barriers
- Stigma regarding demotion
- Management tendency to view recycling as personal failure

### Success Factors
- Openness and transparency
- Management accountability for misjudgment
- Support through embarrassment
- Recognition that recycling creates future success

## Related Concept
This approach relates to the **Peter Principle** (employees rise to their level of incompetence) but provides a constructive solution rather than acceptance of the principle.
