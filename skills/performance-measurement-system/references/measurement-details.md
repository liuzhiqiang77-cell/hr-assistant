# Detailed Performance Measurement

## Daily Operations Checklist Template

```
Date: ___________

☐ Sales Forecast: _________ units planned
☐ Yesterday's Variance: _________ (actual: _________, planned: _________)
☐ Inventory Status:
   - Eggs: _________ (Order: ☐ Cancel: ☐)
   - Bread: _________ (Order: ☐ Cancel: ☐)
   - Coffee: _________ (Order: ☐ Cancel: ☐)
☐ Equipment Status:
   - Toaster: ☐ OK ☐ Broken (Action: ___________)
   - Coffee Maker: ☐ OK ☐ Broken (Action: ___________)
☐ Manpower:
   - Required: _________  Available: _________
   - Shortage: _________ (Action: ___________)
☐ Quality Complaints:
   - Waiter A: _________ complaints
   - Waiter B: _________ complaints
   - Waiter C: _________ complaints
   - Action Required: ___________
```

## Linearity Indicator Calculations

### Ideal Line Formula

```
Ideal Value at Time T = (Target Value × Time Elapsed) / Total Time
```

### Variance Calculation

```
Variance = Actual Value - Ideal Value
Variance % = (Variance / Ideal Value) × 100%
```

### Required Rate Calculation

```
Required Rate = (Target - Actual) / Remaining Time
```

### Example: Recruiting Campaign

- Target: 100 hires by June
- Current month: April (4 months elapsed, 2 remaining)
- Actual hires: 30
- Ideal at April: (100 × 4/6) = 67
- Variance: 30 - 67 = -37 (behind by 37)
- Required rate: (100 - 30) / 2 = 35 hires/month

## Stagger Chart Template

| Forecast Month | Jan | Feb | Mar | Apr | May | Jun |
|----------------|-----|-----|-----|-----|-----|-----|
| January | 100 | 105 | 110 | 115 | 120 | 125 |
| February | - | 102 | 108 | 112 | 118 | 122 |
| March | - | - | 106 | 110 | 115 | 120 |
| April | - | - | - | 108 | 112 | 118 |
| May | - | - | - | - | 110 | 115 |
| June | - | - | - | - | - | 112 |

### Forecast Accuracy Analysis

```
Forecast Accuracy = 1 - (|Actual - Forecast| / Actual)
```

Track accuracy by:
- Forecast horizon (1-month, 3-month, 6-month)
- Product line
- Region/department

## Paired Indicator Examples

### Manufacturing
| Pair | Metric 1 | Metric 2 | Balance Point |
|------|----------|----------|--------------|
| Inventory | Days on hand | Stockout rate | 5-7 days, <1% stockout |
| Production | Units produced | Defect rate | Max output, <2% defects |
| Schedule | On-time delivery | Cost variance | 95% on-time, ±5% cost |

### Sales
| Pair | Metric 1 | Metric 2 | Balance Point |
|------|----------|----------|--------------|
| Revenue | Sales $ | Discount % | Max revenue, <10% discount |
| Customers | New accounts | Churn rate | Growth, <5% churn |
| Activity | Calls made | Conversion rate | Volume, >20% conversion |

### Administrative
| Pair | Metric 1 | Metric 2 | Balance Point |
|------|----------|----------|--------------|
| Processing | Items processed | Error rate | Speed, <1% errors |
| Response | Response time | Resolution rate | Fast, complete answers |
| HR | Time to fill | Quality of hire | Speed, high performance |

## Indicator Design Pitfalls

1. **Measuring Activity Instead of Output**
   - Bad: Number of calls made
   - Good: Number of orders obtained

2. **Single Metric Focus**
   - Bad: Just inventory levels (leads to shortages)
   - Good: Inventory + shortage rate

3. **Vague Measurements**
   - Bad: "Customer satisfaction"
   - Good: "Complaints per 100 customers"

4. **Leading vs. Lagging Confusion**
   - Lagging: Results after the fact (revenue)
   - Leading: Predictive of future (pipeline)
   - Need both for complete picture

5. **Gaming the System**
   - Example: Measuring "cases closed" leads to quick closures without resolution
   - Solution: Pair with "reopened cases" metric

## Implementation Timeline

### Week 1-2: Baseline
- Identify current metrics
- Establish data collection
- Create initial dashboards

### Week 3-4: Design
- Design paired indicators
- Set targets and thresholds
- Train staff on new metrics

### Month 2: Pilot
- Test new indicators
- Gather feedback
- Adjust as needed

### Month 3: Rollout
- Full implementation
- Regular review cycles
- Continuous improvement