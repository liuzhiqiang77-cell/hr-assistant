# Performance Indicators and Monitoring - Detailed Examples

## Daily Operational Checklist - Breakfast Factory

### Morning Review (8:00 AM)
- [ ] Sales forecast: 150 breakfasts planned
- [ ] Yesterday's variance: +5 (actual 145, planned 140)
- [ ] Egg inventory: 160 eggs (slightly high, cancel today's delivery)
- [ ] Toaster status: Unit #2 broken yesterday, repair scheduled
- [ ] Manpower: 1 waiter sick, reallocate busboy to waiter
- [ ] Complaint log: Waiter #3 had 3 complaints (usual is 1), speak to them

### Immediate Actions Taken
1. Cancel egg delivery (save $15)
2. Rearrange production line around broken toaster
3. Move busboy to waiter position
4. Coach Waiter #3 on customer service

## Paired Indicators by Department

### Accounts Payable
- **Primary**: # Vouchers processed per day
- **Counter**: # Errors found per day
- **Goal**: Maximize vouchers while keeping errors below threshold

### Custodial Services
- **Primary**: # Square feet cleaned per day
- **Counter**: Quality rating (1-10) by senior manager
- **Goal**: Clean maximum area while maintaining quality ≥ 8

### Sales
- **Primary**: # Orders obtained per week
- **Counter**: # Returns or cancellations per week
- **Goal**: Maximize sales while minimizing returns

### Software Development
- **Primary**: # Features delivered per sprint
- **Counter**: # Bugs found in testing per sprint
- **Goal**: Deliver features while maintaining quality

### Manufacturing
- **Primary**: # Units produced per day
- **Counter**: # Defects per thousand units
- **Goal**: Maximize output while minimizing defects

## Black Box Process Examples

### College Recruiting
- **Input**: Applicants on campus
- **Labor**: Interviewers conducting interviews
- **Output**: Graduates accepting job offers
- **Windows**: Interview-to-offer rate, offer acceptance rate

### Field Sales Training
- **Input**: Product specifications, market data
- **Labor**: Marketing trainers conducting sessions
- **Output**: Trained sales personnel ready for field
- **Windows**: Training completion rate, post-training sales performance

### Customer Billing
- **Input**: Purchase info, pricing data, shipment confirmation
- **Labor**: Billing clerks processing invoices
- **Output**: Final bills sent to customers
- **Windows**: Invoices processed per day, error rate, days sales outstanding

## Linearity Indicator Examples

### Recruiting Campaign (6-Month Goal)
- **Target**: 100 hires by June 30
- **Ideal Line**: 16.7 hires per month

**Progress Report (April 15)**:
- Time elapsed: 3.5 months
- Ideal progress: 58 hires
- Actual progress: 40 hires
- **Gap**: 18 hires behind

**Required Rate for Remaining 2.5 Months**:
- Remaining needed: 60 hires
- Required rate: 24 hires/month (vs. 16.7 ideal)
- **Action**: Increase recruiting resources immediately

### Manufacturing Production (Monthly Goal)
- **Target**: 1,000 units for month
- **Ideal Line**: 50 units per day (20-day month)

**Progress Report (Day 15)**:
- Time elapsed: 15 days
- Ideal progress: 750 units
- Actual progress: 300 units
- **Problem**: Production heavily back-loaded

**Analysis**:
- Days 1-10: 50 units total (5/day)
- Days 11-15: 250 units (50/day)
- **Issue**: Manpower/equipment underutilized early in month

**Action**: Rebalance production schedule to spread evenly

## Indicator Design Pitfalls

### Over-Optimization Example
- **Single Metric**: Minimize inventory levels
- **Result**: Inventory driven too low
- **Consequence**: Frequent stockouts, lost sales
- **Solution**: Pair with "Incidence of Shortages" metric

### Activity vs. Output Example
- **Wrong Metric**: # Sales calls made (activity)
- **Right Metric**: # Orders obtained (output)
- **Why**: 100 calls with 0 orders = 0 value; 10 calls with 5 orders = high value

### Non-Countable Metrics to Avoid
- "Effort expended" (subjective)
- "Team morale" (difficult to measure consistently)
- "Customer satisfaction" (unless using specific countable proxy like complaint rate)