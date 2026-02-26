---
name: performance-indicators-design
description: Design and implement effective performance indicators to monitor operations, track progress, and enable data-driven management decisions. Use when establishing measurement systems, creating dashboards, or setting up operational monitoring.
---

# Performance Indicators Design

## When to Use
- Establishing operational monitoring systems
- Creating performance dashboards
- Designing metrics for administrative or production work
- Tracking progress toward goals

## Core Concepts

### Black Box Process Representation
Conceptualize any activity as a "black box" with three components:

1. **Input**: Raw materials, data, or applicants flowing in
2. **Labor**: Work performed by personnel
3. **Output**: Finished result flowing out

"Cut windows" into the box using indicators to observe internal operations and predict future output.

**Examples:**
- Recruiting: Applicants → Interviewers → Hired graduates
- Sales Training: Product specs → Marketing people → Trained salespeople
- Billing: Purchase info → Billing personnel → Final bill

### Indicator Design Principles

**Attention Principle:**
- Indicators direct attention like steering a bicycle
- You will steer where you're looking

**Guard Against Overreaction:**
- Single metrics can lead to extreme behaviors
- Example: Driving inventory too low creates shortages

**Paired Indicators:**
- Always pair effect with counter-effect to maintain balance
- Examples:
  - Inventory Levels ↔ Incidence of Shortages
  - Completion Date ↔ Capability
  - Vouchers Processed ↔ Errors Found
  - Square Feet Cleaned ↔ Quality Rating

**Administrative Indicator Criteria:**
1. Any measurement is better than none
2. Measure **Output** (results), not **Activity** (effort)
3. Measure **Physical/Countable** things (vouchers, square feet, orders, transactions)

### Daily Operational Indicator Set
Review these indicators daily to manage operations:

1. **Sales Forecast**: Planned deliveries for today
2. **Variance**: Yesterday's actual vs. planned deliveries
3. **Raw Material Inventory**: Stock levels (order if low, cancel if high)
4. **Equipment Condition**: Breakdowns from yesterday
5. **Manpower**: Staff availability vs. requirements
6. **Quality Indicator**: Customer complaint log

### Linearity Indicator
Track progress toward deadlines with early warning:

1. Plot actual output against time elapsed
2. Define "Ideal Straight Line" from start to target
3. Compare actual progress vs. ideal line
4. Interpret deviations:
   - Below line: Accelerate performance
   - Back-loaded (end of period): Address resource allocation

## Execution Steps

### For Process Analysis
1. Define the activity as a black box
2. Identify Input, Labor, and Output
3. Determine which internal operations to observe
4. Design indicators to "cut windows" into the process

### For Indicator Design
1. Identify what needs to be measured
2. Apply design principles (output-focused, countable)
3. Create paired indicators to prevent overreaction
4. Establish data collection mechanisms

### For Daily Operations
1. Review sales forecast and variance
2. Check inventory levels and adjust orders
3. Assess equipment and manpower status
4. Monitor quality indicators
5. Take immediate corrective actions

### For Progress Tracking
1. Define target and deadline
2. Establish ideal straight line trajectory
3. Plot actual progress regularly
4. Identify deviations early
5. Take corrective action before deadline

## Key Variables
- `primary_metric`: Main indicator being tracked
- `counter_metric`: Opposing indicator to prevent overreaction
- `output_measure`: Physical count of results
- `quality_measure`: Rating or error count
- `actual_output`: Real-time progress data
- `ideal_line`: Linear reference from start to target