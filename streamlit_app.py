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

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "Home"  # Default page is Home

# Add Home and About Us buttons at the top
col1, col2 = st.columns([1.5, 2.5])  # Adjust column widths as needed

with col1:
    # Button to switch to the Home page
    if st.button('Home'):
        st.session_state["current_page"] = "Home"

    # Button to switch to the About Us page
    if st.button('About Us'):
        st.session_state["current_page"] = "About Us"

# Main Layout Split into Two Columns
with col2:
    if st.session_state["current_page"] == "Home":
        # Upload Section for Image Detection
        st.subheader("Upload an Image for Detection")
        uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

            if st.button("Detect Deepfake"):
                with st.spinner("Detecting deepfake..."):
                    time.sleep(2)  # Simulating a delay
                    st.success("Deepfake detected!")

    elif st.session_state["current_page"] == "About Us":
        st.title("About Us")
        st.markdown(
            """
            ### Company Profile
            We are a cutting-edge AI company dedicated to combating deepfake technology and promoting digital authenticity. 
            Our mission is to protect individuals and organizations from manipulated media by providing robust and accessible detection tools.
            """
        )
