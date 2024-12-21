import streamlit as st
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os

# Streamlit page configuration
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://raw.githubusercontent.com/wwchiam/DeepFakeDetect/main/background.jpg');
        background-size: cover;
        background-position: center;
        font-family: Arial, sans-serif;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-top: 10px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
    }
    .sub-title {
        font-size: 22px;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-bottom: 30px;
    }
    .result {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .report-btn {
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title Section
st.markdown('<div class="title">Deepfake Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Ensuring authenticity in the digital world</div>', unsafe_allow_html=True)
st.image("DeepfakeBanner.jpg", use_container_width=True)

# Model Loading
@st.cache_resource
def load_deepfake_model(model_path):
    """Load the deepfake detection model."""
    if os.path.exists(model_path):
        try:
            model = load_model(model_path)
            return model, None
        except Exception as e:
            return None, f"Failed to load the model. Error: {e}"
    return None, "Model file not found. Please check the path."

# Image Preprocessing
def preprocess_image(image_file, target_size=(224, 224)):
    """Preprocess the image for model prediction."""
    try:
        image = load_img(image_file, target_size=target_size)
        image_array = img_to_array(image) / 255.0
        return np.expand_dims(image_array, axis=0)
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Report Fake Image
def report_fake_image(image_file):
    """Simulate reporting a deepfake image."""
    st.success("Thank you for reporting. We will use this image for future training.")

# Main Functionality
def main():
    # Load the model
    model_path = 'improved_vgg16.keras'  # Update with your model path
    model, model_error = load_deepfake_model(model_path)

    if model_error:
        st.error(model_error)
        return

    # About Section
    st.sidebar.title("About")
    st.sidebar.info(
        """
        This tool uses AI to detect whether an uploaded image is real or fake (deepfake).
        Your participation helps us improve our detection algorithms.
        """
    )

    # File Upload
    uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
        image_array = preprocess_image(uploaded_file)

        # Prediction
        if st.button("Detect Deepfake"):
            if image_array is not None and model is not None:
                with st.spinner("Analyzing the image..."):
                    try:
                        prediction = model.predict(image_array)[0][0]
                        if prediction > 0.5:
                            result = "This is a **fake** image."
                            st.markdown(f'<div class="result">{result}</div>', unsafe_allow_html=True)
                            agree = st.radio("Would you like to report this image as a deepfake?", ["Yes", "No"], index=1)
                            if agree == "Yes":
                                report_fake_image(uploaded_file)
                        else:
                            result = "This is a **real** image."
                            st.markdown(f'<div class="result">{result}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error during prediction: {e}")
            else:
                st.warning("Please upload a valid image.")

if __name__ == "__main__":
    main()
