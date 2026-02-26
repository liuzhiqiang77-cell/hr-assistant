# Performance Indicators - Detailed Reference

## Metric Over-Optimization Examples

### Inventory Too Low
- **Metric**: Inventory value
- **Behavior**: Drive inventory to zero
- **Consequence**: Stockouts, lost sales, production stops
- **Counter-metric**: Stockout incidents

### Speed Over Quality
- **Metric**: Project completion date
- **Behavior**: Rush to finish early
- **Consequence**: Bugs, rework, technical debt
- **Counter-metric**: Defect rate at release

### Call Center Efficiency
- **Metric**: Average call duration
- **Behavior**: Rush callers off phone
- **Consequence**: Low satisfaction, repeat calls
- **Counter-metric**: Customer satisfaction score

## Linearity Indicator Visual

```
Output
  ^
  |                                    Target (100)
  |                                   /
  |                              ___/ 
  |                         ___/     
  |                    ___/          
  |               ___/               
  |          ___/                    
  |     ___/                         
  |____/_________________________> Time
    Start                        Deadline
    
    / = Ideal Straight Line
    ___ = Actual (below line, needs acceleration)
```

## Daily Review Template

```
DAILY OPERATIONS REVIEW
Date: _______________

1. SALES FORECAST
   Today's plan: ______
   Yesterday's variance: ______ (plan vs actual)
   Confidence in today's forecast: High/Med/Low

2. INVENTORY STATUS
   Eggs: ______ (Order/Cancel/OK)
   Bread: ______ (Order/Cancel/OK)
   Coffee: ______ (Order/Cancel/OK)

3. EQUIPMENT
   Breakdowns yesterday: Yes/No
   Action needed: _______________

4. MANPOWER
   Staff available: ______ / Required: ______
   Action: _______________

5. QUALITY
   Complaints yesterday: ______
   Staff with issues: _______________

ACTION ITEMS:
1. _______________
2. _______________
3. _______________
```

## Administrative Output Examples

| Department | Physical Output | Quality Measure |
|------------|-----------------|-----------------|
| Payroll | Paychecks processed | Error rate |
| Purchasing | POs issued | On-time delivery % |
| IT Support | Tickets resolved | Customer satisfaction |
| Legal | Contracts reviewed | Risk exposure |
| HR | Employees hired | 90-day retention |