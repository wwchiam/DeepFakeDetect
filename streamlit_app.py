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

# Navigation handler
def navigate(page):
    st.session_state["current_page"] = page

# Header with navigation tabs
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: #ffffff; padding: 10px 20px; border-bottom: 2px solid #e6e6e6;">
        <div style="display: flex; align-items: center;">
            <h3 style="margin: 0; color: #002d26;">A project by <span style='color: #ff5733;'>Wei Wei</span></h3>
        </div>
        <div style="display: flex; gap: 20px; font-size: 16px;">
            <a href="#" onclick="window.parent.postMessage('navigate:About', '*');" style="text-decoration: none; color: #333;">About us</a>
            <a href="#" onclick="window.parent.postMessage('navigate:Contact', '*');" style="text-decoration: none; color: #333;">Contact us</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Listen for custom navigation messages
custom_js = """
<script>
window.addEventListener("message", (event) => {
    if (event.data.startsWith("navigate:")) {
        const page = event.data.split(":")[1];
        window.parent.postMessage(page, "*");
    }
});
</script>
"""
st.markdown(custom_js, unsafe_allow_html=True)

# Main Layout Split into Two Columns
if st.session_state["current_page"] == "Home":
    col1, col2 = st.columns([1, 1.5])

    # Left Column: Title and Banner Section
    with col1:
        st.markdown(
            """
            <div style="background-color: #002d26; padding: 40px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
                <h1 style="color: #ffffff; font-size: 3rem;">Free Deepfake Detector</h1>
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
            # Placeholder for results section
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

# About Us Page
elif st.session_state["current_page"] == "About":
    st.title("About Us")
    st.markdown(
        """
        <p style="font-size: 1.2rem;">
            Welcome to Wei Wei's Deepfake Detection Project! Our mission is to leverage advanced AI technology 
            to protect individuals and organizations from malicious deepfake content.
        </p>
        <p style="font-size: 1.2rem;">
            This project was built by Wei Wei, a passionate team of researchers and developers committed to 
            combating misinformation and fake media.
        </p>
        """,
        unsafe_allow_html=True,
    )

# Contact Us Page
elif st.session_state["current_page"] == "Contact":
    st.title("Contact Us")
    st.markdown(
        """
        <p style="font-size: 1.2rem;">
            For inquiries, collaboration, or support, please email us at: 
            <a href="mailto:info@deepfakedetection.com">info@deepfakedetection.com</a>
        </p>
        """,
        unsafe_allow_html=True,
    )
