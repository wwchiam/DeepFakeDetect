import streamlit as st
import numpy as np
import os
import cv2
from mtcnn import MTCNN
from keras.models import load_model
from keras.preprocessing.image import img_to_array
import tempfile


# Model Loading Function
def load_deepfake_model(model_path):
    """Loads a Keras model from the specified path."""
    if os.path.exists(model_path):
        try:
            model = load_model(model_path)
            return model, None
        except Exception as e:
            return None, f"Failed to load the model. Error: {e}"
    else:
        return None, "The model file does not exist. Please check the path."


# Preprocess Image for Prediction
def preprocess_frame(frame, target_size=(224, 224)):
    """Preprocess a single frame for deepfake detection."""
    try:
        frame = cv2.resize(frame, target_size)
        frame = frame / 255.0
        frame = img_to_array(frame)
        frame = np.expand_dims(frame, axis=0)
        return frame
    except Exception as e:
        st.error(f"Error processing the frame: {e}")
        return None


# Extract Two Frames with Faces Using MTCNN
def extract_two_frames_with_faces(video_file, frame_skip=10):
    """Extract up to 2 frames containing faces using MTCNN."""
    detector = MTCNN()
    extracted_frames = []

    try:
        cap = cv2.VideoCapture(video_file.name)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        for frame_index in range(0, total_frames, frame_skip):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
            ret, frame = cap.read()

            if not ret:
                break

            # Detect faces in the frame
            faces = detector.detect_faces(frame)
            if faces:
                extracted_frames.append(frame)

            # Stop after extracting 2 frames
            if len(extracted_frames) >= 2:
                break

        cap.release()

        if not extracted_frames:
            st.warning("No faces detected in the video.")
        return extracted_frames

    except Exception as e:
        st.error(f"Error extracting frames: {e}")
        return []


# Streamlit App Layout and Logic
def main():
    st.title("🎈 Deepfake Detection")

    # Load the model
    model_path = 'improved_vgg16.keras'  # Change this to your model's path
    model, model_error = load_deepfake_model(model_path)

    if model_error:
        st.error(model_error)
        return

    # File uploader for video
    uploaded_video = st.file_uploader("Upload a video to check if it's real or fake", type=["mp4", "avi", "mov"])

    if uploaded_video is not None:
        # Display the uploaded video
        st.video(uploaded_video, format="video/mp4")

        if st.button("Submit"):
            st.write("Processing the video...")

            # Save the uploaded file to a temporary location
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
                temp_video.write(uploaded_video.read())
                temp_video_path = temp_video.name

            # Extract two frames with faces
            frames = extract_two_frames_with_faces(temp_video, frame_skip=10)

            if frames:
                predictions = []

                # Run prediction on each extracted frame
                for frame in frames:
                    preprocessed_frame = preprocess_frame(frame)
                    if preprocessed_frame is not None:
                        prediction = model.predict(preprocessed_frame)
                        predictions.append(prediction[0][0])

                # Compute average prediction
                if predictions:
                    avg_prediction = np.mean(predictions)

                    # Assuming prediction > 0.5 means fake
                    if avg_prediction > 0.5:
                        st.write("The video is **fake**.")
                    else:
                        st.write("The video is **real**.")
                    st.success("Detection completed!")
                else:
                    st.warning("No valid predictions were made.")
            else:
                st.warning("No frames with faces were extracted from the video.")

if __name__ == "__main__":
    main()
