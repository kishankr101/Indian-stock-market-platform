"""
Sidebar Component

Manages sidebar navigation and configuration.
Provides centralized navigation logic for the application.
"""

import streamlit as st


def render_sidebar():
    """
    Render the sidebar with navigation options.
    
    Returns:
        None
    """
    with st.sidebar:
        st.markdown("### 📈 Indian Stock Market Platform")
        st.divider()
        
        # Placeholder for user info
        st.write("👤 User Profile")
        st.write("""
        - Username: demo_user
        - Account Type: Premium
        """)
        
        st.divider()
        
        st.markdown("### 🧭 Navigation")
        st.write("""
        Use the pages listed below to navigate:
        - Dashboard
        - Market
        - Watchlist
        - Portfolio
        - Paper Trading
        - Technical Analysis
        - News & Research
        - Wallet
        - Profile
        - Settings
        """)
        
        st.divider()
        
        st.markdown("### ⚡ Quick Links")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 Refresh"):
                st.rerun()
        
        with col2:
            if st.button("🆘 Help"):
                st.info("Help documentation will be displayed here.")
        
        st.divider()
        
        st.markdown("### 📞 Support")
        st.write("Email: support@example.com")
        st.write("Phone: +91-XXXX-XXXX-XXXX")
