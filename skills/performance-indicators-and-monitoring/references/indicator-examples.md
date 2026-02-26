# Detailed Indicator Examples and Templates

## Paired Indicator Examples

### Manufacturing
| Primary Metric | Counter Metric | Optimal Range |
|----------------|----------------|---------------|
| Inventory Level | Incidence of Shortages | Balance both |
| Production Rate | Defect Rate | Maximize rate, minimize defects |
| Machine Uptime | Maintenance Cost | High uptime, reasonable cost |

### Administrative Functions
| Function | Output Measure | Quality Measure |
|----------|----------------|----------------|
| Accounts Payable | # Vouchers processed | # Errors found |
| Accounts Receivable | # Invoices sent | % Past due |
| Payroll | # Paychecks issued | # Corrections needed |
| Purchasing | # Purchase orders | % Emergency orders |

### Customer Service
| Primary Metric | Counter Metric |
|----------------|----------------|
| Calls answered per hour | Average call duration |
| Issues resolved | Customer satisfaction score |
| Response time | First-contact resolution rate |

### Software Development
| Primary Metric | Counter Metric |
|----------------|----------------|
| Features delivered | Bugs reported |
| Code commits | Test coverage % |
| Deployment frequency | Rollback frequency |

## Linearity Indicator Examples

### Recruiting Campaign

**Target**: 100 hires by June
**Current Date**: April (4 months elapsed, 2 months remaining)

| Month | Cumulative Hires | Ideal Line | Status |
|-------|------------------|------------|--------|
| Jan | 15 | 16.7 | Slightly behind |
| Feb | 30 | 33.3 | Behind |
| Mar | 45 | 50.0 | Behind |
| Apr | 55 | 66.7 | **Behind - Action needed** |

**Analysis**: At 55 hires in April, need 45 more in 2 months (22.5/month) vs. original pace of 16.7/month.

**Action**: Accelerate recruiting efforts, add resources, or adjust target.

### Manufacturing Production

**Target**: 10,000 units per month

| Week | Units Produced | Ideal Line | Status |
|------|----------------|------------|--------|
| 1 | 1,500 | 2,500 | Behind |
| 2 | 3,000 | 5,000 | Behind |
| 3 | 4,000 | 7,500 | Behind |
| 4 | 6,500 | 10,000 | **Back-loaded** |

**Analysis**: 65% of production in final week indicates inefficient resource use.

**Action**: Smooth production across weeks or investigate bottleneck.

## Stagger Chart Template

### Monthly Sales Forecast Stagger Chart

| Forecast Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug |
|----------------|-----|-----|-----|-----|-----|-----|-----|-----|
| Jan | 100 | 105 | 110 | 115 | 120 | 125 | 130 | 135 |
| Feb | - | 102 | 108 | 112 | 118 | 122 | 128 | 132 |
| Mar | - | - | 106 | 110 | 116 | 120 | 126 | 130 |
| Apr | - | - | - | 108 | 114 | 119 | 124 | 128 |
| May | - | - | - | - | 112 | 117 | 122 | 126 |
| Jun | - | - | - | - | - | 115 | 120 | 124 |

### Analysis

**August Forecast Evolution**:
- January forecast: 135
- February forecast: 132
- March forecast: 130
- April forecast: 128
- May forecast: 126
- June forecast: 124

**Interpretation**: Business outlook is deteriorating. Each revision lowers expectations.

**Action**: Investigate market changes, adjust production plans, communicate revised expectations.

## Daily Operational Review Checklist

### Morning Review Template

- [ ] Sales forecast for today: _______
- [ ] Yesterday's variance: _______ (Plan vs Actual)
- [ ] Raw material inventory:
  - [ ] Eggs: _______ (Order: Yes/No)
  - [ ] Bread: _______ (Cancel delivery: Yes/No)
  - [ ] Coffee: _______ (Order: Yes/No)
- [ ] Equipment status:
  - [ ] Toaster: _______ (Repair needed: Yes/No)
  - [ ] Coffee pot: _______ (Repair needed: Yes/No)
- [ ] Manpower:
  - [ ] Waiters scheduled: _______ (Need temps: Yes/No)
  - [ ] Kitchen staff: _______ (Reallocate: Yes/No)
- [ ] Quality complaints:
  - [ ] Total yesterday: _______
  - [ ] Staff with >3 complaints: _______ (Action taken: _______)

### Corrective Action Log

| Indicator | Issue | Action Taken | Owner | Due Date |
|-----------|-------|--------------|-------|----------|
| Inventory | Eggs below minimum | Order emergency delivery | Purchasing | Today |
| Equipment | Toaster broken | Arrange rental | Maintenance | Tomorrow |
| Manpower | 2 waiters sick | Call temp agency | Manager | Today |
| Quality | Waiter A - 5 complaints | Coaching session | Supervisor | Today |