import streamlit as st

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

# Navigation buttons
st.sidebar.title("Navigation")
if st.sidebar.button("Home"):
    st.session_state["current_page"] = "Home"
if st.sidebar.button("About Us"):
    st.session_state["current_page"] = "About Us"
if st.sidebar.button("Contact Us"):
    st.session_state["current_page"] = "Contact Us"

# Display content based on current page
if st.session_state["current_page"] == "Home":
    # Main Layout Split into Two Columns
    col1, col2 = st.columns([1, 1.5])

    # Left Column: Title and Banner Section
    with col1:
        st.markdown(
            """
            <div style="background-color: #002d26; padding: 40px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
                <h1 style="color: #ffffff; font-size: 3rem;">Deepfake Detector</h1>
                <p style="color: #d4f0e2; font-size: 1rem; margin-top: 20px;">
                    Seeing is no longer believing. Protect yourself from fake images with AI Solution.
                </p>
                <div style="margin-top: 20px;">
                    <img src="https://raw.githubusercontent.com/wwchiam/DeepFakeDetect/main/DeepfakeBanner.jpg" style="width: 100%; max-width: 100%; height: auto; border-radius: 10px;" />
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Right Column: Detection Section
    with col2:
        st.subheader("Upload an Image for Detection")
        uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
            st.markdown(
                """
                <div style="background-color: #004c40; color: #ffffff; padding: 20px; border-radius: 10px; font-size: 1.2rem;">
                    Result session
                </div>
                """,
                unsafe_allow_html=True,
            )

            if st.button("Detect Deepfake"):
                st.write("Analysis feature yet to be implemented.")

elif st.session_state["current_page"] == "About Us":
    st.title("About Us")
    st.markdown(
        """
        ### Company Profile
        We are a cutting-edge AI company dedicated to combating deepfake technology and promoting digital authenticity. 
        Our mission is to protect individuals and organizations from manipulated media by providing robust and accessible detection tools.
        """
    )

elif st.session_state["current_page"] == "Contact Us":
    st.title("Contact Us")
    st.markdown(
        """
        ### Reach Out
        - **Email**: support@deepfakedetector.com
        - **Phone**: +1-800-123-4567
        - **Address**: 123 AI Boulevard, Silicon Valley, CA
        """
    )
