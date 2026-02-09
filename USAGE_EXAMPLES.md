# 📚 Usage Examples - DecisionPilot AI

## Real-World Scenarios

### Scenario 1: CEO Strategic Planning

**Situation:** CEO needs to decide whether to expand into 2 new regions

**Steps:**
1. Navigate to **Business Analytics** to understand current performance
2. Check **Health Score** - if > 70, expansion is viable
3. Go to **Scenario Simulation** → Quick Scenarios
4. Select "Expand 2 Regions"
5. Click "Run Scenarios"

**Expected Output:**
```
Revenue Impact: +60%
Profit Impact: +XX%
Margin: XX%
Recommendation: ✅/⚠️/❌
```

**Decision Framework:**
- ✅ If profit increase > 20% → Expand
- ⚠️ If profit increase 10-20% → Consider carefully
- ❌ If profit increase < 10% → Not recommended

---

### Scenario 2: CFO Budget Planning

**Situation:** CFO needs 3-month revenue forecast for budget planning

**Steps:**
1. Navigate to **Forecasting**
2. Set Forecast Horizon: 30 days (~1 month)
3. Select Model: LSTM (better for longer forecasts)
4. Target Metric: Revenue
5. Click "Generate Forecast"

**Analysis:**
- Review average forecast value
- Check trend direction (📈 or 📉)
- Note confidence interval range
- Compare with XGBoost for validation

**Budget Recommendation:**
- Conservative: Use 5th percentile value
- Moderate: Use mean forecast
- Optimistic: Use 95th percentile

---

### Scenario 3: Risk Manager Assessment

**Situation:** Quarterly risk review meeting

**Steps:**
1. Navigate to **Risk Assessment**
2. Review Risk Heatmap
3. Identify high-severity + high-probability risks
4. Check Priority Risks section
5. Review AI recommendations

**Report Template:**
```
Total Risks: X
High Priority: Y
Risk Score: Z/100

Top 3 Risks:
1. [Risk Description] - Impact: X/10
   Mitigation: [Actions]
2. [Risk Description] - Impact: X/10
   Mitigation: [Actions]
3. [Risk Description] - Impact: X/10
   Mitigation: [Actions]
```

---

### Scenario 4: Sales Director Pricing Strategy

**Situation:** Considering 10% price increase for product line

**Steps:**
1. Go to **Scenario Simulation** → Quick Scenarios
2. Select "10% Price Increase"
3. Run scenario

**Analysis Checklist:**
- [ ] Profit impact > 15%? 
- [ ] Customer satisfaction impact acceptable?
- [ ] Competitive position maintained?
- [ ] Volume loss < 5%?

**Alternative Test:**
Use Custom Scenario to test 5%, 7%, 10%, 12%, 15% increases

---

### Scenario 5: Operations Manager Cost Optimization

**Situation:** Need to reduce costs without impacting revenue

**Steps:**
1. Navigate to **Business Analytics**
2. Identify highest cost regions/products
3. Go to **Scenario Simulation** → Custom Scenario
4. Test different combinations:
   - Cost: -5%, Efficiency: +10%
   - Cost: -10%, Efficiency: +15%
   - Cost: -3%, Volume: +5%

**Optimization Goals:**
- Maintain or increase profit margin
- Keep customer satisfaction > 4.5
- Minimal revenue impact

---

### Scenario 6: Board Meeting Preparation

**Situation:** CEO needs comprehensive overview for board

**Steps:**
1. Start at **Home** for quick metrics
2. Visit **Executive Dashboard** for full view
3. Check **AI Advisor** for executive summary
4. Generate forecasts in **Forecasting**
5. Run key scenarios in **Simulation**

**Board Deck Structure:**
```
Slide 1: Business Health Overview
- Health Score: XX/100
- Revenue: $X.XX M (Growth: +X%)
- Profit Margin: XX%

Slide 2: Performance vs Benchmarks
- Regional breakdown
- Product performance
- Customer satisfaction

Slide 3: Forecast & Outlook
- 30-day revenue forecast
- Trend analysis
- Confidence intervals

Slide 4: Strategic Scenarios
- Scenario comparison charts
- Recommended actions
- Expected ROI

Slide 5: Risk & Mitigation
- Top 3 risks
- Mitigation strategies
- Risk score trend
```

---

## Advanced Use Cases

### Monte Carlo Risk Analysis

**When to use:** Major investment decisions, M&A, new product launches

**Steps:**
1. **Scenario Simulation** → Monte Carlo tab
2. Set iterations: 1000-5000
3. Run simulation
4. Analyze results:
   - Mean profit: Expected value
   - Std dev: Volatility/risk
   - 5th percentile: Worst case
   - 95th percentile: Best case
   - Probability profitable: Success chance

**Decision Rules:**
- If P(profitable) > 80% → Low risk
- If P(profitable) 60-80% → Moderate risk
- If P(profitable) < 60% → High risk

---

### Sensitivity Analysis

**When to use:** Understanding which factors have biggest impact

**Method:**
1. Run custom scenarios varying one parameter at a time
2. Keep others constant
3. Plot profit vs parameter value
4. Identify most sensitive variables

**Example:**
```
Price -10%: Profit -$XXX,XXX
Price -5%:  Profit -$XX,XXX
Price 0%:   Profit $X,XXX,XXX (baseline)
Price +5%:  Profit $X,XXX,XXX
Price +10%: Profit $X,XXX,XXX
```

Most sensitive = Largest profit change per % change

---

### Combining Multiple Strategies

**Optimal Strategy Example:**

**Test Combination:**
- Price: +5%
- Cost: -3%
- Efficiency: +10%
- Volume: +8%

**Steps:**
1. Custom Scenario Builder
2. Set all parameters
3. Run simulation
4. Compare vs individual strategies

**Goal:** Find combination with highest profit impact

---

## Data Interpretation Guide

### Health Score Meanings
- **90-100**: Excellent - Maintain and expand
- **70-89**: Good - Optimize and grow
- **50-69**: Fair - Focus on improvement
- **< 50**: Critical - Immediate action needed

### Profit Margin Benchmarks
- **> 20%**: Excellent
- **15-20%**: Good
- **10-15%**: Average
- **< 10%**: Poor

### Risk Score Levels
- **> 70**: Critical - Urgent mitigation
- **50-70**: High - Active management
- **30-50**: Moderate - Monitor closely
- **< 30**: Low - Standard oversight

### Forecast Confidence
- **Narrow interval**: High confidence
- **Wide interval**: High uncertainty
- **Upward trend**: Positive outlook
- **Downward trend**: Concerning

---

## Best Practices

### 1. Regular Monitoring
- Daily: Check key metrics
- Weekly: Review trends and forecasts
- Monthly: Full health assessment
- Quarterly: Strategic scenario analysis

### 2. Data-Driven Decisions
- Always check multiple scenarios
- Compare forecasts from both models
- Consider risk scores
- Review AI recommendations

### 3. Documentation
- Record decisions and rationale
- Track scenario outcomes
- Monitor forecast accuracy
- Update strategies based on results

### 4. Stakeholder Communication
- Use Executive Dashboard for board
- Share AI Advisor summary with team
- Explain scenario results clearly
- Present both opportunities and risks

---

## Quick Reference Commands

### Start Application
```bash
streamlit run app.py
```

### Access URL
```
http://localhost:8501
```

### Key Navigation
- Home: Overview and quick metrics
- Analytics: Detailed performance analysis
- Forecasting: Predictive models
- Simulation: What-if scenarios
- Risk: Risk assessment
- Advisor: AI recommendations
- Dashboard: Executive view

---

**Need Help?** Check [QUICKSTART.md](QUICKSTART.md) or [README.md](README.md)
