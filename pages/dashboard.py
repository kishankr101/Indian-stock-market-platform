"""
Dashboard Page

Displays an overview of the market and user portfolio.
Shows key metrics, market indices, and portfolio summary.
"""

import streamlit as st


def main():
    """
    Main function for the Dashboard page.
    """
    st.title("📊 Dashboard")
    
    st.markdown("""
    Welcome to your personalized dashboard!
    
    **This page will display:**
    - Market overview with key indices
    - Portfolio summary and performance
    - Recent transactions
    - Market alerts and notifications
    - Quick stats and KPIs
    """)
    
    st.info("🚧 Dashboard implementation in progress...")
    
    # Placeholder sections
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Portfolio Value", value="₹0", delta="0%")
    
    with col2:
        st.metric(label="Today's Gain/Loss", value="₹0", delta="0%")
    
    with col3:
        st.metric(label="Total Return", value="0%", delta="0%")
    
    st.divider()
    
    st.subheader("Market Overview")
    st.write("Market indices and performance data will be displayed here.")
    
    st.divider()
    
    st.subheader("Portfolio Summary")
    st.write("Your portfolio holdings and allocation will be displayed here.")


if __name__ == "__main__":
    main()
