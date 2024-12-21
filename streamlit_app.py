import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header with navigation tabs
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: #ffffff; padding: 10px 20px; border-bottom: 2px solid #e6e6e6;">
        <div style="display: flex; align-items: center;">
            <h3 style="margin: 0; color: #002d26;">A project by <span style='color: #ff5733;'> Wei Wei </span></h3>
        </div>
        <div style="display: flex; gap: 20px; font-size: 16px;">
            <a href="#" style="text-decoration: none; color: #333;">About us</a>
            <a href="#" style="text-decoration: none; color: #333;">Contact us</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Main Layout Split into Two Columns
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



