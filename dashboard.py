"""
Dashboard Module - Business Analytics Dashboard
Provides comprehensive business intelligence visualizations
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from typing import Dict, List, Any


class BusinessDashboard:
    """Advanced analytics dashboard generator"""
    
    def __init__(self):
        self.color_scheme = {
            'primary': '#1f77b4',
            'secondary': '#ff7f0e',
            'success': '#2ca02c',
            'danger': '#d62728',
            'warning': '#ff9900',
            'info': '#17a2b8'
        }
        
    def create_revenue_trend_chart(self, df: pd.DataFrame) -> go.Figure:
        """Create revenue trend visualization"""
        df = df.copy()
        df['date'] = pd.to_datetime(df['date'])
        
        # Aggregate by date
        daily_metrics = df.groupby('date').agg({
            'revenue': 'sum',
            'costs': 'sum',
            'profit': 'sum'
        }).reset_index()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=daily_metrics['date'],
            y=daily_metrics['revenue'],
            name='Revenue',
            line=dict(color=self.color_scheme['primary'], width=3),
            fill='tonexty',
            fillcolor='rgba(31, 119, 180, 0.2)'
        ))
        
        fig.add_trace(go.Scatter(
            x=daily_metrics['date'],
            y=daily_metrics['costs'],
            name='Costs',
            line=dict(color=self.color_scheme['danger'], width=2, dash='dash')
        ))
        
        fig.add_trace(go.Scatter(
            x=daily_metrics['date'],
            y=daily_metrics['profit'],
            name='Profit',
            line=dict(color=self.color_scheme['success'], width=3)
        ))
        
        fig.update_layout(
            title='Revenue, Costs, and Profit Trends',
            xaxis_title='Date',
            yaxis_title='Amount ($)',
            hovermode='x unified',
            template='plotly_white',
            height=400
        )
        
        return fig
    
    def create_performance_gauges(self, health_metrics: Dict[str, Any]) -> go.Figure:
        """Create performance gauge charts"""
        fig = make_subplots(
            rows=1, cols=3,
            specs=[[{'type': 'indicator'}, {'type': 'indicator'}, {'type': 'indicator'}]],
            subplot_titles=('Health Score', 'Profit Margin', 'Customer Satisfaction')
        )
        
        # Health Score Gauge
        fig.add_trace(go.Indicator(
            mode="gauge+number+delta",
            value=health_metrics.get('health_score', 0),
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Health Score"},
            delta={'reference': 80},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': self.color_scheme['primary']},
                'steps': [
                    {'range': [0, 50], 'color': "lightgray"},
                    {'range': [50, 70], 'color': "gray"},
                    {'range': [70, 100], 'color': "lightgreen"}
                ],
                'threshold': {
                    'line': {'color': "red", 'width': 4},
                    'thickness': 0.75,
                    'value': 90
                }
            }
        ), row=1, col=1)
        
        # Profit Margin Gauge
        profit_margin_pct = health_metrics.get('profit_margin', 0) * 100
        fig.add_trace(go.Indicator(
            mode="gauge+number+delta",
            value=profit_margin_pct,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Profit Margin %"},
            delta={'reference': 15},
            gauge={
                'axis': {'range': [None, 30]},
                'bar': {'color': self.color_scheme['success']},
                'steps': [
                    {'range': [0, 10], 'color': "lightgray"},
                    {'range': [10, 20], 'color': "gray"}
                ]
            }
        ), row=1, col=2)
        
        # Customer Satisfaction Gauge
        csat = health_metrics.get('avg_customer_satisfaction', 0)
        fig.add_trace(go.Indicator(
            mode="gauge+number+delta",
            value=csat,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Customer Satisfaction"},
            delta={'reference': 4.5},
            gauge={
                'axis': {'range': [None, 5]},
                'bar': {'color': self.color_scheme['warning']},
                'steps': [
                    {'range': [0, 3.5], 'color': "lightgray"},
                    {'range': [3.5, 4.5], 'color': "gray"}
                ]
            }
        ), row=1, col=3)
        
        fig.update_layout(height=300)
        
        return fig
    
    def create_regional_analysis(self, df: pd.DataFrame) -> go.Figure:
        """Create regional performance analysis"""
        regional_data = df.groupby('region').agg({
            'revenue': 'sum',
            'profit': 'sum',
            'units_sold': 'sum'
        }).reset_index()
        
        regional_data['profit_margin'] = regional_data['profit'] / regional_data['revenue']
        
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'bar'}, {'type': 'pie'}]],
            subplot_titles=('Regional Revenue & Profit', 'Revenue Distribution')
        )
        
        # Bar chart
        fig.add_trace(go.Bar(
            x=regional_data['region'],
            y=regional_data['revenue'],
            name='Revenue',
            marker_color=self.color_scheme['primary']
        ), row=1, col=1)
        
        fig.add_trace(go.Bar(
            x=regional_data['region'],
            y=regional_data['profit'],
            name='Profit',
            marker_color=self.color_scheme['success']
        ), row=1, col=1)
        
        # Pie chart
        fig.add_trace(go.Pie(
            labels=regional_data['region'],
            values=regional_data['revenue'],
            marker=dict(colors=[self.color_scheme['primary'], self.color_scheme['secondary'], 
                               self.color_scheme['success'], self.color_scheme['warning']])
        ), row=1, col=2)
        
        fig.update_layout(height=400, showlegend=True, template='plotly_white')
        
        return fig
    
    def create_product_analysis(self, df: pd.DataFrame) -> go.Figure:
        """Create product category analysis"""
        product_data = df.groupby('product_category').agg({
            'revenue': 'sum',
            'profit': 'sum',
            'units_sold': 'sum',
            'customer_satisfaction': 'mean'
        }).reset_index()
        
        fig = make_subplots(
            rows=2, cols=2,
            specs=[
                [{'type': 'bar'}, {'type': 'scatter'}],
                [{'type': 'bar'}, {'type': 'bar'}]
            ],
            subplot_titles=(
                'Revenue by Product',
                'Profit vs Customer Satisfaction',
                'Units Sold by Product',
                'Profit Margin by Product'
            )
        )
        
        # Revenue by product
        fig.add_trace(go.Bar(
            x=product_data['product_category'],
            y=product_data['revenue'],
            marker_color=self.color_scheme['primary'],
            name='Revenue'
        ), row=1, col=1)
        
        # Profit vs Customer Satisfaction scatter
        fig.add_trace(go.Scatter(
            x=product_data['customer_satisfaction'],
            y=product_data['profit'],
            mode='markers+text',
            text=product_data['product_category'],
            textposition='top center',
            marker=dict(size=15, color=self.color_scheme['success']),
            name='Products'
        ), row=1, col=2)
        
        # Units sold
        fig.add_trace(go.Bar(
            x=product_data['product_category'],
            y=product_data['units_sold'],
            marker_color=self.color_scheme['secondary'],
            name='Units Sold'
        ), row=2, col=1)
        
        # Profit margin
        product_data['margin'] = product_data['profit'] / product_data['revenue']
        fig.add_trace(go.Bar(
            x=product_data['product_category'],
            y=product_data['margin'] * 100,
            marker_color=self.color_scheme['success'],
            name='Profit Margin %'
        ), row=2, col=2)
        
        fig.update_layout(height=600, showlegend=False, template='plotly_white')
        
        return fig
    
    def create_forecast_chart(self, historical_data: List[float], 
                            forecast_data: List[float],
                            dates: List[str] = None) -> go.Figure:
        """Create forecast visualization"""
        if dates is None:
            dates = list(range(len(historical_data) + len(forecast_data)))
        
        fig = go.Figure()
        
        # Historical data
        hist_dates = dates[:len(historical_data)]
        fig.add_trace(go.Scatter(
            x=hist_dates,
            y=historical_data,
            name='Historical',
            line=dict(color=self.color_scheme['primary'], width=3),
            mode='lines+markers'
        ))
        
        # Forecast data
        forecast_dates = dates[len(historical_data)-1:len(historical_data)+len(forecast_data)]
        forecast_values = [historical_data[-1]] + forecast_data
        
        fig.add_trace(go.Scatter(
            x=forecast_dates,
            y=forecast_values,
            name='Forecast',
            line=dict(color=self.color_scheme['danger'], width=3, dash='dash'),
            mode='lines+markers'
        ))
        
        # Add confidence interval
        upper_bound = [val * 1.1 for val in forecast_values]
        lower_bound = [val * 0.9 for val in forecast_values]
        
        fig.add_trace(go.Scatter(
            x=forecast_dates + forecast_dates[::-1],
            y=upper_bound + lower_bound[::-1],
            fill='toself',
            fillcolor='rgba(214, 39, 40, 0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            showlegend=True,
            name='Confidence Interval'
        ))
        
        fig.update_layout(
            title='Revenue Forecast with Confidence Interval',
            xaxis_title='Period',
            yaxis_title='Revenue ($)',
            hovermode='x unified',
            template='plotly_white',
            height=400
        )
        
        return fig
    
    def create_risk_heatmap(self, risks_df: pd.DataFrame) -> go.Figure:
        """Create risk assessment heatmap"""
        # Create risk matrix
        risk_matrix = risks_df.pivot_table(
            values='impact_score',
            index='severity',
            columns='risk_category',
            aggfunc='count',
            fill_value=0
        )
        
        fig = go.Figure(data=go.Heatmap(
            z=risk_matrix.values,
            x=risk_matrix.columns,
            y=risk_matrix.index,
            colorscale='Reds',
            text=risk_matrix.values,
            texttemplate='%{text}',
            textfont={"size": 14},
            hoverongaps=False
        ))
        
        fig.update_layout(
            title='Risk Assessment Heatmap',
            xaxis_title='Risk Category',
            yaxis_title='Severity',
            height=400,
            template='plotly_white'
        )
        
        return fig
    
    def create_scenario_comparison(self, scenario_results: List[Dict[str, Any]]) -> go.Figure:
        """Create scenario comparison chart"""
        scenarios = [s['scenario_name'] for s in scenario_results]
        profits = [s['scenario_profit'] for s in scenario_results]
        revenues = [s['scenario_revenue'] for s in scenario_results]
        margins = [s['scenario_margin'] * 100 for s in scenario_results]
        
        fig = make_subplots(
            rows=1, cols=2,
            specs=[[{'type': 'bar'}, {'type': 'bar'}]],
            subplot_titles=('Profit Comparison', 'Profit Margin Comparison')
        )
        
        # Profit comparison
        colors = [self.color_scheme['success'] if p > 0 else self.color_scheme['danger'] 
                 for p in [s['profit_change_pct'] for s in scenario_results]]
        
        fig.add_trace(go.Bar(
            x=scenarios,
            y=profits,
            marker_color=colors,
            name='Profit'
        ), row=1, col=1)
        
        # Margin comparison
        fig.add_trace(go.Bar(
            x=scenarios,
            y=margins,
            marker_color=self.color_scheme['warning'],
            name='Margin %'
        ), row=1, col=2)
        
        fig.update_layout(
            height=400,
            showlegend=False,
            template='plotly_white'
        )
        
        return fig

    def create_kpi_trends(self, kpi_df: pd.DataFrame) -> go.Figure:
        """Create KPI trend dashboard"""
        df = kpi_df.copy()
        df['date'] = pd.to_datetime(df['date'])

        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=(
                'Net Promoter Score (NPS)',
                'Churn Rate',
                'Pipeline Value',
                'Employee Engagement'
            )
        )

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['nps'],
            mode='lines+markers',
            line=dict(color=self.color_scheme['primary'], width=3),
            name='NPS'
        ), row=1, col=1)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['churn_rate'] * 100,
            mode='lines+markers',
            line=dict(color=self.color_scheme['danger'], width=3),
            name='Churn %'
        ), row=1, col=2)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['pipeline_value'],
            mode='lines+markers',
            line=dict(color=self.color_scheme['success'], width=3),
            name='Pipeline'
        ), row=2, col=1)

        fig.add_trace(go.Scatter(
            x=df['date'],
            y=df['employee_engagement'],
            mode='lines+markers',
            line=dict(color=self.color_scheme['warning'], width=3),
            name='Engagement'
        ), row=2, col=2)

        fig.update_layout(height=600, showlegend=False, template='plotly_white')

        return fig


if __name__ == "__main__":
    # Test the dashboard
    dashboard = BusinessDashboard()
    
    # Load sample data
    df = pd.read_csv('data/sample_sales.csv')
    risks_df = pd.read_csv('data/sample_risks.csv')
    
    # Test charts
    print("Creating revenue trend chart...")
    fig1 = dashboard.create_revenue_trend_chart(df)
    fig1.show()
    
    print("Creating regional analysis...")
    fig2 = dashboard.create_regional_analysis(df)
    fig2.show()
    
    print("Creating product analysis...")
    fig3 = dashboard.create_product_analysis(df)
    fig3.show()
    
    print("Creating risk heatmap...")
    fig4 = dashboard.create_risk_heatmap(risks_df)
    fig4.show()
