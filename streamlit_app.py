import streamlit as st
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os
import cv2
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array

# Page Title
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="auto"
)

# Global CSS
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://raw.githubusercontent.com/wwchiam/DeepFakeDetect/main/background.jpg');
        background-size: cover;
        background-position: center;
        font-family: Arial, sans-serif;
        font-size: 20px;
        color: #ffffff;
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
    .result, .report {
        font-size: 22px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
        color: #ffffff;
    }

    .stSubheader {
        font-size: 18px !important;
        color: #ffffff !important;
    }

    .stTabs div[role="tablist"] {
        justify-content: center !important;
    }

    .stTabs [role="tab"] {
        font-size: 22px !important;
        font-weight: bold !important;
        color: #ffffff !important;
    }

    .css-1cpxqw2, .css-18e3th9, .css-1n76uvr {
        color: #ffffff !important;
    }

    .stFileUploader label {
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title Section
st.markdown('<div class="title">Deepfake Detection System</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Seeing is no longer believing </div>', unsafe_allow_html=True)

# Model Loading
@st.cache_resource
def load_deepfake_model(model_path):
    if os.path.exists(model_path):
        try:
            model = load_model(model_path)
            return model, None
        except Exception as e:
            return None, f"Failed to load the model. Error: {e}"
    return None, "Model file not found. Please check the path."

# Image Preprocessing
def preprocess_image(image_file, target_size=(224, 224)):
    try:
        image = load_img(image_file, target_size=target_size)
        image_array = img_to_array(image) / 255.0
        return np.expand_dims(image_array, axis=0)
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Face Detection and Bounding Box
def detect_face_and_heatmap(image):
    # Convert to grayscale for face detection
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image_gray, 1.1, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    return image, faces

# Save Image Function
def save_reported_image(image_file):
    file_path = f"reported_images/{image_file.name}"
    if not os.path.exists("reported_images"):
        os.makedirs("reported_images")
    with open(file_path, "wb") as f:
        f.write(image_file.getbuffer())
    return file_path

# Report Fake Image
def report_fake_image(image_file):
    file_path = save_reported_image(image_file)
    st.success(f"Thank you for reporting. The image has been saved for review: {file_path}")

# Fancy Detection (Bounding Box and Probability Display)
def fancy_detection(image_file, prediction, image_array):
    probability = round(prediction[0][0] * 100, 2)
    
    # Display probability
    if prediction[0][0] > 0.5:
        st.markdown(f'<div class="result">This is a **fake** image. Probability: {probability}%</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result">This is a **real** image. Probability: {100 - probability}%</div>', unsafe_allow_html=True)
    
    # Show face detection and heatmap
    uploaded_image = load_img(image_file, target_size=(224, 224))
    image_array = img_to_array(uploaded_image)
    image_array = np.array(image_array, dtype=np.uint8)
    
    detected_image, faces = detect_face_and_heatmap(image_array)
    
    # Display detected image with bounding box
    st.image(detected_image, caption="Detected Face", use_container_width=True)
    
    # If heatmap is required, add code to show heatmap on altered areas
    st.markdown("<br><h4>Face Detected in Image</h4>", unsafe_allow_html=True)
    
# Main Functionality
def main():
    # Load the model
    model_path = 'improved_vgg16.keras' 
    model, model_error = load_deepfake_model(model_path)

    if model_error:
        st.error(model_error)
        return

    # Tab Layout
    tabs = st.tabs(["About", "Detection","Deep Neural Network", "Contact Us"])
    
    # About Tab
    with tabs[0]:
        st.subheader("Detect Deepfakes Instantly")
        st.write("In an age where manipulated media is becoming alarmingly common, our Deepfake Detection platform empowers users to verify the authenticity of images with just a simple upload.")
        
    # Detection Tab
    with tabs[1]:
        st.subheader("Upload an Image for Detection")
        uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            # Show the uploaded image in the first column
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

            image_array = preprocess_image(uploaded_file)
            
            # Prediction
            if st.button("Detect Deepfake"):
                if image_array is not None and model is not None:
                    with st.spinner("Analyzing the image..."):
                        try:
                            prediction = model.predict(image_array)
                            fancy_detection(uploaded_file, prediction, image_array)
                            
                            agree = st.radio("Would you like to report this image as a deepfake?", ["Yes", "No"], index=1)
                            if agree == "Yes":
                                report_fake_image(uploaded_file)
                        except Exception as e:
                            st.error(f"Error during prediction: {e}")
                else:
                    st.warning("Please upload a valid image.")
                    
    # Technology Tab
    with tabs[2]:
        st.subheader("Cutting-Edge AI for Reliable Detection")
        st.write("Our deepfake detection engine is built on ResNet50, a state-of-the-art convolutional neural network, fine-tuned for precision and reliability.")
    
    # Contact us Tab
    with tabs[3]:
        st.subheader("Need Help?")
        st.write("Email to 23054196@siswa.um.edu.my for more information")

if __name__ == "__main__":
    main()
