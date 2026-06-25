"""
Navbar Component

Displays top navigation bar with branding and quick actions.
"""

import streamlit as st


def render_navbar():
    """
    Render the top navigation bar.
    
    Returns:
        None
    """
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.markdown("**📈 ISMP**")
    
    with col2:
        st.markdown("### Indian Stock Market Platform")
    
    with col3:
        st.write("")
        st.write("")
        if st.button("🔐 Logout", key="navbar_logout"):
            st.write("Logout functionality will be implemented.")
