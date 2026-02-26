---
name: compensation-and-career-management
description: Design compensation systems, manage promotion cycles, and handle employee recycling. Use when structuring compensation for managers, evaluating promotions based on performance ratings, or addressing employees promoted beyond their capability.
---

# Compensation and Career Management

Design effective compensation systems, manage promotion cycles based on performance, and execute employee recycling when promotions fail.

## Compensation System Design

### Design Performance Bonus (Variable Pay)

**Step 1: Determine Bonus Percentage Based on Total Compensation**

| Level | Bonus Range | Rationale |
|-------|-------------|-----------|
| Middle Manager | 10-25% of total comp | Higher percentage needed for feedback while avoiding hardship from fluctuations |
| Senior Manager | Up to 50% of total comp | Higher earners have less material utility for incremental dollars |

**Step 2: Define Bonus Factors (Scope)**

- Identify if performance is Team-based or Individual-based
- If Team-based, define the team (Project team, Division, or Entire Corporation)

**Recommended 3-Factor Split (e.g., for 20% total comp):**
1. Individual Performance (judged by supervisor)
2. Immediate Team Objective Performance (e.g., department)
3. Overall Corporate Financial Performance

**Step 3: Establish Timing**
- Pay bonus close enough to work time so subordinate remembers why it was awarded
- Account for cause/effect time offsets

**Step 4: Select Metrics**
- **Options:** Countable items (financial), Measurable objectives, or Subjective elements
- **Caution:** Subjective elements may lead to a "beauty contest"

### Design Salary Administration (Base Pay)

**Select Administration Scheme:**

- **Option A: Experience-Only (Easiest)**
  - Pay based strictly on time (X time = Y pay)
  - Ignores merit

- **Option B: Merit-Only (Impractical)**
  - Hard to ignore experience

- **Option C: Compromise (Recommended)** - "Family of curves"
  - Starts everyone at same salary level
  - Individuals move up at different speeds/arrive at different places based on performance
  - Shape approximates experience-only curve but allows variance

**Implement Competitive Ranking (Required for Merit):**
- Accept that merit-based systems require competitive, comparative evaluation
- **Principle:** If someone is first, someone else must be last (similar to sports rankings)

## Promotion Performance Cycle

### The Cycle Logic

1. **Initial State:** Employee at Job 1 performing at "meets requirements" (average)
2. **Improvement Phase:** With training and motivation, performance improves to "exceeds requirements"
3. **Promotion Trigger:** Once employee "exceeds requirements," they are "promotable" and promoted to Job 2
4. **Performance Reset:** Entering Job 2, employee initially performs at "meets requirements" due to new challenges
5. **Cycle Repetition:** With experience, employee again improves to "exceeds requirements"
6. **Cycle Continuation:** Repeat until employee settles at "meets requirements" and is no longer promoted (reaching "level of incompetence")

### Critical Constraint

**If an employee "exceeds requirements" but is NOT promoted to greater challenges:**
- They will "atrophy"
- Performance will permanently return to "meets requirements"

### Promotion Decision Logic

| Performance Rating | Action |
|-------------------|--------|
| Meets requirements | Maintain current level |
| Exceeds requirements | Evaluate for promotion to next job level |

## Employee Recycling Procedure

### When to Use

**Trigger Condition:** Promoted employee performs below-average for extended time, having been promoted "so much over their head."

### The Recycling Process

1. **Identification:** Recognize person is over their head and performing below average
2. **Solution Selection:** Choose to "recycle" rather than terminate
3. **Definition:** Put employee back in job they did well before promotion
4. **Management Accountability:** Management must admit fault for misjudging readiness
5. **Implementation:** Take "forthright and deliberate steps" to place person in capable job
6. **Support System:** Support employee through likely embarrassment
7. **Transparency:** Execute recycling "openly" to reduce stigma
8. **Expected Outcome:** Embarrassment is "short-lived," employee regains confidence
9. **Future Value:** Once confident, employee becomes "excellent candidate for another promotion"

### Prohibited Action

**Do NOT force the employee to leave the company.**
- Reject rationalization: "It is better that we let him go, for his own sake"

## Constraints

- **Compensation:** Do not pay out lavishly if company is going bankrupt
- **Compensation:** Finite money resource requires allocation choices
- **Promotion:** Does not apply to "noncompetitors" with no motivation to do more
- **Recycling:** Overcome societal stigma regarding demotion
- **Recycling:** Overcome management tendency to view it as personal failure

## Key Variables

| Variable | Type | Description |
|----------|------|-------------|
| `total_compensation` | Currency | Total annual compensation of manager |
| `bonus_percentage_target` | Percentage | Target % of total comp for bonus (10-25% middle, up to 50% senior) |
| `performance_rating` | Score/Subjective | Supervisor's judgment of individual performance |
| `team_metric` | Objective/KPI | Measurable performance of immediate team or department |
| `corporate_financial_result` | Currency/Percentage | Overall financial performance of company |
| `performance_rating` | String | Current assessment ("meets requirements" or "exceeds requirements") |
| `job_level` | Integer | Current tier or difficulty of assigned role |
| `performance_duration` | Duration | Time spent below average in new role |
| `previous_role_success` | Boolean | Confirmation employee performed well in prior role |