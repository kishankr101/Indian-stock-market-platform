"""
Cards Component

Reusable card components for displaying information.
Provides functions for creating styled information cards.
"""

import streamlit as st


def display_metric_card(label, value, delta=None, icon="📊"):
    """
    Display a metric card with label and value.
    
    Args:
        label: Metric label
        value: Metric value
        delta: Change in value (optional)
        icon: Emoji icon for the card
    
    Returns:
        None
    """
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.metric(label=label, value=value, delta=delta)


def display_info_card(title, content, icon="ℹ️"):
    """
    Display an information card.
    
    Args:
        title: Card title
        content: Card content
        icon: Emoji icon for the card
    
    Returns:
        None
    """
    st.info(f"{icon} **{title}**\n{content}")


def display_stock_card(symbol, name, price, change_percent):
    """
    Display a stock information card.
    
    Args:
        symbol: Stock symbol
        name: Stock name
        price: Current price
        change_percent: Percentage change
    
    Returns:
        None
    """
    # Implementation will be added
    pass
