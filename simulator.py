"""
Simulator Module - Scenario Simulation and What-If Analysis
Enables business scenario modeling and impact analysis
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Any, Tuple
import copy


class BusinessSimulator:
    """Advanced scenario simulation engine"""
    
    def __init__(self):
        self.base_scenario = None
        self.scenarios = {}
        
    def set_base_scenario(self, df: pd.DataFrame):
        """Set the base scenario for comparison"""
        self.base_scenario = df.copy()
        
    def simulate_price_change(self, df: pd.DataFrame, price_change_pct: float) -> pd.DataFrame:
        """Simulate impact of price changes"""
        df = df.copy()
        
        # Assume price change affects revenue
        df['revenue'] = df['revenue'] * (1 + price_change_pct / 100)
        
        # Assume some demand elasticity (-0.5 means 1% price increase = 0.5% demand decrease)
        elasticity = -0.5
        demand_change = price_change_pct * elasticity / 100
        df['units_sold'] = df['units_sold'] * (1 + demand_change)
        
        # Recalculate profit
        df['profit'] = df['revenue'] - df['costs']
        
        return df
    
    def simulate_cost_change(self, df: pd.DataFrame, cost_change_pct: float) -> pd.DataFrame:
        """Simulate impact of cost changes"""
        df = df.copy()
        
        # Change costs
        df['costs'] = df['costs'] * (1 + cost_change_pct / 100)
        
        # Recalculate profit
        df['profit'] = df['revenue'] - df['costs']
        
        return df
    
    def simulate_volume_change(self, df: pd.DataFrame, volume_change_pct: float) -> pd.DataFrame:
        """Simulate impact of sales volume changes"""
        df = df.copy()
        
        # Change units and revenue proportionally
        multiplier = (1 + volume_change_pct / 100)
        df['units_sold'] = df['units_sold'] * multiplier
        df['revenue'] = df['revenue'] * multiplier
        df['costs'] = df['costs'] * multiplier  # Variable costs scale with volume
        
        # Recalculate profit
        df['profit'] = df['revenue'] - df['costs']
        
        return df
    
    def simulate_market_expansion(self, df: pd.DataFrame, new_regions: int = 1) -> pd.DataFrame:
        """Simulate expansion into new markets"""
        df = df.copy()
        
        # Increase revenue and costs proportionally
        expansion_multiplier = 1 + (new_regions * 0.3)  # 30% increase per new region
        df['revenue'] = df['revenue'] * expansion_multiplier
        df['costs'] = df['costs'] * expansion_multiplier * 1.1  # Higher costs for expansion
        df['units_sold'] = df['units_sold'] * expansion_multiplier
        
        # Recalculate profit
        df['profit'] = df['revenue'] - df['costs']
        
        return df
    
    def simulate_efficiency_improvement(self, df: pd.DataFrame, efficiency_gain_pct: float) -> pd.DataFrame:
        """Simulate operational efficiency improvements"""
        df = df.copy()
        
        # Reduce costs while maintaining revenue
        df['costs'] = df['costs'] * (1 - efficiency_gain_pct / 100)
        
        # Recalculate profit
        df['profit'] = df['revenue'] - df['costs']
        
        return df
    
    def simulate_custom_scenario(self, df: pd.DataFrame, 
                                 price_change: float = 0,
                                 cost_change: float = 0,
                                 volume_change: float = 0,
                                 efficiency_gain: float = 0) -> pd.DataFrame:
        """Simulate a custom scenario with multiple factors"""
        df = df.copy()
        
        # Apply changes in sequence
        if price_change != 0:
            df = self.simulate_price_change(df, price_change)
        
        if volume_change != 0:
            df = self.simulate_volume_change(df, volume_change)
        
        if efficiency_gain != 0:
            df = self.simulate_efficiency_improvement(df, efficiency_gain)
        
        if cost_change != 0:
            df = self.simulate_cost_change(df, cost_change)
        
        return df
    
    def compare_scenarios(self, base_df: pd.DataFrame, scenario_df: pd.DataFrame, 
                         scenario_name: str) -> Dict[str, Any]:
        """Compare scenario results with base scenario"""
        base_revenue = base_df['revenue'].sum()
        base_profit = base_df['profit'].sum()
        base_margin = base_profit / base_revenue if base_revenue > 0 else 0
        
        scenario_revenue = scenario_df['revenue'].sum()
        scenario_profit = scenario_df['profit'].sum()
        scenario_margin = scenario_profit / scenario_revenue if scenario_revenue > 0 else 0
        
        revenue_change = ((scenario_revenue - base_revenue) / base_revenue * 100) if base_revenue > 0 else 0
        profit_change = ((scenario_profit - base_profit) / base_profit * 100) if base_profit > 0 else 0
        margin_change = ((scenario_margin - base_margin) / base_margin * 100) if base_margin > 0 else 0
        
        return {
            'scenario_name': scenario_name,
            'base_revenue': float(base_revenue),
            'scenario_revenue': float(scenario_revenue),
            'revenue_change_pct': float(revenue_change),
            'base_profit': float(base_profit),
            'scenario_profit': float(scenario_profit),
            'profit_change_pct': float(profit_change),
            'base_margin': float(base_margin),
            'scenario_margin': float(scenario_margin),
            'margin_change_pct': float(margin_change),
            'recommendation': self._get_scenario_recommendation(profit_change, margin_change)
        }
    
    def _get_scenario_recommendation(self, profit_change: float, margin_change: float) -> str:
        """Get recommendation based on scenario results"""
        if profit_change > 10 and margin_change > 5:
            return "✅ Highly Recommended - Significant profit and margin improvement"
        elif profit_change > 5:
            return "👍 Recommended - Positive profit impact"
        elif profit_change > 0:
            return "⚠️ Consider - Modest improvement"
        elif profit_change > -5:
            return "⚠️ Caution - Minimal negative impact"
        else:
            return "❌ Not Recommended - Significant negative impact"
    
    def run_monte_carlo_simulation(self, df: pd.DataFrame, 
                                   iterations: int = 1000,
                                   revenue_volatility: float = 0.1,
                                   cost_volatility: float = 0.05) -> Dict[str, Any]:
        """Run Monte Carlo simulation for risk analysis"""
        results = []
        
        base_revenue = df['revenue'].sum()
        base_costs = df['costs'].sum()
        
        for _ in range(iterations):
            # Generate random variations
            revenue_factor = np.random.normal(1.0, revenue_volatility)
            cost_factor = np.random.normal(1.0, cost_volatility)
            
            simulated_revenue = base_revenue * revenue_factor
            simulated_costs = base_costs * cost_factor
            simulated_profit = simulated_revenue - simulated_costs
            
            results.append({
                'revenue': simulated_revenue,
                'costs': simulated_costs,
                'profit': simulated_profit,
                'margin': simulated_profit / simulated_revenue if simulated_revenue > 0 else 0
            })
        
        results_df = pd.DataFrame(results)
        
        # Calculate Value at Risk properly using profit
        base_profit = df['profit'].sum()
        profit_var = float(results_df['profit'].quantile(0.05) - base_profit)  # 5% worst case loss
        
        return {
            'iterations': iterations,
            'mean_revenue': float(results_df['revenue'].mean()),
            'std_revenue': float(results_df['revenue'].std()),
            'mean_profit': float(results_df['profit'].mean()),
            'std_profit': float(results_df['profit'].std()),
            'profit_5th_percentile': float(results_df['profit'].quantile(0.05)),
            'profit_95th_percentile': float(results_df['profit'].quantile(0.95)),
            'probability_profitable': float((results_df['profit'] > 0).mean()),
            'value_at_risk_5pct': float(profit_var)  # 5% VaR - potential profit loss
        }
    
    def sensitivity_analysis(self, df: pd.DataFrame, 
                           parameter: str = 'price',
                           range_pct: Tuple[float, float] = (-20, 20),
                           steps: int = 9) -> List[Dict[str, Any]]:
        """Perform sensitivity analysis on a parameter"""
        results = []
        
        parameter_values = np.linspace(range_pct[0], range_pct[1], steps)
        
        for value in parameter_values:
            if parameter == 'price':
                scenario_df = self.simulate_price_change(df, value)
            elif parameter == 'cost':
                scenario_df = self.simulate_cost_change(df, value)
            elif parameter == 'volume':
                scenario_df = self.simulate_volume_change(df, value)
            elif parameter == 'efficiency':
                scenario_df = self.simulate_efficiency_improvement(df, abs(value))
            else:
                continue
            
            profit = scenario_df['profit'].sum()
            revenue = scenario_df['revenue'].sum()
            margin = profit / revenue if revenue > 0 else 0
            
            results.append({
                'parameter_value': float(value),
                'profit': float(profit),
                'revenue': float(revenue),
                'margin': float(margin)
            })
        
        return results
    
    def generate_scenario_report(self, comparisons: List[Dict[str, Any]]) -> str:
        """Generate a formatted scenario analysis report"""
        report = """
╔════════════════════════════════════════════════════════════════╗
║             SCENARIO ANALYSIS REPORT                           ║
╚════════════════════════════════════════════════════════════════╝

"""
        for comp in comparisons:
            report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 {comp['scenario_name']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Revenue Impact:
  Base: ${comp['base_revenue']:,.0f}
  Scenario: ${comp['scenario_revenue']:,.0f}
  Change: {comp['revenue_change_pct']:+.1f}%

Profit Impact:
  Base: ${comp['base_profit']:,.0f}
  Scenario: ${comp['scenario_profit']:,.0f}
  Change: {comp['profit_change_pct']:+.1f}%

Margin:
  Base: {comp['base_margin']:.1%}
  Scenario: {comp['scenario_margin']:.1%}
  Change: {comp['margin_change_pct']:+.1f}%

{comp['recommendation']}
"""
        
        return report


if __name__ == "__main__":
    # Test the simulator
    simulator = BusinessSimulator()
    
    # Load sample data
    df = pd.read_csv('data/sample_sales.csv')
    simulator.set_base_scenario(df)
    
    # Test scenarios
    print("Running scenario simulations...\n")
    
    # Scenario 1: Price increase
    scenario1 = simulator.simulate_price_change(df, 10)
    comp1 = simulator.compare_scenarios(df, scenario1, "10% Price Increase")
    
    # Scenario 2: Cost reduction
    scenario2 = simulator.simulate_cost_change(df, -5)
    comp2 = simulator.compare_scenarios(df, scenario2, "5% Cost Reduction")
    
    # Scenario 3: Volume increase
    scenario3 = simulator.simulate_volume_change(df, 15)
    comp3 = simulator.compare_scenarios(df, scenario3, "15% Volume Increase")
    
    # Scenario 4: Market expansion
    scenario4 = simulator.simulate_market_expansion(df, 2)
    comp4 = simulator.compare_scenarios(df, scenario4, "Expand to 2 New Regions")
    
    # Generate report
    report = simulator.generate_scenario_report([comp1, comp2, comp3, comp4])
    print(report)
    
    # Monte Carlo simulation
    print("\nRunning Monte Carlo simulation...")
    mc_results = simulator.run_monte_carlo_simulation(df)
    print(f"Mean Profit: ${mc_results['mean_profit']:,.0f}")
    print(f"Profit Std Dev: ${mc_results['std_profit']:,.0f}")
    print(f"5th Percentile: ${mc_results['profit_5th_percentile']:,.0f}")
    print(f"95th Percentile: ${mc_results['profit_95th_percentile']:,.0f}")
    print(f"Probability Profitable: {mc_results['probability_profitable']:.1%}")
