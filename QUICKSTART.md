# 🚀 Quick Start Guide - DecisionPilot AI

## Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Streamlit (UI framework)
- XGBoost (ML forecasting)
- TensorFlow/Keras (LSTM models)
- Plotly (visualizations)
- Pandas, NumPy (data processing)

### Step 2: Run the Application
```bash
streamlit run app.py
```

The application will start on `http://localhost:8501`

### Step 3: Load Sample Data
1. Open the app in your browser
2. Click "Load Sample Data" in the sidebar
3. Explore the features!

## 📱 Features Overview

### 🏠 Home
- Quick business overview
- Key metrics at a glance
- Health score and trends

### 📊 Business Analytics
- Revenue, costs, and profit trends
- Regional performance analysis
- Product category breakdown
- Raw data exploration

### 🔮 Forecasting
- **Models**: XGBoost and LSTM
- **Options**: 7-30 day forecasts
- **Targets**: Revenue or Profit
- Confidence intervals included

### 🎲 Scenario Simulation

**Quick Scenarios:**
- 10% Price Increase
- 5% Cost Reduction
- 15% Volume Increase
- Expand to 2 New Regions

**Custom Scenarios:**
- Adjust price, costs, volume, efficiency
- See immediate impact on profit

**Monte Carlo:**
- Risk simulation
- 100-5000 iterations
- Probability analysis

### 🛡️ Risk Assessment
- Risk heatmap visualization
- Priority risk identification
- AI-powered mitigation strategies
- Track risk status

### 💡 AI Advisor
- Executive summary reports
- Strategic recommendations
- Business health analysis
- Performance benchmarking

### 📈 Executive Dashboard
- Comprehensive KPI view
- Performance gauges
- All key metrics in one place

## 💡 Tips

### For Best Results:
1. **Load Data First**: Always load sample data before exploring features
2. **Start with Analytics**: Understand your current state
3. **Try Forecasting**: See where you're heading
4. **Run Scenarios**: Test different strategies
5. **Check Advisor**: Get AI-powered recommendations

### Understanding Metrics:
- **Health Score**: Overall business performance (0-100)
- **Profit Margin**: Profitability ratio (higher is better)
- **Revenue Growth**: Change over time (positive = growing)
- **Risk Score**: Potential business risks (lower is better)

### Interpreting Forecasts:
- **XGBoost**: Good for stable trends
- **LSTM**: Better for complex patterns
- **Confidence Interval**: Shows uncertainty range
- Compare both models for best insight

### Using Scenarios:
- **Green recommendations**: Implement immediately
- **Yellow warnings**: Consider carefully
- **Red alerts**: Avoid or mitigate
- Run multiple scenarios to compare

## 🔧 Customization

### Add Your Own Data:
Replace the CSV files in the `data/` folder:
- `sample_sales.csv`: Your sales data
- `sample_risks.csv`: Your risk data

**Required columns for sales data:**
- date, revenue, costs, profit, region, product_category, units_sold, customer_satisfaction

**Required columns for risk data:**
- risk_id, risk_category, severity, probability, impact_score, mitigation_status, description

### Adjust Model Parameters:
Edit `predictor.py` to change:
- Forecast window size
- Model hyperparameters
- Feature engineering

### Customize Scenarios:
Edit `simulator.py` to add:
- New scenario types
- Custom business logic
- Industry-specific models

## 🐛 Troubleshooting

### App won't start?
```bash
# Check Python version (needs 3.8+)
python --version

# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

### Data not loading?
- Ensure CSV files are in the `data/` folder
- Check file format matches requirements
- Look for error messages in the sidebar

### Models not training?
- First run takes longer (training models)
- Subsequent runs use cached models
- Check `models/` folder for saved models

### Charts not displaying?
- Ensure Plotly is installed
- Check browser console for errors
- Try refreshing the page

## 📞 Support

For issues or questions:
1. Check the [README.md](README.md) for detailed documentation
2. Review error messages in the Streamlit interface
3. Open an issue on GitHub

## 🎯 Next Steps

Once you're comfortable:
1. **Import real data**: Replace sample data with your business data
2. **Customize scenarios**: Add industry-specific scenarios
3. **Extend models**: Add more ML models or features
4. **Share insights**: Export reports for stakeholders
5. **Deploy**: Host on Streamlit Cloud for team access

---

**Ready to make data-driven decisions? Start exploring! 🚀**
