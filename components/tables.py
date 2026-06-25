"""
Tables Component

Reusable table components for displaying data.
Provides functions for creating formatted data tables.
"""

import streamlit as st
import pandas as pd


def display_data_table(data, title, max_rows=100):
    """
    Display a formatted data table.
    
    Args:
        data: DataFrame to display
        title: Table title
        max_rows: Maximum number of rows to display
    
    Returns:
        None
    """
    st.subheader(title)
    st.dataframe(data.head(max_rows), use_container_width=True)


def display_stock_table(stocks_data):
    """
    Display a table of stock information.
    
    Args:
        stocks_data: DataFrame with stock information
    
    Returns:
        None
    """
    # Implementation will be added
    pass


def display_portfolio_table(portfolio_data):
    """
    Display portfolio holdings in a table.
    
    Args:
        portfolio_data: DataFrame with portfolio data
    
    Returns:
        None
    """
    # Implementation will be added
    pass
