# 🧠 DecisionPilot AI - Enterprise Decision Intelligence Platform

> **Transform your business decisions with AI-powered analytics, forecasting, and strategic recommendations**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28-FF4B4B)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🚀 Overview

**DecisionPilot AI** is an enterprise-grade AI decision intelligence platform designed for executives and business leaders. It combines advanced machine learning, predictive analytics, and intelligent advisory systems to provide actionable insights for strategic decision-making.

### ✨ Key Features

- 📊 **Business Analytics** - Real-time performance metrics and comprehensive business intelligence
- 🔮 **AI Forecasting** - XGBoost and LSTM-based predictions for revenue, profit, and key metrics
- 🎲 **Scenario Simulation** - What-if analysis, Monte Carlo simulations, and sensitivity testing
- 🛡️ **Risk Assessment** - Intelligent risk identification and mitigation recommendations
- 💡 **AI Advisor** - Strategic recommendations powered by business intelligence algorithms
- 📈 **Executive Dashboard** - Premium visualizations and KPI tracking

## 🧱 Tech Stack

| Layer | Technology |
|-------|-----------|
| **ML** | XGBoost, LSTM (TensorFlow/Keras) |
| **NLP** | Transformers (LLM-ready) |
| **Backend** | FastAPI (ready for API endpoints) |
| **Frontend** | Streamlit |
| **Database** | SQLite (SQLAlchemy-ready) |
| **Visualization** | Plotly, Matplotlib, Seaborn |
| **Cloud** | Streamlit Cloud (deployment-ready) |

## 📁 Project Structure

```
DecisionPilot-AI/
│
├── app.py                 # Main Streamlit application
├── advisor.py             # AI business advisor module
├── predictor.py           # ML forecasting engine (XGBoost/LSTM)
├── simulator.py           # Scenario simulation engine
├── dashboard.py           # Analytics dashboard generator
│
├── data/                  # Sample datasets
│   ├── sample_sales.csv   # Historical sales data
│   └── sample_risks.csv   # Risk assessment data
│
├── models/                # Trained ML models
│   ├── xgboost_model.pkl  # (generated)
│   └── lstm_model.h5      # (generated)
│
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔧 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ravigohel142996/AI-Decision-Intelligence-Platform.git
   cd AI-Decision-Intelligence-Platform
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the app**
   - Open your browser and navigate to `http://localhost:8501`

## 💻 Usage

### 1. Load Sample Data
- Click "Load Sample Data" in the sidebar
- The platform will load historical sales and risk data

### 2. Explore Features

#### 📊 Business Analytics
- View revenue, cost, and profit trends
- Analyze regional and product performance
- Track key performance indicators

#### 🔮 Forecasting
- Select forecast horizon (7-30 days)
- Choose between XGBoost and LSTM models
- Generate predictions for revenue or profit
- Visualize forecasts with confidence intervals

#### 🎲 Scenario Simulation
- **Quick Scenarios**: Test predefined business scenarios
  - Price increases/decreases
  - Cost optimization
  - Volume changes
  - Market expansion
- **Custom Scenarios**: Build your own what-if analysis
- **Monte Carlo**: Risk simulation with thousands of iterations

#### 🛡️ Risk Assessment
- View risk heatmaps by category and severity
- Identify high-priority risks
- Get AI-powered mitigation recommendations

#### 💡 AI Advisor
- Receive strategic recommendations
- Get executive summaries
- Access business health scores

#### 📈 Executive Dashboard
- Comprehensive view of all key metrics
- Performance gauges and indicators
- Quick decision-making insights

## 🎯 Use Cases

### For CEOs and Business Leaders
- Strategic planning and decision-making
- Performance monitoring and KPI tracking
- Risk identification and mitigation
- Investment scenario analysis

### For Finance Teams
- Revenue and profit forecasting
- Budget planning and variance analysis
- Financial scenario modeling
- Cost optimization strategies

### For Operations Managers
- Efficiency improvement identification
- Capacity planning
- Supply chain optimization
- Regional performance analysis

## 🔬 Machine Learning Models

### XGBoost Forecasting
- **Algorithm**: Gradient Boosted Trees
- **Features**: Lagged values, rolling statistics, temporal features
- **Use Case**: Short to medium-term predictions with high accuracy

### LSTM Neural Networks
- **Architecture**: Multi-layer LSTM with dropout
- **Features**: Sequential time series patterns
- **Use Case**: Long-term trend forecasting and pattern recognition

### Business Intelligence
- Knowledge-based recommendation system
- Rule-based risk assessment
- Statistical benchmarking

## 📊 Sample Data

The platform includes comprehensive sample datasets:

- **Sales Data**: 40+ days of historical data
  - Daily revenue, costs, profit
  - Regional breakdown (North, South, East, West)
  - Product categories (Electronics, Clothing)
  - Customer satisfaction scores

- **Risk Data**: 10 enterprise risks
  - Categories: Financial, Operational, Strategic, Compliance, Technology
  - Severity levels and impact scores
  - Mitigation status tracking

## 🚀 Deployment

### Streamlit Cloud
1. Push your code to GitHub
2. Connect to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy directly from your repository

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

## 🔐 Security Notes

- **All dependencies updated to patched versions** - No known vulnerabilities
- FastAPI 0.115.0+ - Fixes ReDoS vulnerability
- PyTorch 2.6.0+ - Fixes heap buffer overflow and RCE vulnerabilities  
- Transformers 4.48.0+ - Fixes deserialization vulnerabilities
- Uses TensorFlow's integrated Keras (no separate vulnerable keras package)
- Environment variables support via python-dotenv
- Ready for FastAPI backend integration with secure version

## 🛠️ Customization

### Adding New Data Sources
```python
# In app.py
sales_df = pd.read_csv('your_data.csv')
```

### Extending Models
```python
# In predictor.py
def train_custom_model(self, df):
    # Add your custom ML model
    pass
```

### Creating Custom Scenarios
```python
# In simulator.py
def simulate_custom_scenario(self, df, **params):
    # Implement your business logic
    pass
```

## 📈 Roadmap

- [ ] Real-time data streaming integration
- [ ] Advanced NLP with LLM integration
- [ ] Multi-user support with authentication
- [ ] Custom alert system
- [ ] Export reports to PDF
- [ ] API endpoints with FastAPI
- [ ] Mobile-responsive design
- [ ] Integration with ERP systems

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License.

## 👤 Author

**Ravi Gohel**
- GitHub: [@ravigohel142996](https://github.com/ravigohel142996)

## 🙏 Acknowledgments

- Built with Streamlit for rapid prototyping
- ML models powered by XGBoost and TensorFlow
- Visualizations by Plotly
- Inspired by enterprise business intelligence platforms

---

**⭐ Star this repository if you find it helpful!**
