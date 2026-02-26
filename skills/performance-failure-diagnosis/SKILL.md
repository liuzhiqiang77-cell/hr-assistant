---
name: performance-failure-diagnosis
description: Diagnose the root cause of performance failures to determine appropriate managerial intervention. Use when an employee is not performing their job or when deciding between hands-on versus hands-off management for a specific task.
---

# Performance Failure Diagnosis

Diagnose performance failures to identify whether issues stem from capability (can't) or motivation (won't), and determine the appropriate management style based on task-relevant maturity.

## When to Use
- An individual is not performing their job effectively
- You need to decide between hands-on or hands-off management for a specific task
- Performance issues require intervention (training vs motivation)

## Diagnostic Framework

### Step 1: Apply the "Can't vs. Won't" Test

Ask yourself: **If this person's life depended on doing the work, could they do it?**

**If YES (Won't):**
- The person is capable but not motivated
- Use motivation strategies
- Focus on increasing desire to perform well

**If NO (Can't):**
- The person lacks capability
- Use training to build skills
- Focus on increasing individual capability

> **Critical Principle:** These are the only two reasons a person does not do their job. Everything else is secondary.

### Step 2: Assess Task-Relevant Maturity

Evaluate the employee's maturity level **specifically for the task at hand** (not general maturity).

**For Immature Employees:**
- **Action:** Apply hands-on training
- **Critical Constraint:** Do NOT allow "learn by mistakes" approach
- **Reasoning:** The subordinate's tuition is paid by customers—this is wrong

**For Mature Employees:**
- **Action:** Apply delegate approach (hands-off management)
- Allow autonomy within defined parameters

## Decision Flow

```
Performance Issue Detected
       ↓
"Life or Death" Test
       ↓
Can't Do It? → YES → Training (Capability Issue)
       ↓
      NO → Won't Do It → Motivation Strategies
```

```
Task-Specific Maturity Assessment
       ↓
Immature? → YES → Hands-on Training
       ↓
      NO → Mature → Delegate Approach
```

## Key Variables

| Variable | Type | Description |
|----------|------|-------------|
| `life_dependent_capability` | Boolean | Could the person perform if their life depended on it? |
| `task_maturity_level` | Categorical | Employee's skill level for the specific task (Immature vs Mature) |

## Output
- Root cause identification: **Capability** (requires training) or **Motivation** (requires motivational strategies)
- Management style selection: **Hands-on Training** or **Delegate Approach**