import streamlit as st

# Page configuration
st.set_page_config(page_title="Free Deepfake Detector", layout="wide")

# Header with navigation tabs
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: #ffffff; padding: 10px 20px; border-bottom: 2px solid #e6e6e6;">
        <div style="display: flex; align-items: center;">
            <h3 style="margin: 0; color: #002d26;">A project by <span style='color: #ff5733;'>WeiWei</span></h3>
        </div>
        <div style="display: flex; gap: 20px; font-size: 16px;">
            <a href="#" style="text-decoration: none; color: #333;">About us</a>
            <a href="#" style="text-decoration: none; color: #333;">Help</a>
            <a href="#" style="text-decoration: none; color: #333;">Contact us</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Title and Banner Section
st.markdown(
    """
    <div style="background-color: #002d26; padding: 40px; border-radius: 10px; margin-bottom: 20px; text-align: center;">
        <h1 style="color: #ffffff; font-size: 3rem;">Free Deepfake Detector</h1>
        <div style="margin-top: 20px;">
            <div style="background-color: #004c40; color: #ffffff; padding: 20px; border-radius: 10px; font-size: 1.2rem;">Banner</div>
        </div>
        <p style="color: #d4f0e2; font-size: 1rem; margin-top: 20px;">
            Learn more about protecting your organization today by integrating AI detection solutions.
        </p>
        <p style="color: #00ff00; font-size: 1rem; font-weight: bold;">Learn more <span style="color: #ffffff;">&#x2192;</span></p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Tab Layout
tabs = st.tabs(["About", "Start Detection", "Contact Us"])

# About Tab
with tabs[0]:
    st.subheader("Objective")
    st.write("Still thinking what to write... ")

    st.subheader("Who Built This?")
    st.write("Still thinking what to write... ")

    st.subheader("Based On")
    st.write("Still thinking what to write... ")

    st.subheader("Training Results")
    st.write("""
    - **Accuracy**: XXX on the validation dataset.
    - **Precision**: XXX%
    - **Recall**: XXX%
    """)

# Detection Tab
with tabs[1]:
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

# Contact Us Tab
with tabs[2]:
    st.subheader("Need Help?")
    st.write("Email to xxx for more information")
