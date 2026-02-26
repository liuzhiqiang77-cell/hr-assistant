# Indicator Design Examples

## Manufacturing

### Primary Indicators
- Units produced
- On-time delivery rate
- First-pass yield

### Paired Indicators
| Primary | Counter | Target |
|---------|---------|--------|
| Production rate | Defect rate | High rate, low defects |
| Inventory level | Stockout rate | Low inventory, no stockouts |
| Machine speed | Downtime | Fast operation, reliable |

## Administrative Functions

### Accounts Payable
- **Output:** Vouchers processed per day
- **Quality:** Errors found per 100 vouchers
- **Target:** 50 vouchers/day, <1% errors

### Human Resources
- **Output:** Positions filled per month
- **Quality:** Retention at 6 months
- **Target:** 10 hires/month, >90% retention

### Customer Service
- **Output:** Calls handled per hour
- **Quality:** Customer satisfaction score
- **Target:** 20 calls/hour, >4.5/5 rating

## Linearity Indicator Examples

### Sales Tracking

| Month | Target | Cumulative Target | Actual | Cumulative Actual | Status |
|-------|--------|-------------------|--------|-------------------|--------|
| Jan | 100 | 100 | 90 | 90 | Below line |
| Feb | 100 | 200 | 110 | 200 | On line |
| Mar | 100 | 300 | 95 | 295 | Below line |
| Apr | 100 | 400 | 130 | 425 | Above line |

**Action Required in March:** Increase rate to 105/month to catch up.

### Production Output

| Week | Target | Actual | Variance |
|------|--------|--------|----------|
| 1 | 500 | 400 | -100 |
| 2 | 500 | 450 | -50 |
| 3 | 500 | 600 | +100 |
| 4 | 500 | 700 | +200 |

**Pattern:** Back-loaded production
**Risk:** Equipment breakdown in week 4 could miss target
**Action:** Smooth production across weeks