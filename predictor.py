"""
Predictor Module - ML Forecasting with XGBoost and LSTM
Handles time series forecasting and business predictions
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import xgboost as xgb
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
import pickle
import os


class BusinessPredictor:
    """Enterprise-grade forecasting engine"""
    
    def __init__(self):
        self.xgb_model = None
        self.lstm_model = None
        self.scaler = StandardScaler()
        self.models_dir = 'models'
        os.makedirs(self.models_dir, exist_ok=True)
        
    def prepare_data(self, df, target_col='revenue', window_size=7):
        """Prepare time series data for ML models"""
        # Sort by date
        df = df.sort_values('date').reset_index(drop=True)
        
        # Feature engineering
        df['day_of_week'] = pd.to_datetime(df['date']).dt.dayofweek
        df['day_of_month'] = pd.to_datetime(df['date']).dt.day
        df['month'] = pd.to_datetime(df['date']).dt.month
        
        # Create lagged features
        for i in range(1, window_size + 1):
            df[f'lag_{i}'] = df[target_col].shift(i)
        
        # Rolling statistics
        df['rolling_mean_7'] = df[target_col].rolling(window=7, min_periods=1).mean()
        df['rolling_std_7'] = df[target_col].rolling(window=7, min_periods=1).std()
        
        # Drop rows with NaN values from lagged features
        df = df.dropna()
        
        return df
    
    def train_xgboost(self, df, target_col='revenue'):
        """Train XGBoost model for forecasting"""
        # Prepare features
        df = self.prepare_data(df, target_col)
        
        # Select features
        feature_cols = [col for col in df.columns if col not in ['date', target_col, 'region', 'product_category']]
        X = df[feature_cols]
        y = df[target_col]
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        # Train model
        self.xgb_model = xgb.XGBRegressor(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=5,
            random_state=42
        )
        self.xgb_model.fit(X_train, y_train)
        
        # Evaluate
        train_score = self.xgb_model.score(X_train, y_train)
        test_score = self.xgb_model.score(X_test, y_test)
        
        # Save model
        with open(f'{self.models_dir}/xgboost_model.pkl', 'wb') as f:
            pickle.dump(self.xgb_model, f)
        
        return {
            'train_score': train_score,
            'test_score': test_score,
            'predictions': self.xgb_model.predict(X_test),
            'actuals': y_test.values
        }
    
    def create_lstm_sequences(self, data, window_size=7):
        """Create sequences for LSTM training"""
        X, y = [], []
        for i in range(len(data) - window_size):
            X.append(data[i:i + window_size])
            y.append(data[i + window_size])
        return np.array(X), np.array(y)
    
    def train_lstm(self, df, target_col='revenue', window_size=7):
        """Train LSTM model for time series forecasting"""
        # Prepare data
        df = df.sort_values('date').reset_index(drop=True)
        data = df[target_col].values.reshape(-1, 1)
        
        # Scale data
        scaled_data = self.scaler.fit_transform(data)
        
        # Create sequences
        X, y = self.create_lstm_sequences(scaled_data, window_size)
        
        # Reshape for LSTM [samples, time steps, features]
        X = X.reshape((X.shape[0], X.shape[1], 1))
        
        # Split data
        split_idx = int(len(X) * 0.8)
        X_train, X_test = X[:split_idx], X[split_idx:]
        y_train, y_test = y[:split_idx], y[split_idx:]
        
        # Build LSTM model
        self.lstm_model = Sequential([
            LSTM(50, activation='relu', return_sequences=True, input_shape=(window_size, 1)),
            Dropout(0.2),
            LSTM(50, activation='relu'),
            Dropout(0.2),
            Dense(1)
        ])
        
        self.lstm_model.compile(optimizer='adam', loss='mse', metrics=['mae'])
        
        # Train model
        history = self.lstm_model.fit(
            X_train, y_train,
            epochs=50,
            batch_size=16,
            validation_data=(X_test, y_test),
            verbose=0
        )
        
        # Save model
        self.lstm_model.save(f'{self.models_dir}/lstm_model.h5')
        
        # Make predictions
        predictions = self.lstm_model.predict(X_test)
        predictions = self.scaler.inverse_transform(predictions)
        actuals = self.scaler.inverse_transform(y_test)
        
        return {
            'train_loss': history.history['loss'][-1],
            'val_loss': history.history['val_loss'][-1],
            'predictions': predictions.flatten(),
            'actuals': actuals.flatten()
        }
    
    def forecast_next_n_days(self, df, n_days=7, target_col='revenue', method='xgboost'):
        """Forecast next N days using trained model"""
        if method == 'xgboost':
            if self.xgb_model is None:
                self.train_xgboost(df, target_col)
            
            # Prepare last data point
            df_prep = self.prepare_data(df, target_col)
            feature_cols = [col for col in df_prep.columns if col not in ['date', target_col, 'region', 'product_category']]
            last_features = df_prep[feature_cols].iloc[-1:].values
            
            # Make predictions
            forecast = []
            for _ in range(n_days):
                pred = self.xgb_model.predict(last_features)[0]
                forecast.append(pred)
                # Update features for next prediction (simplified)
                last_features = last_features.copy()
            
            return forecast
        
        elif method == 'lstm':
            if self.lstm_model is None:
                self.train_lstm(df, target_col)
            
            # Get last window_size values
            window_size = 7
            data = df[target_col].values[-window_size:].reshape(-1, 1)
            scaled_data = self.scaler.transform(data)
            
            # Make predictions
            forecast = []
            current_sequence = scaled_data.reshape(1, window_size, 1)
            
            for _ in range(n_days):
                pred = self.lstm_model.predict(current_sequence, verbose=0)
                forecast.append(self.scaler.inverse_transform(pred)[0, 0])
                
                # Update sequence
                current_sequence = np.roll(current_sequence, -1, axis=1)
                current_sequence[0, -1, 0] = pred[0, 0]
            
            return forecast
        
        else:
            raise ValueError(f"Unknown method: {method}")
    
    def get_feature_importance(self, df, target_col='revenue'):
        """Get feature importance from XGBoost model"""
        if self.xgb_model is None:
            self.train_xgboost(df, target_col)
        
        df_prep = self.prepare_data(df, target_col)
        feature_cols = [col for col in df_prep.columns if col not in ['date', target_col, 'region', 'product_category']]
        
        importance = self.xgb_model.feature_importances_
        feature_importance = dict(zip(feature_cols, importance))
        
        return sorted(feature_importance.items(), key=lambda x: x[1], reverse=True)


if __name__ == "__main__":
    # Test the predictor
    predictor = BusinessPredictor()
    
    # Load sample data
    df = pd.read_csv('data/sample_sales.csv')
    
    # Test XGBoost
    print("Training XGBoost model...")
    xgb_results = predictor.train_xgboost(df)
    print(f"XGBoost Train R²: {xgb_results['train_score']:.4f}")
    print(f"XGBoost Test R²: {xgb_results['test_score']:.4f}")
    
    # Test LSTM
    print("\nTraining LSTM model...")
    lstm_results = predictor.train_lstm(df)
    print(f"LSTM Val Loss: {lstm_results['val_loss']:.4f}")
    
    # Test forecasting
    print("\nForecasting next 7 days...")
    forecast_xgb = predictor.forecast_next_n_days(df, n_days=7, method='xgboost')
    print(f"XGBoost Forecast: {forecast_xgb}")
    
    forecast_lstm = predictor.forecast_next_n_days(df, n_days=7, method='lstm')
    print(f"LSTM Forecast: {forecast_lstm}")
