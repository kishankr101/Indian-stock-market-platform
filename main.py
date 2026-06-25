"""
Indian Stock Market Platform - Main Application Entry Point

This is the main Streamlit application that orchestrates all pages and components.
Streamlit automatically detects pages from the 'pages/' directory.
"""

import streamlit as st
from config import APP_CONFIG

# Configure Streamlit page settings
st.set_page_config(
    page_title=APP_CONFIG['APP_NAME'],
    page_icon=APP_CONFIG['APP_ICON'],
    layout=APP_CONFIG['LAYOUT'],
    initial_sidebar_state=APP_CONFIG['SIDEBAR_STATE'],
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
    Displays the dashboard homepage and navigation guide.
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
    Use the **sidebar menu** (left side) to navigate between different sections:
    
    - **Dashboard**: Overview of market performance and portfolio
    - **Market**: Explore stocks, indices, and market data
    - **Watchlist**: Create and manage your watchlists
    - **Portfolio**: Track your investments
    - **Paper Trading**: Practice trading with virtual money
    - **Technical Analysis**: Analyze stocks with technical indicators
    - **News & Research**: Stay updated with latest financial news
    - **Wallet**: Manage your account balance
    - **Profile**: View and edit your profile
    - **Settings**: Configure application preferences
    """)
    
    st.divider()
    
    # Footer
    st.markdown("""
    <div style='text-align: center; color: #999; margin-top: 2rem;'>
        <p>© 2024 Indian Stock Market Platform | Built with ❤️ using Streamlit</p>
        <p style='font-size: 0.9rem;'>Disclaimer: This is a demo platform. Always consult a financial advisor before investing.</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
