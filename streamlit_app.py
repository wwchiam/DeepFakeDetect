import streamlit as st

# Page configuration
st.set_page_config(page_title="Free Deepfake Detector", layout="wide")

# Header with navigation tabs
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; background-color: #ffffff; padding: 10px 20px; border-bottom: 2px solid #e6e6e6;">
        <div style="display: flex; align-items: center;">
            <img src="https://via.placeholder.com/150x50.png?text=Resemble.AI" alt="Resemble.AI Logo" style="height: 50px; margin-right: 10px;">
            <h3 style="margin: 0; color: #002d26;">RESEMBLE.AI</h3>
        </div>
        <div style="display: flex; gap: 20px; font-size: 16px;">
            <a href="#" style="text-decoration: none; color: #333;">AI Voice Generator</a>
            <a href="#" style="text-decoration: none; color: #333;">Detect</a>
            <a href="#" style="text-decoration: none; color: #333;">Resources</a>
            <a href="#" style="text-decoration: none; color: #333;">Government</a>
            <a href="#" style="text-decoration: none; color: #333;">Pricing</a>
            <a href="#" style="text-decoration: none; color: #333;">Sign In</a>
            <a href="#" style="text-decoration: none; background-color: #ffd700; color: #002d26; padding: 5px 15px; border-radius: 5px;">Request Demo</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Title Section
st.markdown(
    """
    <div style="background-color: #002d26; padding: 20px; border-radius: 10px;">
        <h1 style="color: #ffffff;">Free Deepfake Detector</h1>
        <p style="color: #d4f0e2; font-size: 18px;">
            1 out of 4 people are impacted by Voice AI Scams causing more than $1.6B in damages.
            Protect your organization today by integrating Resemble’s Detect Stack.
        </p>
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
        # Prediction placeholder
        if st.button("Detect Deepfake"):
            st.write("Analysis feature yet to be implemented.")

# Contact Us Tab
with tabs[2]:
    st.subheader("Need Help?")
    st.write("Email to xxx for more information")
