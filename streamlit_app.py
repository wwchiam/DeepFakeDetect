import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

##########################################################################################################################
# Navigation Bar

option = st.selectbox("", ("Home", "About Us", "Contact Us"))

if option == "About Us":
    st.header("About Us")
    st.write("""
        Testing testing 
    """)

elif option == "Home":
    st.header("Our Product")
    st.write("""
        Testing testing 
    """)

elif option == "Contact Us":
    st.header("Contact Us")
    st.write("""
        Testing testing 
    """)
    

##########################################################################################################################
