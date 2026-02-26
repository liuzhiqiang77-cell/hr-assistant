---
name: performance-review-complex-cases
description: Handle complex performance review scenarios including manager rating constraints and major performance turnaround situations. Use when a manager's organization performed poorly, or when a subordinate requires a "Blast" review to avoid termination.
---

# Performance Review Complex Cases

Handle special scenarios in performance reviews: enforcing organizational performance caps on manager ratings and executing the "Blast" process for major performance problems.

## Case 1: The Potential Trap Rule

### Apply the Organization Cap

**RULE:** The performance rating of a manager cannot be higher than the rating accorded to his organization.

### Assess Substance Over Form

- **Evaluate:** Actual performance and real output
- **Ignore:** "Potential" defined as form (knowledge, handling oneself well, looking like a manager)

### Enforce Consequences for Poor Organizational Performance

**If the business unit:**
- Lost money
- Missed revenue forecasts
- Slipped schedules
- Showed poor internal measures

**Then the manager:**
- **Cannot** receive a high rating
- **Cannot** be rated "outstanding" despite organization failure
- **Must** accept lower rating reflecting organizational reality

### Prevent Negative Signaling

- Avoid signaling that "acting" like a manager is sufficient
- Reinforce that **performing** like a manager is the requirement

## Case 2: The "Blast" Performance Review Process

### When to Use

**Trigger Condition:** A subordinate has a major performance problem requiring turnaround to avoid firing.

### Prerequisites

- Manager possesses facts and examples
- Subordinate is at risk of termination unless performance improves

### The Resistance Cycle

Track and facilitate progression through these stages:

| Stage | Description | Manager's Role |
|-------|-------------|----------------|
| **1. Ignore** | Passive ignoring of problem | Present facts to demonstrate reality |
| **2. Deny** | Active denial of problem's existence | Use evidence to overcome resistance |
| **3. Blame Others** | Admits problem but blames others | Guide to assume responsibility |
| **4. Assume Responsibility** | "It is my problem" (emotional step) | Facilitate this critical transition |
| **5. Find Solution** | Intellectual step to remedy | Shared task, relatively easier |

### Facilitation Process

**Stage 1-3 (Ignore → Deny → Blame Others):**
- Use facts and examples to demonstrate reality
- Present evidence to overcome resistance
- Maintain firm position

**Stage 4 (Assume Responsibility):**
- This is the **biggest step**—an emotional transition
- Subordinate realizes: "If it is my problem, I have to do something about it"
- This implies work and unpleasantness

**Stage 5 (Find Solution):**
- Once responsibility is assumed, finding solution is an intellectual step
- This is a shared task and relatively easier

### Possible Outcomes

1. **Best:** Subordinate accepts assessment AND recommended cure
2. **Acceptable:** Subordinate disagrees with assessment but accepts cure
3. **Failure:** Subordinate disagrees with assessment and does not commit

### Fallback Procedure (Stuck at "Blame Others")

If subordinate refuses to assume responsibility:

1. **Assume formal role:** "I am your boss, endowed with position power"
2. **State clearly:** "This is what I, as your boss, am instructing you to do"
3. **Acknowledge disagreement:** "I understand you do not see it my way. You may be right or I may be right"
4. **Assert organizational requirement:** "I am not only empowered, I am required by the organization for which we both work to give you instructions, and this is what I want you to do"
5. **Secure commitment:** Obtain subordinate's commitment to the course of action
6. **Monitor performance:** Track performance against that commitment

### Key Distinction

- **Assuming Responsibility:** Emotional step (hard)
- **Finding Solution:** Intellectual step (easier)

## Key Variables

| Variable | Type | Description |
|----------|------|-------------|
| `manager_rating` | Score/Grade | Proposed performance rating for individual manager |
| `organization_rating` | Score/Grade | Rating derived from organization's output |
| `current_stage` | Enum | Current stage: Ignore, Deny, Blame Others, Assume Responsibility, Find Solution |
| `evidence_available` | Boolean | Whether manager has sufficient facts and examples |

## Constraints

- **Potential Trap:** Does not apply if organization failed due to external factors beyond manager's control (though strict adherence is implied)
- **Blast Process:** Cannot proceed to solution-finding if subordinate is stuck in denial or blame stages