---
name: Adaptive Leadership and Training
description: Adjust management style based on employee task-relevant maturity, design and deliver high-leverage manager-led training, and calculate organizational training volume requirements. Use when deciding between hands-on and hands-off management, when subordinates lack skills, for new employee onboarding, or when introducing new skills to the organization.
---

# Adaptive Leadership and Training

## When to Use This Skill
- Deciding whether to use hands-on or hands-off management for a specific task
- Subordinates lack specific skills or capability
- New employees join the organization
- Introducing new principles, methods, or skills to existing staff
- Assessing training resource requirements and ROI

## Core Principle
A manager's output is **the output of their organization—no more, no less**. To increase individual performance, use two principal means:
1. Increasing motivation (desire to do the job well)
2. Increasing individual capability (via training)

**Critical**: Just as motivation cannot be fully delegated, neither should training be delegated solely to specialists.

## Workflow 1: Task-Relevant Maturity Management

**Purpose**: Distinguish the top 5% of managers who think deeply about their craft from the 95% who do not.

**Procedure:**
1. Assess employee's maturity level **specifically for the task at hand** (Task-Relevant Maturity)
2. Determine management style based on assessment:

| Employee Maturity | Management Style | Critical Constraint |
|-------------------|------------------|-------------------|
| **Immature** in task | Hands-on training | Do NOT allow employee to 'make their own mistakes' to learn |
| **More Mature** in task | Delegate approach (hands-off) | Provide autonomy, supervise outcomes |

**Critical Constraint for Immature Employees:**
- The problem with 'learn by mistakes': "The subordinate's tuition is paid by his customers. And that is absolutely wrong."
- Employees learning through mistakes harm customers and the business

**Decision Template:**
- `employee_maturity`: Categorical [Immature, Mature]
- `management_style`: Action [Hands-on Training, Delegate Approach]

## Workflow 2: High-Leverage Training Design and Delivery

**Purpose**: Maximize organizational output through efficient, manager-led training.

### Trainer Assignment
- **Who trains**: The manager (you) must instruct direct subordinates and next few ranks below
- **Rationale**: Training must be performed by a "suitable role model" who is a "believable, practicing authority"
- **Constraint**: Proxies cannot effectively fill this role, regardless of subject matter expertise

### ROI Calculation Example

**Preparation**: Allocate 3 hours of preparation for every 1 hour of course time

**Scenario:**
- Course: 4 lectures (4 hours)
- Manager time: 12 hours preparation
- Students: 10
- Student annual work: 20,000 hours total
- Performance improvement: 1%

**Result**: 200 hours of work gained (1% of 20,000) for 12-hour investment
**ROI**: 16.7x return on manager's time

### Cultural Alignment
- Avoid 'highly structured and academic' approaches if they contradict company practices
- **Example**: If company uses 'free market' job applications, do not teach 'carefully coordinated rotations' or long-term career plans
- **Warning**: Mismatch between teaching and practice demoralizes participants

### Consistency Requirements
- Training must be a **process, not an event**
- Provide 'reliable, consistent presence' that is 'systematic and scheduled'
- Do NOT use training as 'rescue effort summoned to solve the problem of the moment'

**Training Failure Risks:**
- Untrained employees miss specific conditions (e.g., 'out-of-tune' machinery)
- Consequences: inefficiencies, excess costs, unhappy customers, danger
- **Example**: Untrained operator caused >$1M in scrapped material and delivery slips

## Workflow 3: Training Volume and Resource Assessment

### Curriculum Scope Benchmark
- Maintain catalogue of courses (e.g., 50+ classes)
- Range: Basic skills (telephone manners) to complex technical (ion implanter: ~200 hours)
- Include management disciplines (strategic planning, constructive confrontation, performance reviews, productive meetings)
- Allocate **2-4% of employee time** to classroom learning

### Training Classification

**Task 1: New Member Training**
- Teaching new members skills needed for their jobs
- **Formula**: `Annual Training Load (%) = Annual Turnover Rate (%) + Annual Growth Rate (%)`
- **Example**: 10% turnover + 10% growth = 20% of staff need basic training annually

**Task 2: New Skills Training**
- Teaching new ideas, principles, or skills to present members
- **Target**: 100% of the staff
- **Comparison Formula**: `Task 2 Magnitude = 100% / Task 1 Load`
- **Example**: If Task 1 is 20%, Task 2 is 5x larger (100% / 20%)

### Cost and Feasibility Decision
- Calculate cost based on student time
- **Benchmark**: One-day course for middle-management staff can cost >$1,000,000 in student time alone
- **Decision Rule**: Do not enter Task 2 (training all staff) lightly due to high magnitude and cost

## Key Variables

| Variable | Type | Description |
|----------|------|-------------|
| `prep_ratio` | Numeric | Hours of preparation per hour of course time (standard: 3) |
| `total_student_hours` | Numeric | Total annual work hours of trained group |
| `performance_improvement` | Percentage | Efficiency gain from training (e.g., 1%) |
| `annual_turnover_rate` | Percentage | Staff leaving organization annually |
| `annual_growth_rate` | Percentage | Organization growth rate annually |
| `task_1_load` | Percentage | Staff requiring basic training (Turnover + Growth) |
| `task_2_magnitude` | Multiplier | Factor by which training all staff exceeds training new staff |

## Constraints
- Do not use 'learn by mistakes' approach for immature employees
- Training content must align with company culture
- Training must not be a one-time 'rescue effort'
- Proxies cannot assume the role of teacher
- Training must be tied to practice
- Training must be a continuing process