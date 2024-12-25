import streamlit as st
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import img_to_array
from mtcnn import MTCNN
from PIL import Image

# Page Title
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="auto"
)

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

# Image Preprocessing (without cv2)
def preprocess_image(image_file, target_size=(224, 224)):
    try:
        # Open image with PIL, resize to target size and convert to array
        image = load_img(image_file, target_size=target_size)
        image_array = img_to_array(image)
        image_array = image_array / 255.0  # Normalize the image
        return np.expand_dims(image_array, axis=0)
    except Exception as e:
        st.error(f"Error processing image: {e}")
        return None

# Face Detection with MTCNN (without OpenCV)
def detect_face_and_heatmap(image):
    detector = MTCNN()
    faces = detector.detect_faces(image)
    
    # Draw bounding boxes around faces (this time with PIL)
    pil_image = Image.fromarray(image)
    for face in faces:
        x, y, w, h = face['box']
        pil_image = pil_image.crop((x, y, x + w, y + h))  # Crop the face region

    # Convert the cropped face back to numpy array for display
    face_image = np.array(pil_image)
    return face_image, faces

# Fancy Detection (Bounding Box and Probability Display)
def fancy_detection(image_file, prediction, image_array):
    probability = round(prediction[0][0] * 100, 2)
    
    if prediction[0][0] > 0.5:
        st.markdown(f'<div class="result">This is a **fake** image. Probability: {probability}%</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result">This is a **real** image. Probability: {100 - probability}%</div>', unsafe_allow_html=True)
    
    uploaded_image = load_img(image_file, target_size=(224, 224))
    image_array = img_to_array(uploaded_image)
    image_array = np.array(image_array, dtype=np.uint8)
    
    detected_image, faces = detect_face_and_heatmap(image_array)
    
    st.image(detected_image, caption="Detected Face", use_container_width=True)
    st.markdown("<br><h4>Face Detected in Image</h4>", unsafe_allow_html=True)

# Main Functionality
def main():
    model_path = 'improved_vgg16.keras' 
    model, model_error = load_deepfake_model(model_path)

    if model_error:
        st.error(model_error)
        return

    tabs = st.tabs(["About", "Detection","Deep Neural Network", "Contact Us"])
    
    with tabs[0]:
        st.subheader("Detect Deepfakes Instantly")
        st.write("In an age where manipulated media is becoming alarmingly common, our Deepfake Detection platform empowers users to verify the authenticity of images with just a simple upload.")
        
    with tabs[1]:
        st.subheader("Upload an Image for Detection")
        uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

        if uploaded_file:
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

            image_array = preprocess_image(uploaded_file)
            
            if st.button("Detect Deepfake"):
                if image_array is not None and model is not None:
                    with st.spinner("Analyzing the image..."):
                        try:
                            prediction = model.predict(image_array)
                            fancy_detection(uploaded_file, prediction, image_array)
                        except Exception as e:
                            st.error(f"Error during prediction: {e}")
                else:
                    st.warning("Please upload a valid image.")
                    
    with tabs[2]:
        st.subheader("Cutting-Edge AI for Reliable Detection")
        st.write("Our deepfake detection engine is built on ResNet50, a state-of-the-art convolutional neural network, fine-tuned for precision and reliability.")
    
    with tabs[3]:
        st.subheader("Need Help?")
        st.write("Email to 23054196@siswa.um.edu.my for more information")

if __name__ == "__main__":
    main()
