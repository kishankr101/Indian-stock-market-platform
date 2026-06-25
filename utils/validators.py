"""
Validators Module

Data validation functions for user inputs and data integrity.
"""

import re
from utils.constants import VALID_EMAIL_REGEX, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH


def validate_email(email):
    """
    Validate email address format.
    
    Args:
        email: Email address to validate
    
    Returns:
        Boolean indicating if email is valid
    """
    return re.match(VALID_EMAIL_REGEX, email) is not None


def validate_password(password):
    """
    Validate password strength.
    
    Args:
        password: Password to validate
    
    Returns:
        Boolean indicating if password is valid
    """
    if len(password) < MIN_PASSWORD_LENGTH or len(password) > MAX_PASSWORD_LENGTH:
        return False
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return False
    
    return True


def validate_stock_symbol(symbol):
    """
    Validate stock symbol format.
    
    Args:
        symbol: Stock symbol to validate
    
    Returns:
        Boolean indicating if symbol is valid
    """
    # Stock symbols should be alphanumeric and 1-10 characters
    return re.match(r'^[A-Z0-9]{1,10}$', symbol.upper()) is not None


def validate_quantity(quantity):
    """
    Validate quantity for trading.
    
    Args:
        quantity: Quantity to validate
    
    Returns:
        Boolean indicating if quantity is valid
    """
    try:
        qty = float(quantity)
        return qty > 0
    except (ValueError, TypeError):
        return False


def validate_price(price):
    """
    Validate price for trading.
    
    Args:
        price: Price to validate
    
    Returns:
        Boolean indicating if price is valid
    """
    try:
        prc = float(price)
        return prc >= 0
    except (ValueError, TypeError):
        return False
