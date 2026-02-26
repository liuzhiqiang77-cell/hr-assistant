---
name: performance-review-scenarios
description: Handle specific performance review scenarios including preventing the potential trap for managers, conducting "blast" reviews for problem employees, and developing high achievers. Use when dealing with managers whose organizations performed poorly, subordinates requiring turnaround to avoid termination, or high performers needing future-oriented development.
---

# Performance Review Scenarios

## When to Use This Skill
- A manager's organization performed poorly but the manager wants a high rating
- A subordinate has a major performance problem requiring turnaround
- A subordinate is a high achiever and needs development guidance
- Conducting detailed evaluations for specific roles

## The Potential Trap Rule

### When to Apply
A manager's organization performs poorly (lost money, missed revenue forecasts, slipped schedules, poor internal measures).

### The Rule
**The performance rating of a manager cannot be higher than the rating accorded to his organization.**

### Execution Steps

**Step 1: Assess Substance over Form**
- Evaluate actual performance and real output
- Ignore "potential" defined as form (knowledge, handling oneself well, looking like a manager)

**Step 2: Apply the Organization Cap**
- Compare the manager's rating to the organization's rating
- Enforce: Manager Rating ≤ Organization Rating

**Step 3: Enforce Consequences**
- If the business unit failed, the manager cannot receive a high rating
- Reject excuses that the organization failed but the manager is "outstanding"

**Step 4: Prevent Negative Signaling**
- Avoid signaling that "acting" like a manager is sufficient
- Reinforce that performing like a manager is the requirement

## The 'Blast' Performance Review Process

### When to Apply
A subordinate has a major performance problem requiring turnaround to avoid firing.

### The 5 Stages of Resistance

1. **Ignore**: Passive ignoring of the problem
2. **Deny**: Active denial of the problem's existence
3. **Blame Others**: Admits problem exists but blames others
4. **Assume Responsibility**: Admits "It is my problem" (emotional step)
5. **Find Solution**: Intellectual step to remedy the situation

### Execution Steps

**Step 1: Identify Current Stage**
Track where the subordinate is in the resistance cycle.

**Step 2: Facilitate Progression**
- Use facts and examples to demonstrate reality (Ignore → Deny)
- Use evidence to overcome resistance (Deny → Blame Others)
- Guide to Assume Responsibility (the critical emotional step)
- Once responsibility is assumed, finding the solution is a shared, easier task

**Step 3: Evaluate Possible Outcomes**
- Outcome 1: Subordinate accepts assessment and recommended cure
- Outcome 2: Subordinate disagrees with assessment but accepts cure
- Outcome 3: Subordinate disagrees and does not commit

**Step 4: Execute Fallback Procedure (If Stuck at 'Blame Others')**
1. Assume formal supervisor role with position power
2. State clearly: "This is what I, as your boss, am instructing you to do."
3. Acknowledge disagreement: "I understand that you do not see it my way. You may be right or I may be right."
4. Assert organizational requirement: "I am not only empowered, I am required by the organization for which we both work to give you instructions, and this is what I want you to do."
5. Secure commitment to the course of action
6. Monitor performance against that commitment

## High Achiever Development Strategy

### When to Apply
A subordinate is identified as a high performer.

### Common Pitfall
Supervisors often spend effort justifying the judgment of superior performance while giving little attention to how the subordinate could do even better.

### Execution Steps

**Step 1: Analyze Current Review Content**
Determine if the review is purely retrospective or focused on justifying a high rating.

**Step 2: Recognize the Contrast**
Poor performers receive detailed "corrective action programs," but high achievers often lack future-oriented guidance.

**Step 3: Shift Priority**
Define specific actions the subordinate needs to take to improve performance or maintain their current level.

**Step 4: Apply Leverage Principle**
High achievers account for a disproportionately large share of work. Improving them is a "high-leverage activity" with great impact on group output.

## Variables
- **manager_rating** (Score/Grade): Proposed performance rating for the individual manager
- **organization_rating** (Score/Grade): Performance rating from organization's output
- **current_stage** (Enum): Ignore, Deny, Blame Others, Assume Responsibility, Find Solution
- **evidence_available** (Boolean): Whether manager has sufficient facts and examples
- **subordinate_performance_level** (Category): High Achiever, Poor Performer, etc.
- **review_focus** (String): Retrospective (past) or Developmental (future)

## Output
- A corrected rating ensuring Manager Rating ≤ Organization Rating
- Subordinate assumes responsibility and commits to a solution, OR follows direct instructions with monitoring
- A performance review with specific steps for future improvement for high achievers