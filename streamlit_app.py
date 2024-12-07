import os
import numpy as np
import cv2
import tempfile
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import streamlit as st

# Load your trained model
model_path = 'improved_vgg16.keras'  # Update with your actual model path

# Error handling for model loading
try:
    model = load_model(model_path)
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading the model: {e}")
    model = None

# Title and description of the app
st.title("🎈 Deepfake Detection")
st.write(
    "Not sure if that picture or video is real? Let us reveal the truth."
)

# Function to preprocess an image
def preprocess_image(image_path, target_size=(224, 224)):
    """Load and preprocess an image for prediction."""
    try:
        image = load_img(image_path, target_size=target_size)
        image_array = img_to_array(image) / 255.0  # Normalize
        return np.expand_dims(image_array, axis=0)
    except Exception as e:
        st.error(f"Error loading or processing the image: {e}")
        return None

# Function to preprocess video frames
def preprocess_video(video_path, target_size=(224, 224), max_frames=30):
    """Extract and preprocess frames from a video."""
    frames = []
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret or frame_count >= max_frames:
            break
        
        # Resize frame to target size
        frame = cv2.resize(frame, target_size)
        frame = frame / 255.0  # Normalize
        frames.append(frame)
        frame_count += 1
    
    cap.release()
    return np.array(frames)

# Upload file
uploaded_file = st.file_uploader("Upload a photo or video", type=["jpg", "jpeg", "png", "mp4", "avi"])

if uploaded_file is not None:
    # Save file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name
    
    # Display file info
    st.write(f"Uploaded file: {uploaded_file.name}")
    
    # Process based on file type
    if uploaded_file.type.startswith("image/"):
        # Process image
        st.image(temp_file_path, caption="Uploaded Image", use_column_width=True)
        input_data = preprocess_image(temp_file_path)
        if input_data is not None:
            st.write("Analyzing the image...")
            prediction = model.predict(input_data)
            result = "FAKE" if prediction[0][0] > 0.5 else "ORIGINAL"
            st.success(f"The model predicts the image is {result}. Confidence: {prediction[0][0]:.2f}")
    elif uploaded_file.type.startswith("video/"):
        # Process video
        st.video(temp_file_path)
        st.write("Extracting frames from the video...")
        frames = preprocess_video(temp_file_path)
        
        if frames is not None and len(frames) > 0:
            st.write(f"Analyzing {len(frames)} frames...")
            predictions = model.predict(frames)
            avg_confidence = np.mean(predictions[:, 0])  # Assuming binary classification
            result = "FAKE" if avg_confidence > 0.5 else "ORIGINAL"
            st.success(f"The model predicts the video is {result}. Average Confidence: {avg_confidence:.2f}")
        else:
            st.error("Could not process frames from the video.")
    
    # Clean up temporary file
    os.unlink(temp_file_path)

# Submit button
if st.button("Submit to Check"):
    if uploaded_file is None:
        st.warning("Please upload a file first.")
