"""
Configuration Module

Centralized configuration for the Streamlit application.
Manages environment variables, API keys, and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ========================
# Application Configuration
# ========================
APP_CONFIG = {
    'APP_NAME': 'Indian Stock Market Platform',
    'APP_ICON': '📈',
    'LAYOUT': 'wide',
    'SIDEBAR_STATE': 'expanded',
    'THEME': 'light',
}

# ========================
# Database Configuration
# ========================
DB_CONFIG = {
    'ENGINE': os.getenv('DB_ENGINE', 'sqlite'),  # 'sqlite' or 'postgresql'
    'SQLITE_PATH': os.getenv('SQLITE_PATH', 'data/market_data.db'),
    'POSTGRES_HOST': os.getenv('POSTGRES_HOST', 'localhost'),
    'POSTGRES_PORT': os.getenv('POSTGRES_PORT', 5432),
    'POSTGRES_DB': os.getenv('POSTGRES_DB', 'stock_market'),
    'POSTGRES_USER': os.getenv('POSTGRES_USER', 'postgres'),
    'POSTGRES_PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
}

# ========================
# API Configuration
# ========================
API_CONFIG = {
    'MARKET_DATA_API': os.getenv('MARKET_DATA_API', 'yfinance'),
    'NEWS_API_KEY': os.getenv('NEWS_API_KEY', ''),
    'STOCK_API_ENDPOINT': os.getenv('STOCK_API_ENDPOINT', 'https://api.example.com'),
}

# ========================
# Authentication Configuration
# ========================
AUTH_CONFIG = {
    'ENABLE_AUTH': os.getenv('ENABLE_AUTH', 'false').lower() == 'true',
    'SECRET_KEY': os.getenv('SECRET_KEY', 'your-secret-key-change-in-production'),
    'SESSION_TIMEOUT': int(os.getenv('SESSION_TIMEOUT', 3600)),  # 1 hour in seconds
}

# ========================
# Market Data Configuration
# ========================
MARKET_CONFIG = {
    'NSE_INDEX': ['NIFTY50', 'NIFTY100', 'NIFTYNXT50'],
    'BSE_INDEX': ['SENSEX'],
    'DEFAULT_TIMEFRAME': '1d',  # 1 day
    'SUPPORTED_TIMEFRAMES': ['1m', '5m', '15m', '1h', '1d', '1w', '1mo'],
}

# ========================
# Trading Configuration
# ========================
TRADING_CONFIG = {
    'PAPER_TRADING_ENABLED': True,
    'INITIAL_BALANCE': 1000000,  # 10 lakh rupees
    'COMMISSION_PERCENTAGE': 0.05,  # 0.05% per trade
}

# ========================
# UI Configuration
# ========================
UI_CONFIG = {
    'CHART_HEIGHT': 400,
    'CHART_WIDTH': 800,
    'TABLE_MAX_ROWS': 100,
    'COLORS': {
        'PRIMARY': '#1f77b4',
        'SUCCESS': '#2ca02c',
        'WARNING': '#ff7f0e',
        'DANGER': '#d62728',
        'NEUTRAL': '#7f7f7f',
    },
}

# ========================
# Logging Configuration
# ========================
LOGGING_CONFIG = {
    'LOG_LEVEL': os.getenv('LOG_LEVEL', 'INFO'),
    'LOG_FILE': os.getenv('LOG_FILE', 'logs/app.log'),
    'LOG_FORMAT': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
}

# ========================
# Feature Flags
# ========================
FEATURE_FLAGS = {
    'ENABLE_PAPER_TRADING': True,
    'ENABLE_TECHNICAL_ANALYSIS': True,
    'ENABLE_NEWS_MODULE': True,
    'ENABLE_ADMIN_PANEL': False,
}
