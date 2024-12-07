import os
import numpy as np
import cv2
import tempfile
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import streamlit as st

# Title and description of the app
st.title("🎈 Deepfake Detection")
st.write(
    "Not sure if that picture or video is real? Let us reveal the truth."
)

# Upload file
uploaded_file = st.file_uploader("Upload a photo or video", type=["jpg", "jpeg", "png", "mp4", "avi"])



