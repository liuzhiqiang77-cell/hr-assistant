---
name: employee-performance-diagnosis
description: Use when an employee is underperforming, when performance issues arise, or when determining whether training or motivation interventions are needed.
---

# Employee Performance Diagnosis

## When to Use
- Observing underperformance
- Employee not performing job duties
- Determining appropriate intervention for performance issues
- Diagnosing root cause of performance problems

## Diagnostic Framework

### Step 1: Identify the Issue

Observe and confirm that the employee is not doing their job.

### Step 2: Determine Root Cause

Categorize the performance issue into one of two buckets:

**Can't do it:**
- Employee lacks the capability
- This is a **Training** issue

**Won't do it:**
- Employee lacks the motivation
- This is a **Motivation** issue

### Step 3: Select Intervention

Based on the diagnosis:

| Root Cause | Intervention |
|------------|--------------|
| Can't do (Capability) | Train the employee |
| Won't do (Motivation) | Motivate the employee |

## Key Constraint

**Critical limitation:** There is nothing else a manager can do to improve output other than motivate and train.

## Decision Logic

```
IF employee not performing →
  Determine: Can't do OR Won't do? →
    Can't do → TRAIN
    Won't do → MOTIVATE
```