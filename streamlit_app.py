import streamlit as st
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import os

# Page Title Appear at browser
st.set_page_config(
    page_title="Deepfake Detection",
    page_icon="🕵️‍♂️",
    layout="wide",
    initial_sidebar_state="auto"
)
