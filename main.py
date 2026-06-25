"""
Indian Stock Market Platform - Main Application Entry Point
"""

import streamlit as st
import pandas as pd
from datetime import datetime

# Configure Streamlit page settings
st.set_page_config(
    page_title="Indian Stock Market Platform",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #555;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """
    Main application function.
    """
    st.markdown('<div class="main-header">📈 Indian Stock Market Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Your comprehensive platform for stock market analysis and trading</div>', unsafe_allow_html=True)
    
    st.divider()
    
    # Welcome Section
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📊 **Dashboard**\nReal-time market overview")
    with col2:
        st.success("🏠 **Market**\nExplore stocks and indices")
    with col3:
        st.warning("⭐ **Watchlist**\nTrack your favorite stocks")
    
    st.divider()
    
    # Features Overview
    st.subheader("🌟 Features")
    features = [
        "📈 Real-time market data and analysis",
        "💼 Portfolio management and tracking",
        "📊 Technical analysis tools",
        "📰 Latest financial news and research",
        "💰 Paper trading for practice",
        "👛 Wallet management",
        "⚙️ Customizable settings",
    ]
    
    for feature in features:
        st.write(f"- {feature}")
    
    st.divider()
    
    # Navigation Guide
    st.subheader("🧭 Navigation Guide")
    st.write("""
    ### Available Modules:
    
    1. **Dashboard** - Overview of market performance and portfolio
    2. **Market** - Explore stocks, indices, and market data
    3. **Watchlist** - Create and manage your watchlists
    4. **Portfolio** - Track your investments
    5. **Paper Trading** - Practice trading with virtual money
    6. **Technical Analysis** - Analyze stocks with technical indicators
    7. **News & Research** - Stay updated with latest financial news
    8. **Wallet** - Manage your account balance
    9. **Profile** - View and edit your profile
    10. **Settings** - Configure application preferences
    """)
    
    st.divider()
    
    # Quick Stats
    st.subheader("📊 Quick Stats")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(label="Market Status", value="Open", delta="✅ Live")
    
    with col2:
        st.metric(label="Total Users", value="0", delta="")
    
    with col3:
        st.metric(label="Total Trades", value="0", delta="")
    
    with col4:
        st.metric(label="Platform Uptime", value="100%", delta="✅")
    
    st.divider()
    
    # Sample Data
    st.subheader("📋 Sample Market Data")
    
    sample_data = {
        'Symbol': ['INFY', 'TCS', 'RELIANCE', 'WIPRO', 'HDFCBANK'],
        'Price': [1450.50, 3650.25, 2580.75, 425.30, 1620.80],
        'Change %': [2.5, -1.2, 3.8, 1.5, -0.8],
        'Volume': ['5.2M', '3.1M', '8.5M', '4.3M', '6.7M']
    }
    
    df = pd.DataFrame(sample_data)
    st.dataframe(df, use_container_width=True)
    
    st.divider()
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: #999; margin-top: 2rem;'>
        <p>© 2024 Indian Stock Market Platform | Built with ❤️ using Streamlit</p>
        <p style='font-size: 0.9rem;'>Disclaimer: This is a demo platform. Always consult a financial advisor before investing.</p>
        <p style='font-size: 0.85rem;'>Last Updated: 2024 | Version 1.0</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
