---
name: compensation-system-design
description: Design compensation systems for middle and senior managers including performance bonuses and salary administration. Use when creating or reviewing compensation structures, determining bonus percentages and factors, or establishing salary administration schemes.
---

# Compensation System Design

## Part 1: Performance Bonus Design (Variable Pay)

### Determine Bonus Percentage Based on Total Compensation

| Manager Level | Bonus Percentage | Rationale |
|---------------|------------------|-----------|
| Middle Manager | 10% to 25% of total compensation | Higher earners have less material utility for incremental dollars; sufficient for feedback while avoiding hardship from fluctuations |
| Senior Manager | Up to 50% of total compensation | Higher percentage needed for feedback due to base salary saturation |

### Define Bonus Factors (Scope)

1. **Identify performance basis**: Team-based or Individual-based

2. **If Team-based, define the team**:
   - Project team
   - Division
   - Entire Corporation

3. **Recommended 3-Factor Split** (e.g., for 20% total comp):
   - **Individual Performance**: Judged by supervisor
   - **Immediate Team Objective Performance**: Department-level metrics
   - **Overall Corporate Financial Performance**: Company-wide results

### Establish Timing

- Pay bonus close enough to the work time so the subordinate remembers why it was awarded
- Account for cause/effect time offsets

### Select Metrics

| Option Type | Description | Caution |
|-------------|-------------|---------|
| Countable items | Financial metrics | Ensure alignment with goals |
| Measurable objectives | KPI-based targets | Must be clearly defined |
| Subjective elements | Qualitative assessment | May lead to "beauty contest" |

## Part 2: Salary Administration (Base Pay)

### Select Administration Scheme

| Option | Description | Pros/Cons |
|--------|-------------|----------|
| **Option A: Experience-Only** | Pay based strictly on time (X time = Y pay) | Easiest, but ignores merit |
| Option B: Merit-Only | Pay based on performance only | Impractical; hard to ignore experience |
| **Option C: Compromise (Recommended)** | "Family of curves" | Best balance; starts everyone at same level, allows different progression speeds based on performance |

### Implement the "Family of Curves" Approach

1. **Start everyone** at same salary level
2. **Allow different progression**: Individuals move up at different speeds and arrive at different places based on performance
3. **Shape**: Approximates experience-only curve but allows variance for merit

### Competitive Ranking (Required for Merit)

- **Acceptance**: Merit-based systems require competitive, comparative evaluation
- **Principle**: If someone is first, someone else must be last (similar to sports rankings)
- **Implication**: Cannot avoid ranking in a true merit-based system

## Key Constraints

- **Financial Reality**: Do not pay out lavishly if the company is going bankrupt
- **Resource Limits**: Finite money resource requires allocation choices
- **Assessment Difficulty**: Performance is hard to assess precisely for middle managers (not paid by piece, woven into team)

## When to Use This Skill

- Designing compensation systems for middle or senior managers
- Reviewing existing compensation structures
- Determining bonus percentages and factor splits
- Establishing salary administration schemes
- Transitioning from experience-based to merit-based pay

## Variables to Consider

- **total_compensation**: The total annual compensation of the manager
- **bonus_percentage_target**: Target % of total comp allocated to bonus (10-25% for middle, up to 50% for senior)
- **performance_rating**: Supervisor's judgment of individual performance
- **team_metric**: Measurable performance of the immediate team or department
- **corporate_financial_result**: Overall financial performance of the company