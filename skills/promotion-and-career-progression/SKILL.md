---
name: promotion-and-career-progression
description: Manage employee promotions based on performance cycles and execute employee recycling when promoted employees struggle. Use when evaluating employees for promotion, when promoted employees perform below average, or when managing career progression.
---

# Promotion and Career Progression

## When to Use This Skill
- An employee's performance rating is "exceeds requirements"
- A promoted employee is performing below average for an extended period
- You need to evaluate promotion eligibility
- You need to handle a demotion/recycling situation

## Promotion Performance Cycle Logic

### The Performance Cycle

1. **Initial State**: Employee starts at Job 1 performing at "average" level ("meets requirements")

2. **Improvement Phase**: With training and motivation, performance improves to "above-average" ("exceeds requirements")

3. **Promotion Trigger**: Once employee "exceeds requirements", they are considered "promotable" and promoted to Job 2

4. **Performance Reset**: Upon entering Job 2, employee initially performs at "meets requirements" due to new challenges

5. **Cycle Repetition**: With experience, employee improves to "exceeds requirements", leading to another promotion

6. **Cycle Conclusion**: Cycle repeats until employee settles at "meets requirements" and is no longer promoted (reaching their "level of incompetence")

### Critical Constraint
**If an employee "exceeds the requirements" but is NOT promoted to greater challenges, they will "atrophy" and performance will permanently return to "meets requirements."**

### Decision Rule

| Performance Rating | Action |
|-------------------|--------|
| Meets requirements | Maintain current level |
| Exceeds requirements | Evaluate for promotion |

### Constraints
- Does not apply to "noncompetitors" who have no motivation to do more

## Employee Recycling Procedure

### When to Apply
- Employee has been promoted
- Employee is performing below average for extended period
- Employee has been promoted "so much over his head" that they cannot succeed

### Recycling Steps

1. **Identification**: Recognize that the person is over their head in the current role

2. **Solution Selection**: Choose to "recycle" the employee rather than terminate them

3. **Definition of Recycling**: Put the employee back into the job they did well before the promotion

4. **Management Accountability**: Management must admit it was "at fault for misjudging the employee's readiness"

5. **Implementation**: Take "forthright and deliberate steps" to place the person in a job they can do

6. **Support System**: Support the employee in the face of likely "embarrassment"

7. **Transparency**: Execute the recycling "openly" to reduce stigma

8. **Expected Outcome**: Embarrassment will be "short-lived" and employee will regain confidence

9. **Future Value**: Once confidence is regained, employee becomes an "excellent candidate for another promotion" and is likely to succeed

### Prohibited Action
**Do NOT force the employee to leave the company.**

Reject the rationalization: "It is better that we let him go, for his own sake."

### Challenges
- Societal stigma regarding demotion
- Management tendency to view it as personal failure

## Variables

- `performance_rating` (String): "meets requirements" or "exceeds requirements"
- `job_level` (Integer): Current tier or difficulty of assigned role
- `performance_duration` (Duration): Time spent performing below average in new role
- `previous_role_success` (Boolean): Confirmation that employee performed well in prior role

## Expected Outcomes
- Promotion to next job level when performance exceeds requirements
- Employee is demoted to previous successful role with management support, retaining them for future success
- Prevention of performance atrophy through timely promotions

## Related Concept
Peter Principle: Employees rise to their "level of incompetence" where they can no longer perform effectively.