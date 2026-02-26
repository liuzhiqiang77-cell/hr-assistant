# Indicator Design and Forecasting Examples

## Paired Indicators Examples

### Inventory Management
- **Primary**: Inventory Level (units on hand)
- **Counter**: Incidence of Shortages (stockouts per month)
- **Purpose**: Prevent driving inventory too low (creates shortages) or too high (waste)

### Project Management
- **Primary**: Completion Date (when project finishes)
- **Counter**: Capability (features/functionality delivered)
- **Purpose**: Prevent rushing (missed features) or perfectionism (missed deadlines)

### Sales Performance
- **Primary**: Sales Volume (revenue or units)
- **Counter**: Customer Satisfaction (complaints or returns)
- **Purpose**: Prevent aggressive selling that damages relationships

### Administrative Work
- **Primary**: Vouchers Processed (count)
- **Counter**: Errors Found (count)
- **Purpose**: Ensure speed doesn't compromise accuracy

## Daily Operations Example

**Breakfast Factory Morning Review**:

1. **Sales Forecast**: 200 breakfasts planned
2. **Variance**: Yesterday planned 180, delivered 175 (97% - good confidence)
3. **Inventory**: 250 eggs (need 200, good), 150 bread slices (need 200, order more)
4. **Equipment**: Toaster working, coffee machine needs repair (call technician)
5. **Manpower**: 3 waiters scheduled, 1 called in sick (move dishwasher to waiter)
6. **Quality**: Waiter B had 5 complaints yesterday (usual is 1-2, speak to Waiter B)

**Actions Taken**:
- Order 50 more bread slices
- Schedule coffee machine repair
- Reassign dishwasher to waiter duty
- Coach Waiter B on customer service

## Linearity Indicator Example

**Recruiting Campaign**:
- **Target**: 100 hires by June
- **Timeline**: January to June (6 months)
- **Ideal Line**: 16.7 hires per month

**Progress Check (April)**:
- **Time Elapsed**: 3 months (50%)
- **Actual Hires**: 30 (30%)
- **Behind Schedule**: 20 hires
- **Required Rate**: 70 hires in 2 months = 35/month (vs. 16.7 ideal)

**Action**: Accelerate recruiting efforts, add resources, or revise target

**Manufacturing Example**:
- **Target**: 1,000 units/month
- **Week 1-3**: 200 units total (very slow)
- **Week 4**: 800 units (rush)

**Problem**: Back-loaded production indicates inefficient resource use
**Action**: Spread production evenly across month to reduce stress and breakdown risk

## Stagger Chart Example

```
              Target Month
Forecast    Aug  Sep  Oct  Nov  Dec  Jan
Month
Jul        100  110  120  130  140  150
Aug             105  115  125  135  145
Sep                  110  120  130  140
Oct                       115  125  135
Nov                            120  130
Dec                                 125
```

**Analysis for December**:
- July forecast: 140
- August forecast: 135
- September forecast: 130
- October forecast: 125
- November forecast: 120
- December forecast: 125

**Trend**: Forecasts declining from July to November, then slight increase in December
**Insight**: Business outlook deteriorated through fall, now stabilizing

## Administrative Forecasting Example

**Accounts Payable Department**:

**Indicators**:
- Vouchers processed per month
- Average processing time per voucher
- Errors per 100 vouchers

**Historical Data**:
- Jan: 1,000 vouchers, 5 staff
- Feb: 1,100 vouchers, 5 staff
- Mar: 1,200 vouchers, 5 staff
- Apr: 1,300 vouchers, 5 staff

**Standard**: 240 vouchers/person/month (from trend)

**May Forecast**: 1,500 vouchers expected

**Headcount Calculation**:
- 1,500 ÷ 240 = 6.25 staff needed
- **Action**: Hire 1 additional staff member

**Without Forecasting** (Parkinson's Law):
- Staff stays at 5 people
- Work expands to fill available time
- Processing time increases, backlog grows
- Productivity declines