"""
Constants Module

Defines constant values used throughout the application.
"""

# ========================
# Market Constants
# ========================
NSE_INDICES = ['NIFTY50', 'NIFTY100', 'NIFTYNXT50', 'NIFTYIT', 'NIFTYPHARMA']
BSE_INDICES = ['SENSEX', 'SENSEX50', 'BSE100']

# Trading hours (IST)
MARKET_OPEN_TIME = "09:15"  # 9:15 AM
MARKET_CLOSE_TIME = "15:30"  # 3:30 PM

# ========================
# Trading Constants
# ========================
PAPER_TRADING_INITIAL_BALANCE = 1000000  # 10 lakh rupees
COMMISSION_PERCENTAGE = 0.05  # 0.05% per trade

ORDER_TYPES = ["LIMIT", "MARKET", "STOP", "STOP_LIMIT"]
ORDER_SIDES = ["BUY", "SELL"]

# ========================
# Validation Constants
# ========================
MIN_PASSWORD_LENGTH = 8
MAX_PASSWORD_LENGTH = 128
VALID_EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# ========================
# Time Constants
# ========================
TIMEFRAMES = {
    '1m': 'One Minute',
    '5m': 'Five Minutes',
    '15m': 'Fifteen Minutes',
    '1h': 'One Hour',
    '1d': 'One Day',
    '1w': 'One Week',
    '1mo': 'One Month',
}

# ========================
# Currency Constants
# ========================
DEFAULT_CURRENCY = 'INR'
CURRENCY_SYMBOLS = {
    'INR': '₹',
    'USD': '$',
    'EUR': '€',
}

# ========================
# Status Constants
# ========================
TRANSACTION_STATUSES = ['PENDING', 'COMPLETED', 'FAILED', 'CANCELLED']
ORDER_STATUSES = ['PENDING', 'OPEN', 'FILLED', 'PARTIALLY_FILLED', 'CANCELLED']
