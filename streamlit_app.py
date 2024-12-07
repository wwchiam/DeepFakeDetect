import streamlit as st
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import zipfile

# Set the browser tab name
st.set_page_config(page_title="WW's Deepfake Detection App 🎈")

# Title and description of the app
st.title("🎈 Deepfake Detection")
st.write(
    "Not sure if that picture or video is real? Let us reveal the truth."
)

#model = load_model(improved_vgg16.keras)

# Image upload
image_file = st.file_uploader("Choose an image", type=['jpg', 'jpeg', 'png'])

# Function to preprocess the image
def preprocess_image(image, target_size=(224, 224)):
    """Load and preprocess an image for prediction."""
    try:
        # Load the image
        image = load_img(image, target_size=target_size)
        
        # Convert the image to a numpy array
        image_array = img_to_array(image)
        
        # Normalize the image (scale pixel values to [0, 1])
        image_array = image_array / 255.0
        
        # Add a batch dimension
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    except Exception as e:
        st.error(f"Error loading or processing the image: {e}")
        return None

# Prediction logic
if image_file is not None:
    # Display the uploaded image
    st.image(image_file, caption='Uploaded Image', use_column_width=True)
    
    # Preprocess the image
    input_image = preprocess_image(image_file)

    if input_image is not None:
        # Predict using the model
        prediction = model.predict(input_image)

        # Interpret the result
        if prediction[0][0] > 0.5:
            st.write(f"The model predicts the image is **FAKE** with a confidence of {prediction[0][0]:.2f}")
        else:
            st.write(f"The model predicts the image is **ORIGINAL** with a confidence of {1 - prediction[0][0]:.2f}")
else:
    st.write("Please upload an image for prediction.")
