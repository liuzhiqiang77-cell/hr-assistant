# Compensation System Formulas and Calculations

## Bonus Calculation Formula

```
Total Bonus = Total Compensation × Bonus Percentage × Performance Score

Where:
- Total Compensation = Base Salary + Target Bonus
- Bonus Percentage = 10-25% (middle manager) or up to 50% (senior manager)
- Performance Score = Factor-weighted average of individual, team, and corporate performance
```

### Example: Middle Manager Compensation

**Inputs**:
- Base Salary: $150,000
- Target Bonus Percentage: 20% of total comp
- Individual Performance Score: 1.2 (exceeds)
- Team Performance Score: 1.0 (meets)
- Corporate Performance Score: 0.9 (misses)

**Step 1: Calculate Total Compensation**
```
Total Compensation = Base Salary / (1 - Bonus Percentage)
Total Compensation = $150,000 / (1 - 0.20) = $187,500
```

**Step 2: Calculate Target Bonus**
```
Target Bonus = Total Compensation × Bonus Percentage
Target Bonus = $187,500 × 0.20 = $37,500
```

**Step 3: Apply Performance Weights**
```
Assume weights: Individual (50%), Team (30%), Corporate (20%)

Weighted Performance Score = 
  (1.2 × 0.50) + 
  (1.0 × 0.30) + 
  (0.9 × 0.20) = 0.6 + 0.3 + 0.18 = 1.08
```

**Step 4: Calculate Actual Bonus**
```
Actual Bonus = Target Bonus × Weighted Performance Score
Actual Bonus = $37,500 × 1.08 = $40,500
```

**Total Payout**: $150,000 + $40,500 = $190,500

---

## Salary Curve Calculation

### "Family of Curves" Approach

Three curves representing different performance trajectories:

| Years of Experience | Low Performer | Average Performer | High Performer |
|---------------------|---------------|-------------------|----------------|
| 0 | $100,000 | $100,000 | $100,000 |
| 1 | $105,000 | $110,000 | $115,000 |
| 2 | $110,000 | $121,000 | $132,250 |
| 3 | $115,500 | $133,100 | $152,088 |
| 5 | $127,600 | $161,051 | $200,944 |
| 10 | $162,889 | $259,374 | $403,876 |

**Growth Rates**:
- Low Performer: ~5% annually
- Average Performer: ~10% annually
- High Performer: ~15% annually

**Advantage**: Starts everyone at same level but diverges based on sustained performance.

---

## Bonus Sensitivity Analysis

### Impact of Bonus Percentage on Motivation

| Bonus % | Total Comp (at $100k base) | 10% Performance Variance | Impact |
|---------|---------------------------|---------------------------|--------|
| 5% | $105,263 | ±$526 | Minimal motivation signal |
| 10% | $111,111 | ±$1,111 | Noticeable but weak |
| 20% | $125,000 | ±$2,500 | Meaningful feedback |
| 30% | $142,857 | ±$4,286 | Strong motivation |
| 50% | $200,000 | ±$10,000 | Very strong feedback |

**Insight**: Lower-paid employees need higher bonus percentages for the same motivational impact.

### High-Earner Diminishing Returns

| Base Salary | 10% Bonus | 25% Bonus | 50% Bonus |
|-------------|-----------|-----------|----------|
| $100,000 | $10,000 | $25,000 | $50,000 |
| $200,000 | $20,000 | $50,000 | $100,000 |
| $500,000 | $50,000 | $125,000 | $250,000 |
| $1,000,000 | $100,000 | $250,000 | $500,000 |

**Insight**: For someone earning $1M, a $50K bonus (5% of total) is negligible. A 50% bonus provides meaningful feedback without causing financial hardship if missed.