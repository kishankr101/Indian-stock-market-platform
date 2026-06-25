"""
Configuration Module
"""

import os
from dotenv import load_dotenv

load_dotenv()

APP_CONFIG = {
    'APP_NAME': 'Indian Stock Market Platform',
    'APP_ICON': '📈',
    'LAYOUT': 'wide',
    'SIDEBAR_STATE': 'expanded',
    'THEME': 'light',
}

DB_CONFIG = {
    'ENGINE': os.getenv('DB_ENGINE', 'sqlite'),
    'SQLITE_PATH': os.getenv('SQLITE_PATH', 'data/market_data.db'),
}

API_CONFIG = {
    'MARKET_DATA_API': os.getenv('MARKET_DATA_API', 'yfinance'),
}
