# Tannico E-commerce | Peak Season Strategic Performance
**Cart Abandonment Campaign: leveraging A/B Testing & Exploratory Data Analysis for Revenue Recovery**


## Executive Summary

This project identifies and recovers **$2,376 in net revenue** from high-intent abandoned cart sessions through a data-driven free shipping intervention strategy.

The analysis focuses on the **Peak Season period (November 1, 2020 – December 31, 2020)**, evaluating the impact of the **Q4 Holiday Season** on e-commerce performance.

### Key Results

| Metric | Value |
|--------|-------|
| **Cart Abandonment Identified** | 92.6% |
| **Optimal Shipping Threshold** | $50 (down from $70) |
| **Revenue Recovery Potential** | $2,376 net gain |
| **Target Sessions Converted** | 41 out of 64 (64.1%) |
| **ROI** | 375% ($500 investment) |
| **Primary Market** | Italy (49.8% of recoverable revenue) |

---
## Interactive Dashboard (Tableau Public)
The analysis is supported by an interactive dashboard for executive and operational monitoring.

[![Tannico Dashboard Preview](images/dashboard_1.png)](https://public.tableau.com/shared/WGRQ467XM?:display_count=n&:origin=viz_share_link:showVizHome=no)

*Click the image above to explore the interactive visualizations and the implementation checklist.*

---
## Project Overview

### Business Challenge

Out of $18,468 in total lost revenue, we identified critical sessions abandoned specifically due to shipping friction. Traditional recovery methods were failing to convert this high-intent segment.

## Strategic Objective
Design a targeted cart recovery campaign using the optimal free shipping threshold to maximize net revenue recovery while minimizing incentive costs.

## Approach

1. Anomaly Detection: Isolated high-intent churn sessions (target anomaly cohort)
2. Exploratory Data Analysis (EDA): Geographic, device, and product segmentation
3. A/B Test Simulation: Validated $50 threshold effectiveness
4. Campaign Execution Roadmap: Phased rollout prioritization


## Dataset Transformation

### From Generic to Context-Specific

The original Google Merchandise Store data underwent comprehensive transformation to create a realistic Italian wine e-commerce environment:

#### **1. Contextual Mapping**
- **2.6M raw events** re-categorized into wine product taxonomy
- Product categories: Red Wines, White & Rosé, Sparkling, Accessories, Gift Boxes, Gourmet Products
- Behavioral patterns aligned with wine purchasing behavior

#### **2. Geographic Localization**
- **Italy-centric distribution**: 45% of total traffic
- Realistic European market representation (UK, France, Germany, Spain)
- Geographic weighting based on actual wine e-commerce patterns

#### **3. Session Engineering**
- Event-level data aggregated into **43,772 unique user sessions**
- Engineered features:
  - `avg_session_value`: Average cart value per session
  - `cart_value`: Final cart value before checkout
  - `device_category`: Desktop, Mobile, Tablet
  - `transaction_revenue_usd`: Actual converted revenue
  - `session_original_revenue`: Protected revenue field for A/B testing

#### **4. Tableau-Ready Export**
- Clean, structured dataset: `tannico_sessions.csv`
- Optimized dimensions for BI visualization
- Consistent geography, device, and category hierarchies

---

## Methodology

### Phase 1: Data Quality & Exploration

**Inspection & Quality Check**
- Data profiling and distribution analysis
- Outlier detection and handling
- Geographic and temporal pattern identification

**Cleaning & Validation**
- Missing value imputation strategies
- Data type consistency enforcement
- Revenue field validation and protection

### Phase 2: Anomaly Injection & Simulation

**Strategic Anomaly Design**
- Identified high-intent sessions (cart value $50-$70)
- Simulated shipping friction by zeroing `transaction_revenue_usd`
- Preserved original revenue in `session_original_revenue` for validation

**A/B Test Simulation**
- **Control Group (A)**: Current $70 threshold → 0% conversion
- **Treatment Groups (B)**: Alternative thresholds ($40, $50, $60)
- Statistical validation of conversion lift

**Optimization Results**

| Threshold | Sessions Recovered | Gross Revenue | Net Revenue | Winner |
|-----------|-------------------|---------------|-------------|--------|
| **$50** | **64** | **$3,723** | **$2,376** | ✅ **OPTIMAL** |
| $60 | 0 | $0 | $0 | ❌ |
| $40 | 64 | $3,723 | $2,023 | ⚠️ Over-incentivized |

### Phase 3: Geographic & Behavioral Analysis

**Italy-First Strategy Discovery**
- **Sensitivity Gap Analysis**: Italian customers show 49.8% representation in churned carts vs. 45% overall traffic
- **Device Patterns**: Desktop users in Italy represent 26.6% of recoverable revenue
- **Category Insights**: Red Wines dominate abandoned high-value carts

**Segmentation Matrix**

| Priority | Market | Device | Sessions | Net Revenue | % of Total Recovery |
|----------|--------|--------|----------|-------------|---------------------|
| 🔴 **HIGH** | Italy | Desktop | 17 | $793 | 33.4% |
| 🟡 **MEDIUM** | UK, FR, DE | Mobile | 16 | $342 | 14.4% |
| 🟢 **LOW** | Others | All | 31 | $1,241 | 52.2% |

---

## Technologies Used

### Core Analytics Stack
- **Python 3.8+**: Primary analysis language
- **Pandas**: Data manipulation and aggregation
- **NumPy**: Numerical computing
- **Jupyter Notebook**: Interactive development environment

### Visualization & BI
- **Tableau**: Strategic performance dashboard
- **Matplotlib & Seaborn**: Exploratory data visualization
- **Plotly**: Interactive charts (funnel analysis)

### Statistical Methods
- **A/B Testing**: Conversion rate optimization
- **Revenue Modeling**: ROI simulation
- **Cohort Analysis**: Geographic and device segmentation

---
## Key Insights & Findings

### 1. The Shipping Barrier Problem

**Finding**: The $70 free shipping threshold creates a psychological barrier that results in 92.6% abandonment in the critical $50-$70 cart value range.

**Evidence**:
- 64 high-intent sessions identified with cart values between $50-$70
- 0% conversion rate in control group (current $70 threshold)
- Average cart value of abandoned sessions: $58.17

### 2. The Optimal Intervention Point

**Finding**: $50 is the mathematically optimal threshold, balancing conversion recovery and shipping cost investment.

**Validation**:
- **$50 threshold**: Recovers 64 sessions, $2,376 net gain
- **$60 threshold**: Recovers 0 sessions (still above cart values)
- **$40 threshold**: Over-incentivizes, reducing net margin

### 3. The Italy Opportunity

**Finding**: Italian customers are disproportionately sensitive to shipping costs, representing the highest-density recovery opportunity.

**Strategic Implication**:
- Italy = 45% of total traffic but 49.8% of recoverable revenue
- **Italy Desktop segment alone** = 33.4% of total recovery potential
- Justifies market-specific, phased rollout approach

### 4. Device-Specific Behavior

**Finding**: Desktop users in Italy show higher cart values and stronger recovery potential than mobile users.

**Actionable Insight**:
- Phase 1 should target Desktop (higher ARPU)
- Phase 2 should optimize mobile experience separately
- Different messaging strategies needed per device type

---

## Implementation Roadmap

### **PHASE 1: HIGH IMPACT** (Months 1-2)
**Italy - Desktop | IMMEDIATE ACTION**

**Target**: 17 sessions (26.6% of recoverable cohort)  
**Revenue Opportunity**: $1,277 gross | $793 net gain  
**Focus Categories**: Red Wines (13 sessions, $737) + White & Rosé (11 sessions, $603)

**Actions**:
1. Launch cart recovery email campaign with $50 free shipping offer
2. Implement exit-intent pop-up on desktop checkout pages
3. A/B test offer messaging (urgency vs. value-focused)
4. Monitor conversion rate daily for first 2 weeks

**Success Metrics**:
- Target conversion rate: 65% (41 of 64 sessions)
- Break-even point: 9 conversions
- Expected timeframe: 30-45 days

---

### **PHASE 2: STRATEGIC ROLLOUT** (Month 3)
**UK, France, Germany - Mobile | PHASED APPROACH**

**Target**: 5-6 sessions per country (~16 sessions total, 25% of cohort)  
**Revenue Opportunity**: $536 gross | $342 net gain  
**Device Focus**: Mobile-only optimization

**Actions**:
1. Adapt messaging for mobile-first experience
2. Test simplified checkout flow with embedded shipping offer
3. Monitor desktop vs. mobile conversion differential
4. Localize messaging per market (language, cultural nuances)

**Success Metrics**:
- Mobile conversion rate target: 60%
- Cross-device behavior tracking
- Market-specific performance benchmarks

---

### **PHASE 3: TACTICAL MONITORING** (Months 4-6)
**Remaining Markets - Automated | LOW PRIORITY**

**Target**: 30+ sessions (47% of cohort, dispersed across 15+ countries)  
**Revenue Opportunity**: $1,910 gross | $1,241 net gain  
**Approach**: Automated recovery, no significant ad spend

**Actions**:
1. Deploy Klaviyo/Mailchimp automated email sequences
2. Standard abandoned cart series (3-email sequence)
3. No paid media allocation
4. Passive monitoring only

**Success Metrics**:
- Automated recovery rate: 40-50%
- Cost per recovery: <$5
- ROI threshold: >200%

---

## Tableau Dashboard Features

### Interactive Performance Monitoring

The Tableau dashboard (`tannico_recovery_50_threshold.twbx`) provides real-time monitoring capabilities:

#### **1. Strategy Simulation Panel**
- **Adjustable Parameters**: 
  - Success Rate (conversion assumption)
  - Campaign Cost (budget allocation)
  - Offer Threshold (shipping limit)
  - Country Filter (market selection)
- **Live ROI Calculation**: Updates automatically based on parameter changes
- **Break-even Analysis**: Shows minimum conversions needed for profitability

#### **2. Geographic Priority Map**
- **Heat Map Visualization**: Density of recoverable sessions by country
- **Bubble Chart**: Sessions vs. Average Revenue per market
- **Priority Segmentation**: Visual classification (High/Medium/Low)

#### **3. Revenue & Churn Profile**
- **Distribution Analysis**: Session revenue histogram with $50 threshold marker
- **Abandonment Patterns**: Visual identification of the $50-$70 "danger zone"
- **Category Breakdown**: Product mix of high-intent abandoned carts

#### **4. Recovery Segments Detail**
- **Scatter Plot Matrix**: Sessions vs. Revenue by segment
- **Strategic Role Classification**:
  - Volume Foundation (high sessions, moderate revenue)
  - Volume Co-Driver (balanced sessions/revenue)
  - Margin Maximizer (low sessions, high revenue)
  - Basket Builder (accessory/add-on opportunities)

#### **5. Strategic & Operational Deployment**
This section transitions from data analysis to execution, providing both a high-level roadmap and the tactical tools needed for the rollout.
- **Implementation Roadmap (Timeline View)**: A 3-phase execution strategy prioritizing segments by ROI.

- **Target Metrics**: Precise forecasting of recoverable sessions, revenue, and net gain for each phase of the investment.

- **Granular Execution Checklist (Tabular View)**: A detailed operational table (detailed in Tableau Tab 2) that ranks the 64 recoverable sessions by priority.

  - **Actionable Data**: Includes specific Country-Device-Category combinations for surgical targeting.

  - **Financial Traceability**: Real-time visibility of Gross Opportunity and Estimated Net Gain per session to monitor the 375.2% ROI rollout.

---

## Learning Outcomes & Skills Demonstrated

### Data Engineering
- ✅ Event-to-session aggregation at scale (2.6M → 43K records)
- ✅ Domain-specific data transformation and mapping
- ✅ Feature engineering for behavioral analysis
- ✅ Data quality assurance and validation protocols

### Analytical Methods
- ✅ A/B test design and simulation
- ✅ Revenue modeling and ROI calculation
- ✅ Cohort segmentation and prioritization
- ✅ Funnel analysis and churn detection

### Business Intelligence
- ✅ Tableau dashboard development
- ✅ Interactive parameter controls for scenario planning
- ✅ Stakeholder-ready visualization design
- ✅ KPI definition and tracking framework

### Strategic Thinking
- ✅ Phased implementation planning
- ✅ Risk-weighted decision making
- ✅ Market prioritization based on data density
- ✅ Cross-functional communication (technical → business)

---

## Critical Insights for Stakeholders

### Why This Analysis Matters

**Traditional Approach**: Apply uniform free shipping threshold across all markets and hope for improvement.

**Data-Driven Approach**: 
1. Identify the exact cart value range causing friction ($50-$70)
2. Quantify the recovery opportunity with precision ($2,376)
3. Prioritize by geographic sensitivity (Italy = 50% of opportunity)
4. Phase implementation to minimize risk and maximize learning

**Result**: 375% ROI with clear execution roadmap instead of guesswork.

---

## Author

**Sara Magni**  
*Data Analyst*

[sara.m4gn1.data@gmail.com](mailto:sara.m4gn1.data@gmail.com) | [LinkedIn](https://www.linkedin.com/in/sara-m4gn1/) | [GitHub](https://github.com/Sara-Magni)

---

## Acknowledgments

- **Data Source**: Google Merchandise Store (Google Analytics Sample Dataset)
- **Inspiration**: Real-world e-commerce optimization challenges faced by wine retailers
- **Tools**: Built with open-source technologies and Tableau Public

---

*Every metric is grounded in data, every recommendation is testable, and every visualization tells a story.*