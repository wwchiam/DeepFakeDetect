import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling buttons
st.markdown("""
    <style>
        .nav-button {
            display: inline-block;
            padding: 10px 20px;
            margin: 5px;
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            text-decoration: none;
            text-align: center;
            font-size: 16px;
        }
        .nav-button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Display custom top navigation buttons
col1, col2, col3 = st.columns(3)

# Buttons for navigation
with col1:
    if st.button("Home"):
        st.session_state.page = "Home"
        
with col2:
    if st.button("About Us"):
        st.session_state.page = "About Us"
        
with col3:
    if st.button("Contact Us"):
        st.session_state.page = "Contact Us"

# If `st.session_state.page` is not set, set default to "Home"
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Display the corresponding content based on the button clicked
if st.session_state.page == "Home":
    st.header("Our Product")
    st.write("""
        This is the Home section. Here we describe our main product or service.
    """)

elif st.session_state.page == "About Us":
    st.header("About Us")
    st.write("""
        This is the About Us section. Here we introduce our platform and goals.
    """)

elif st.session_state.page == "Contact Us":
    st.header("Contact Us")
    st.write("""
        This is the Contact Us section. Feel free to reach out to us for more information.
    """)
