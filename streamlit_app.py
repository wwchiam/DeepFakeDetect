import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"

# Main Layout Split into Two Columns
col1, col2 = st.columns([1.5, 2.5])  # Adjust column widths as needed

# Left Column: Banner & Navigation Section
with col1:
    # Green Box Container for Title and Banner Image
    st.markdown(
        """
        <div style="background-color: #004d40; padding: 40px; border-radius: 20px; margin-bottom: 20px; text-align: center; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);">
            <h1 style="color: #ffffff; font-size: 3rem; font-weight: bold;">Deepfake Detector</h1>
            <p style="color: #d4f0e2; font-size: 1.2rem; margin-top: 15px; font-style: italic;">
                Seeing is no longer believing. Protect yourself from fake images with AI Solution.
            </p>
            <div style="margin-top: 20px;">
                    <img src="https://raw.githubusercontent.com/wwchiam/DeepFakeDetect/main/DeepfakeBanner.jpg" style="width: 100%; height: auto; border-radius: 10px;" />
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Navigation buttons at the top of the page
st.markdown(
    """
    <div style="display: flex; justify-content: flex-start; margin-bottom: 20px;">
        <button style="background-color: #004d40; color: white; border: none; padding: 10px 20px; font-size: 16px; cursor: pointer; margin-right: 10px;" onclick="window.location.href='/home'">Home</button>
        <button style="background-color: #004d40; color: white; border: none; padding: 10px 20px; font-size: 16px; cursor: pointer; margin-right: 10px;" onclick="window.location.href='/about'">About Us</button>
        <button style="background-color: #004d40; color: white; border: none; padding: 10px 20px; font-size: 16px; cursor: pointer;" onclick="window.location.href='/help'">Help</button>
    </div>
    """, 
    unsafe_allow_html=True
)

# Right Column: Content Based on Current Page
with col2:
    if st.button('Home'):
        st.session_state["current_page"] = "Home"
        st.write("Hello from Home!")

    elif st.button('About Us'):
        st.session_state["current_page"] = "About Us"
        st.write("Hello from About Us!")

    elif st.button('Help'):
        st.session_state["current_page"] = "Help"
        st.write("Hello from Help!")
