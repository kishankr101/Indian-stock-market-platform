"""
Helpers Module

Utility functions for common operations.
Provides helper functions used throughout the application.
"""

import re
from datetime import datetime
from utils.constants import VALID_EMAIL_REGEX


def format_currency(amount, currency='INR'):
    """
    Format an amount as currency.
    
    Args:
        amount: Amount to format
        currency: Currency code (default: INR)
    
    Returns:
        Formatted currency string
    """
    if currency == 'INR':
        return f"₹{amount:,.2f}"
    elif currency == 'USD':
        return f"${amount:,.2f}"
    elif currency == 'EUR':
        return f"€{amount:,.2f}"
    else:
        return f"{amount:,.2f} {currency}"


def format_percentage(value, decimal_places=2):
    """
    Format a value as a percentage.
    
    Args:
        value: Value to format
        decimal_places: Number of decimal places
    
    Returns:
        Formatted percentage string
    """
    return f"{value:.{decimal_places}f}%"


def format_date(date_obj, format_string="%Y-%m-%d"):
    """
    Format a date object to string.
    
    Args:
        date_obj: Date object to format
        format_string: Format string
    
    Returns:
        Formatted date string
    """
    if isinstance(date_obj, str):
        return date_obj
    return date_obj.strftime(format_string)


def calculate_percentage_change(old_value, new_value):
    """
    Calculate percentage change between two values.
    
    Args:
        old_value: Previous value
        new_value: Current value
    
    Returns:
        Percentage change
    """
    if old_value == 0:
        return 0
    return ((new_value - old_value) / abs(old_value)) * 100


def is_market_open():
    """
    Check if the market is currently open.
    
    Returns:
        Boolean indicating if market is open
    """
    # Implementation will be added
    pass


def round_to_precision(value, precision=2):
    """
    Round a value to a specific precision.
    
    Args:
        value: Value to round
        precision: Number of decimal places
    
    Returns:
        Rounded value
    """
    return round(value, precision)
