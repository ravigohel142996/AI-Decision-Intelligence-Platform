"""
DecisionPilot AI - Enterprise AI Decision Intelligence Platform
Main Streamlit Application
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# Import modules
from advisor import BusinessAdvisor
from predictor import BusinessPredictor
from simulator import BusinessSimulator
from dashboard import BusinessDashboard


# Page configuration
st.set_page_config(
    page_title="DecisionPilot AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium UI
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, rgba(248,250,255,0.9) 0%, rgba(255,255,255,1) 35%);
    }
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        padding: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-card {
        background: white;
        padding: 1.25rem;
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(31, 119, 180, 0.08);
        border: 1px solid rgba(31, 119, 180, 0.08);
    }
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .kpi-card {
        background: linear-gradient(135deg, #1f77b4 0%, #17a2b8 100%);
        padding: 1.25rem;
        border-radius: 14px;
        color: white;
        text-align: left;
        box-shadow: 0 6px 16px rgba(31, 119, 180, 0.2);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
    }
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        font-weight: bold;
        border-radius: 5px;
    }
    .glass-banner {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 18px;
        padding: 1.5rem 2rem;
        box-shadow: 0 12px 30px rgba(0,0,0,0.08);
        border: 1px solid rgba(255,255,255,0.4);
    }
    .pill {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 999px;
        font-size: 0.8rem;
        background: rgba(31, 119, 180, 0.1);
        color: #1f77b4;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    .recommendation-box {
        background: #f0f8ff;
        padding: 1rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .alert-box {
        background: #fff3cd;
        padding: 1rem;
        border-left: 4px solid #ff9900;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .success-box {
        background: #d4edda;
        padding: 1rem;
        border-left: 4px solid #28a745;
        margin: 1rem 0;
        border-radius: 5px;
    }
    .sidebar-card {
        background: rgba(31, 119, 180, 0.08);
        padding: 0.75rem 1rem;
        border-radius: 12px;
        margin-top: 1rem;
        border: 1px solid rgba(31, 119, 180, 0.1);
    }
</style>
""", unsafe_allow_html=True)


# Initialize session state
if 'data_loaded' not in st.session_state:
    st.session_state.data_loaded = False
if 'sales_data' not in st.session_state:
    st.session_state.sales_data = None
if 'risks_data' not in st.session_state:
    st.session_state.risks_data = None
if 'kpi_data' not in st.session_state:
    st.session_state.kpi_data = None


# Initialize modules
@st.cache_resource
def initialize_modules():
    """Initialize all modules"""
    advisor = BusinessAdvisor()
    predictor = BusinessPredictor()
    simulator = BusinessSimulator()
    dashboard = BusinessDashboard()
    return advisor, predictor, simulator, dashboard


def load_data():
    """Load sample data"""
    try:
        sales_df = pd.read_csv('data/sample_sales.csv')
        risks_df = pd.read_csv('data/sample_risks.csv')
        kpi_df = pd.read_csv('data/sample_kpis.csv')
        return sales_df, risks_df, kpi_df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None, None, None


def main():
    """Main application"""
    
    # Header
    st.markdown('<div class="main-header">🧠 DecisionPilot AI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Enterprise AI Brain for Strategic Decision Making</div>', unsafe_allow_html=True)
    
    # Initialize modules
    advisor, predictor, simulator, dashboard = initialize_modules()
    
    # Sidebar
    st.sidebar.title("🎯 Navigation")
    page = st.sidebar.radio(
        "Select Feature",
        ["🏠 Home", "📊 Business Analytics", "🔮 Forecasting", "🎲 Scenario Simulation",
         "🚨 Risk Detection", "🛡️ Risk Assessment", "💡 AI Advisor", "📈 Executive Dashboard"]
    )
    
    # Data loading
    st.sidebar.markdown("---")
    st.sidebar.subheader("📁 Data Management")
    
    if st.sidebar.button("Load Sample Data"):
        sales_df, risks_df, kpi_df = load_data()
        if sales_df is not None:
            st.session_state.sales_data = sales_df
            st.session_state.risks_data = risks_df
            st.session_state.kpi_data = kpi_df
            st.session_state.data_loaded = True
            st.sidebar.success("✅ Data loaded successfully!")
    
    # Check if data is loaded
    if not st.session_state.data_loaded:
        st.warning("⚠️ Please load sample data from the sidebar to continue.")
        return
    
    sales_df = st.session_state.sales_data
    risks_df = st.session_state.risks_data
    kpi_df = st.session_state.kpi_data
    
    # Page routing
    if page == "🏠 Home":
        show_home(sales_df, risks_df, kpi_df, advisor, dashboard)
    
    elif page == "📊 Business Analytics":
        show_business_analytics(sales_df, dashboard)
    
    elif page == "🔮 Forecasting":
        show_forecasting(sales_df, predictor, dashboard)
    
    elif page == "🎲 Scenario Simulation":
        show_scenario_simulation(sales_df, simulator, dashboard)

    elif page == "🚨 Risk Detection":
        show_risk_detection(sales_df, advisor, dashboard)
    
    elif page == "🛡️ Risk Assessment":
        show_risk_assessment(risks_df, advisor, dashboard)
    
    elif page == "💡 AI Advisor":
        show_ai_advisor(sales_df, risks_df, advisor)
    
    elif page == "📈 Executive Dashboard":
        show_executive_dashboard(sales_df, risks_df, kpi_df, advisor, predictor, dashboard)


def show_home(sales_df, risks_df, kpi_df, advisor, dashboard):
    """Home page with overview"""
    st.header("Welcome to DecisionPilot AI")

    st.markdown("""
    <div class="glass-banner">
        <span class="pill">Enterprise AI</span>
        <span class="pill">Real-time Analytics</span>
        <span class="pill">Secure by Design</span>
        <h3>🚀 Enterprise-Grade AI Decision Intelligence Platform</h3>
        <p><strong>DecisionPilot AI</strong> empowers executives with advanced analytics, predictive insights,
        and intelligent recommendations for strategic decision-making.</p>
        <p><strong>Mission Control:</strong> Unified analytics, forecasting, risk detection, and simulation
        across business, operations, and finance teams.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### 🎯 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Business Analytics**
        - Real-time performance metrics
        - Regional & product analysis
        - Trend visualization
        """)
    
    with col2:
        st.markdown("""
        **🔮 AI Forecasting**
        - XGBoost predictions
        - LSTM time series
        - Multi-period forecasts
        """)
    
    with col3:
        st.markdown("""
        **🎲 Scenario Simulation**
        - What-if analysis
        - Monte Carlo simulation
        - Sensitivity analysis
        """)
    
    st.markdown("---")
    
    # Quick metrics
    st.subheader("📈 Quick Business Overview")
    
    health = advisor.analyze_business_health(sales_df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "Total Revenue",
            f"${health['total_revenue']:,.0f}",
            delta=f"{health['revenue_growth_rate']:.1%}"
        )
    
    with col2:
        st.metric(
            "Total Profit",
            f"${health['total_profit']:,.0f}",
            delta=f"{health['profit_margin']:.1%}"
        )
    
    with col3:
        st.metric(
            "Health Score",
            f"{health['health_score']:.0f}/100",
            delta=health['overall_status']
        )
    
    with col4:
        st.metric(
            "Customer Satisfaction",
            f"{health['avg_customer_satisfaction']:.2f}/5.0",
            delta=health['satisfaction_rating']['rating']
        )

    st.markdown("---")

    st.subheader("✨ Enterprise KPI Pulse")
    latest_kpi = kpi_df.sort_values('date').iloc[-1]

    kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)
    with kpi_col1:
        st.markdown(
            f"<div class='kpi-card'><div class='metric-label'>NPS</div>"
            f"<div class='metric-value'>{latest_kpi['nps']:.0f}</div></div>",
            unsafe_allow_html=True
        )
    with kpi_col2:
        st.markdown(
            f"<div class='kpi-card'><div class='metric-label'>Churn</div>"
            f"<div class='metric-value'>{latest_kpi['churn_rate']:.1%}</div></div>",
            unsafe_allow_html=True
        )
    with kpi_col3:
        st.markdown(
            f"<div class='kpi-card'><div class='metric-label'>Pipeline</div>"
            f"<div class='metric-value'>${latest_kpi['pipeline_value']/1e6:.2f}M</div></div>",
            unsafe_allow_html=True
        )
    with kpi_col4:
        st.markdown(
            f"<div class='kpi-card'><div class='metric-label'>Engagement</div>"
            f"<div class='metric-value'>{latest_kpi['employee_engagement']:.2f}/5</div></div>",
            unsafe_allow_html=True
        )
    with kpi_col5:
        st.markdown(
            f"<div class='kpi-card'><div class='metric-label'>Partner Health</div>"
            f"<div class='metric-value'>{latest_kpi['partner_health']:.0f}</div></div>",
            unsafe_allow_html=True
        )

    with st.expander("📊 KPI Trends"):
        kpi_fig = dashboard.create_kpi_trends(kpi_df)
        st.plotly_chart(kpi_fig, use_container_width=True)


def show_business_analytics(sales_df, dashboard):
    """Business analytics page"""
    st.header("📊 Business Analytics Dashboard")
    
    # Revenue trends
    st.subheader("Revenue, Costs, and Profit Trends")
    fig1 = dashboard.create_revenue_trend_chart(sales_df)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Regional analysis
    st.subheader("Regional Performance Analysis")
    fig2 = dashboard.create_regional_analysis(sales_df)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Product analysis
    st.subheader("Product Category Analysis")
    fig3 = dashboard.create_product_analysis(sales_df)
    st.plotly_chart(fig3, use_container_width=True)
    
    # Data table
    with st.expander("📋 View Raw Data"):
        st.dataframe(sales_df, use_container_width=True)


def show_forecasting(sales_df, predictor, dashboard):
    """Forecasting page"""
    st.header("🔮 AI-Powered Forecasting")
    
    col1, col2 = st.columns([2, 1])
    
    with col2:
        st.subheader("Forecast Settings")
        forecast_days = st.slider("Forecast Horizon (days)", 7, 30, 14)
        forecast_method = st.selectbox("Model", ["XGBoost", "LSTM"])
        target_metric = st.selectbox("Target Metric", ["revenue", "profit"])
        
        if st.button("Generate Forecast"):
            with st.spinner("Training model and generating forecast..."):
                method = forecast_method.lower()
                forecast = predictor.forecast_next_n_days(
                    sales_df, 
                    n_days=forecast_days, 
                    target_col=target_metric,
                    method=method
                )
                
                # Store forecast with its parameters to detect stale data
                st.session_state.forecast = forecast
                st.session_state.forecast_params = {
                    'days': forecast_days,
                    'method': forecast_method,
                    'metric': target_metric
                }
                st.session_state.forecast_generated = True
                st.success("✅ Forecast generated!")
    
    with col1:
        st.subheader("Forecast Visualization")
        
        if 'forecast_generated' in st.session_state and st.session_state.forecast_generated:
            historical = sales_df[target_metric].values[-30:]
            forecast = st.session_state.forecast
            
            fig = dashboard.create_forecast_chart(
                historical.tolist(),
                forecast
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Forecast summary
            st.markdown("### 📊 Forecast Summary")
            avg_forecast = np.mean(forecast)
            trend = "Upward 📈" if forecast[-1] > forecast[0] else "Downward 📉"
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Average Forecast", f"${avg_forecast:,.0f}")
            with col_b:
                st.metric("Trend", trend)
            with col_c:
                st.metric("Last Value", f"${forecast[-1]:,.0f}")
        else:
            st.info("👈 Configure settings and click 'Generate Forecast' to see predictions")


def show_scenario_simulation(sales_df, simulator, dashboard):
    """Scenario simulation page"""
    st.header("🎲 Scenario Simulation & What-If Analysis")
    
    tab1, tab2, tab3 = st.tabs(["Quick Scenarios", "Custom Scenario", "Monte Carlo"])
    
    with tab1:
        st.subheader("Quick Scenario Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            scenarios_to_run = st.multiselect(
                "Select Scenarios",
                ["10% Price Increase", "5% Cost Reduction", "15% Volume Increase", "Expand 2 Regions"],
                default=["10% Price Increase"]
            )
        
        if st.button("Run Scenarios"):
            with st.spinner("Running simulations..."):
                comparisons = []
                
                if "10% Price Increase" in scenarios_to_run:
                    scenario = simulator.simulate_price_change(sales_df, 10)
                    comp = simulator.compare_scenarios(sales_df, scenario, "10% Price Increase")
                    comparisons.append(comp)
                
                if "5% Cost Reduction" in scenarios_to_run:
                    scenario = simulator.simulate_cost_change(sales_df, -5)
                    comp = simulator.compare_scenarios(sales_df, scenario, "5% Cost Reduction")
                    comparisons.append(comp)
                
                if "15% Volume Increase" in scenarios_to_run:
                    scenario = simulator.simulate_volume_change(sales_df, 15)
                    comp = simulator.compare_scenarios(sales_df, scenario, "15% Volume Increase")
                    comparisons.append(comp)
                
                if "Expand 2 Regions" in scenarios_to_run:
                    scenario = simulator.simulate_market_expansion(sales_df, 2)
                    comp = simulator.compare_scenarios(sales_df, scenario, "Expand to 2 New Regions")
                    comparisons.append(comp)
                
                # Display results
                if comparisons:
                    fig = dashboard.create_scenario_comparison(comparisons)
                    st.plotly_chart(fig, use_container_width=True)
                    
                    # Detailed results
                    for comp in comparisons:
                        with st.expander(f"📊 {comp['scenario_name']}"):
                            col_a, col_b, col_c = st.columns(3)
                            with col_a:
                                st.metric("Revenue Impact", 
                                         f"${comp['scenario_revenue']:,.0f}",
                                         f"{comp['revenue_change_pct']:+.1f}%")
                            with col_b:
                                st.metric("Profit Impact",
                                         f"${comp['scenario_profit']:,.0f}",
                                         f"{comp['profit_change_pct']:+.1f}%")
                            with col_c:
                                st.metric("Margin",
                                         f"{comp['scenario_margin']:.1%}",
                                         f"{comp['margin_change_pct']:+.1f}%")
                            
                            st.markdown(f"**{comp['recommendation']}**")
    
    with tab2:
        st.subheader("Custom Scenario Builder")
        
        col1, col2 = st.columns(2)
        
        with col1:
            price_change = st.slider("Price Change (%)", -30, 30, 0)
            cost_change = st.slider("Cost Change (%)", -30, 30, 0)
        
        with col2:
            volume_change = st.slider("Volume Change (%)", -30, 30, 0)
            efficiency_gain = st.slider("Efficiency Gain (%)", 0, 30, 0)
        
        if st.button("Run Custom Scenario"):
            scenario = simulator.simulate_custom_scenario(
                sales_df,
                price_change=price_change,
                cost_change=cost_change,
                volume_change=volume_change,
                efficiency_gain=efficiency_gain
            )
            
            comp = simulator.compare_scenarios(sales_df, scenario, "Custom Scenario")
            
            st.success("✅ Simulation complete!")
            
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Revenue Impact", 
                         f"${comp['scenario_revenue']:,.0f}",
                         f"{comp['revenue_change_pct']:+.1f}%")
            with col_b:
                st.metric("Profit Impact",
                         f"${comp['scenario_profit']:,.0f}",
                         f"{comp['profit_change_pct']:+.1f}%")
            with col_c:
                st.metric("Margin",
                         f"{comp['scenario_margin']:.1%}",
                         f"{comp['margin_change_pct']:+.1f}%")
            
            st.markdown(f"### {comp['recommendation']}")
    
    with tab3:
        st.subheader("Monte Carlo Risk Simulation")
        
        iterations = st.slider("Number of Iterations", 100, 5000, 1000)
        
        if st.button("Run Monte Carlo Simulation"):
            with st.spinner("Running Monte Carlo simulation..."):
                results = simulator.run_monte_carlo_simulation(sales_df, iterations=iterations)
                
                st.success("✅ Simulation complete!")
                
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Mean Profit", f"${results['mean_profit']:,.0f}")
                with col2:
                    st.metric("Std Dev", f"${results['std_profit']:,.0f}")
                with col3:
                    st.metric("5th Percentile", f"${results['profit_5th_percentile']:,.0f}")
                with col4:
                    st.metric("Probability Profitable", f"{results['probability_profitable']:.1%}")


def show_risk_detection(sales_df, advisor, dashboard):
    """Risk detection page using anomaly signals"""
    st.header("🚨 Risk Detection & Early Warning System")
    st.markdown("Proactively identify operational anomalies and potential revenue risks.")

    detection = advisor.detect_operational_risks(sales_df)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Detected Anomalies", detection['anomaly_count'])
    with col2:
        st.metric("Operational Risk Score", f"{detection['risk_score']:.1f}/100")
    with col3:
        st.metric("Monitoring Window", "14 days")

    st.subheader("📉 Revenue Trend with Anomaly Focus")
    fig = dashboard.create_revenue_trend_chart(sales_df)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("🔍 Anomaly Log")
    if detection['anomalies']:
        anomaly_df = pd.DataFrame(detection['anomalies'])
        st.dataframe(anomaly_df, use_container_width=True)
    else:
        st.success("✅ No significant anomalies detected across the monitoring window.")


def show_risk_assessment(risks_df, advisor, dashboard):
    """Risk assessment page"""
    st.header("🛡️ Risk Assessment & Mitigation")
    
    # Analyze risks
    risk_analysis = advisor.analyze_risks(risks_df)
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Risks", risk_analysis['total_risks'])
    with col2:
        st.metric("High Priority", risk_analysis['high_risk_count'])
    with col3:
        st.metric("Risk Score", f"{risk_analysis['risk_score']:.1f}/100")
    with col4:
        st.metric("Avg Impact", f"{risk_analysis['avg_impact_score']:.1f}/10")
    
    # Risk heatmap
    st.subheader("Risk Assessment Heatmap")
    fig = dashboard.create_risk_heatmap(risks_df)
    st.plotly_chart(fig, use_container_width=True)
    
    # Priority risks
    st.subheader("🚨 Priority Risks")
    
    if risk_analysis['priority_risks']:
        for risk in risk_analysis['priority_risks']:
            with st.expander(f"⚠️ {risk['description']}"):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.write(f"**Category:** {risk['risk_category']}")
                with col_b:
                    st.write(f"**Severity:** {risk['severity']}")
                with col_c:
                    st.write(f"**Impact:** {risk['impact_score']}/10")
                
                st.write(f"**Probability:** {risk['probability']:.0%}")
                st.write(f"**Status:** {risk['mitigation_status']}")
    else:
        st.success("✅ No high-priority risks identified")
    
    # Recommendations
    st.subheader("💡 Risk Mitigation Recommendations")
    recommendations = advisor.get_risk_recommendations(risk_analysis)
    for rec in recommendations:
        st.markdown(rec)
    
    # All risks table
    with st.expander("📋 View All Risks"):
        st.dataframe(risks_df, use_container_width=True)


def show_ai_advisor(sales_df, risks_df, advisor):
    """AI Advisor page"""
    st.header("💡 AI Business Advisor")
    
    # Analyze business
    health_analysis = advisor.analyze_business_health(sales_df)
    risk_analysis = advisor.analyze_risks(risks_df)
    
    # Executive summary
    st.subheader("📄 Executive Summary")
    summary = advisor.generate_executive_summary(health_analysis, risk_analysis)
    st.code(summary, language=None)
    
    # Strategic recommendations
    st.subheader("🎯 Strategic Recommendations")
    recommendations = advisor.get_strategic_recommendations(health_analysis)
    
    for rec in recommendations:
        if "PRIORITY" in rec or "URGENT" in rec:
            st.markdown(f'<div class="alert-box">{rec}</div>', unsafe_allow_html=True)
        elif "✅" in rec:
            st.markdown(f'<div class="success-box">{rec}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="recommendation-box">{rec}</div>', unsafe_allow_html=True)


def show_executive_dashboard(sales_df, risks_df, kpi_df, advisor, predictor, dashboard):
    """Executive dashboard with all key metrics"""
    st.header("📈 Executive Dashboard")
    
    # Analyze data
    health = advisor.analyze_business_health(sales_df)
    
    # Performance gauges
    st.subheader("Performance Indicators")
    fig_gauges = dashboard.create_performance_gauges(health)
    st.plotly_chart(fig_gauges, use_container_width=True)
    
    # Two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Revenue Trends")
        fig_revenue = dashboard.create_revenue_trend_chart(sales_df)
        st.plotly_chart(fig_revenue, use_container_width=True)
    
    with col2:
        st.subheader("Regional Performance")
        fig_regional = dashboard.create_regional_analysis(sales_df)
        st.plotly_chart(fig_regional, use_container_width=True)
    
    # Risk assessment
    st.subheader("Risk Overview")
    fig_risk = dashboard.create_risk_heatmap(risks_df)
    st.plotly_chart(fig_risk, use_container_width=True)

    st.subheader("Enterprise KPI Trends")
    kpi_fig = dashboard.create_kpi_trends(kpi_df)
    st.plotly_chart(kpi_fig, use_container_width=True)


if __name__ == "__main__":
    main()
