"""
Advisor Module - AI Business Advisor with LLM
Provides intelligent recommendations and insights
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any
import json


class BusinessAdvisor:
    """AI-powered business advisor for strategic recommendations"""
    
    def __init__(self):
        self.knowledge_base = self._initialize_knowledge_base()
    
    def _initialize_knowledge_base(self) -> Dict[str, Any]:
        """Initialize business knowledge base"""
        return {
            'revenue_growth_strategies': [
                'Expand into new markets',
                'Increase pricing strategically',
                'Improve customer retention',
                'Cross-sell and upsell products',
                'Enhance digital marketing efforts',
                'Develop new product lines'
            ],
            'cost_reduction_strategies': [
                'Optimize supply chain',
                'Automate manual processes',
                'Renegotiate supplier contracts',
                'Reduce operational overhead',
                'Implement energy efficiency measures',
                'Consolidate vendors'
            ],
            'risk_mitigation_actions': {
                'Financial': ['Diversify revenue streams', 'Build cash reserves', 'Hedge currency exposure'],
                'Operational': ['Cross-train staff', 'Diversify suppliers', 'Implement backup systems'],
                'Strategic': ['Conduct market research', 'Monitor competitor activity', 'Innovate continuously'],
                'Compliance': ['Stay updated on regulations', 'Conduct regular audits', 'Implement compliance training'],
                'Technology': ['Update security systems', 'Backup data regularly', 'Invest in cybersecurity']
            },
            'performance_benchmarks': {
                'profit_margin': {'excellent': 0.20, 'good': 0.15, 'average': 0.10, 'poor': 0.05},
                'revenue_growth': {'excellent': 0.25, 'good': 0.15, 'average': 0.08, 'poor': 0.02},
                'customer_satisfaction': {'excellent': 4.8, 'good': 4.5, 'average': 4.0, 'poor': 3.5}
            }
        }
    
    def analyze_business_health(self, df: pd.DataFrame) -> Dict[str, Any]:
        """Comprehensive business health analysis"""
        # Calculate key metrics
        total_revenue = df['revenue'].sum()
        total_costs = df['costs'].sum()
        total_profit = df['profit'].sum()
        
        profit_margin = total_profit / total_revenue if total_revenue > 0 else 0
        avg_customer_satisfaction = df['customer_satisfaction'].mean()
        
        # Calculate growth rate
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        first_week = df.head(7)['revenue'].sum()
        last_week = df.tail(7)['revenue'].sum()
        revenue_growth = (last_week - first_week) / first_week if first_week > 0 else 0
        
        # Performance ratings
        margin_rating = self._rate_metric(profit_margin, 'profit_margin')
        growth_rating = self._rate_metric(revenue_growth, 'revenue_growth')
        satisfaction_rating = self._rate_metric(avg_customer_satisfaction, 'customer_satisfaction')
        
        # Overall health score (0-100)
        health_score = (
            margin_rating['score'] * 0.4 +
            growth_rating['score'] * 0.3 +
            satisfaction_rating['score'] * 0.3
        )
        
        return {
            'total_revenue': float(total_revenue),
            'total_profit': float(total_profit),
            'profit_margin': float(profit_margin),
            'revenue_growth_rate': float(revenue_growth),
            'avg_customer_satisfaction': float(avg_customer_satisfaction),
            'health_score': float(health_score),
            'margin_rating': margin_rating,
            'growth_rating': growth_rating,
            'satisfaction_rating': satisfaction_rating,
            'overall_status': self._get_health_status(health_score)
        }
    
    def _rate_metric(self, value: float, metric_type: str) -> Dict[str, Any]:
        """Rate a metric against benchmarks"""
        benchmarks = self.knowledge_base['performance_benchmarks'].get(metric_type, {})
        
        if value >= benchmarks.get('excellent', float('inf')):
            rating = 'Excellent'
            score = 100
        elif value >= benchmarks.get('good', float('inf')):
            rating = 'Good'
            score = 80
        elif value >= benchmarks.get('average', float('inf')):
            rating = 'Average'
            score = 60
        elif value >= benchmarks.get('poor', float('inf')):
            rating = 'Poor'
            score = 40
        else:
            rating = 'Critical'
            score = 20
        
        return {
            'value': value,
            'rating': rating,
            'score': score
        }
    
    def _get_health_status(self, score: float) -> str:
        """Get overall health status"""
        if score >= 85:
            return 'Excellent'
        elif score >= 70:
            return 'Good'
        elif score >= 50:
            return 'Fair'
        else:
            return 'Needs Attention'
    
    def get_strategic_recommendations(self, health_analysis: Dict[str, Any]) -> List[str]:
        """Generate strategic recommendations based on health analysis"""
        recommendations = []
        
        # Profit margin recommendations
        if health_analysis['margin_rating']['score'] < 70:
            recommendations.append('🎯 PRIORITY: Improve profit margins through cost optimization')
            recommendations.extend([f"   • {strategy}" for strategy in self.knowledge_base['cost_reduction_strategies'][:3]])
        
        # Revenue growth recommendations
        if health_analysis['growth_rating']['score'] < 70:
            recommendations.append('📈 Focus on accelerating revenue growth')
            recommendations.extend([f"   • {strategy}" for strategy in self.knowledge_base['revenue_growth_strategies'][:3]])
        
        # Customer satisfaction recommendations
        if health_analysis['satisfaction_rating']['score'] < 70:
            recommendations.append('⭐ Enhance customer satisfaction and retention')
            recommendations.append('   • Implement customer feedback program')
            recommendations.append('   • Improve product/service quality')
            recommendations.append('   • Enhance customer support')
        
        # Overall performance
        if health_analysis['health_score'] >= 85:
            recommendations.append('✅ Maintain excellent performance and explore expansion opportunities')
        elif health_analysis['health_score'] < 50:
            recommendations.append('⚠️ URGENT: Address critical business health issues immediately')
        
        return recommendations
    
    def analyze_risks(self, risks_df: pd.DataFrame) -> Dict[str, Any]:
        """Analyze risk portfolio"""
        # Calculate risk metrics
        high_risk_count = len(risks_df[risks_df['severity'] == 'High'])
        avg_impact = risks_df['impact_score'].mean()
        avg_probability = risks_df['probability'].mean()
        
        # Risk categories distribution
        category_distribution = risks_df['risk_category'].value_counts().to_dict()
        
        # Priority risks (High severity and probability > 0.5)
        priority_risks = risks_df[
            (risks_df['severity'] == 'High') & 
            (risks_df['probability'] > 0.5)
        ]
        
        return {
            'total_risks': len(risks_df),
            'high_risk_count': high_risk_count,
            'avg_impact_score': float(avg_impact),
            'avg_probability': float(avg_probability),
            'category_distribution': category_distribution,
            'priority_risks': priority_risks.to_dict('records'),
            'risk_score': float(avg_impact * avg_probability * 10)
        }
    
    def get_risk_recommendations(self, risk_analysis: Dict[str, Any]) -> List[str]:
        """Generate risk mitigation recommendations"""
        recommendations = []
        
        if risk_analysis['risk_score'] > 50:
            recommendations.append('🚨 HIGH RISK ALERT: Immediate action required')
        
        # Recommendations for priority risks
        for risk in risk_analysis['priority_risks']:
            category = risk['risk_category']
            recommendations.append(f"\n📋 {risk['description']}")
            
            mitigation_actions = self.knowledge_base['risk_mitigation_actions'].get(category, [])
            for action in mitigation_actions:
                recommendations.append(f"   • {action}")
        
        # Overall risk management
        if risk_analysis['high_risk_count'] > 3:
            recommendations.append('\n🛡️ Implement comprehensive risk management framework')
            recommendations.append('   • Establish risk monitoring system')
            recommendations.append('   • Create risk response team')
            recommendations.append('   • Develop contingency plans')
        
        return recommendations
    
    def generate_executive_summary(self, health_analysis: Dict[str, Any], 
                                   risk_analysis: Dict[str, Any],
                                   forecast_trend: str = 'Positive') -> str:
        """Generate executive summary report"""
        summary = f"""
╔════════════════════════════════════════════════════════════════╗
║           DECISIONPILOT AI - EXECUTIVE SUMMARY                 ║
╚════════════════════════════════════════════════════════════════╝

📊 BUSINESS HEALTH OVERVIEW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Health Score: {health_analysis['health_score']:.1f}/100 ({health_analysis['overall_status']})
Revenue: ${health_analysis['total_revenue']:,.0f}
Profit: ${health_analysis['total_profit']:,.0f}
Profit Margin: {health_analysis['profit_margin']:.1%} ({health_analysis['margin_rating']['rating']})
Revenue Growth: {health_analysis['revenue_growth_rate']:.1%} ({health_analysis['growth_rating']['rating']})
Customer Satisfaction: {health_analysis['avg_customer_satisfaction']:.2f}/5.0 ({health_analysis['satisfaction_rating']['rating']})

🎯 RISK ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Risk Score: {risk_analysis['risk_score']:.1f}/100
Total Risks: {risk_analysis['total_risks']}
High Priority Risks: {risk_analysis['high_risk_count']}
Average Impact: {risk_analysis['avg_impact_score']:.1f}/10

📈 FORECAST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Trend: {forecast_trend}
Outlook: {"Favorable growth expected" if forecast_trend == "Positive" else "Caution advised"}

🔥 KEY RECOMMENDATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
        
        # Add strategic recommendations
        strategic_recs = self.get_strategic_recommendations(health_analysis)
        for i, rec in enumerate(strategic_recs[:5], 1):
            summary += f"{rec}\n"
        
        summary += "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
        summary += "Generated by DecisionPilot AI - Enterprise Decision Intelligence\n"
        
        return summary


if __name__ == "__main__":
    # Test the advisor
    advisor = BusinessAdvisor()
    
    # Load sample data
    sales_df = pd.read_csv('data/sample_sales.csv')
    risks_df = pd.read_csv('data/sample_risks.csv')
    
    # Analyze business health
    print("Analyzing business health...")
    health_analysis = advisor.analyze_business_health(sales_df)
    print(json.dumps(health_analysis, indent=2))
    
    # Get recommendations
    print("\nStrategic Recommendations:")
    recommendations = advisor.get_strategic_recommendations(health_analysis)
    for rec in recommendations:
        print(rec)
    
    # Analyze risks
    print("\nAnalyzing risks...")
    risk_analysis = advisor.analyze_risks(risks_df)
    print(json.dumps(risk_analysis, indent=2))
    
    # Generate executive summary
    print("\n" + "="*70)
    summary = advisor.generate_executive_summary(health_analysis, risk_analysis)
    print(summary)
