import streamlit as st
import numpy as np
import pandas as pd
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
from sklearn.preprocessing import StandardScaler
import os
import io


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


# Image Preprocessing Function
def preprocess_image(image_file, target_size=(224, 224)):
    """Preprocess the uploaded image for deepfake detection."""
    try:
        # Load image
        image = load_img(image_file, target_size=target_size)
        
        # Convert image to numpy array
        image_array = img_to_array(image) 
        
        # Normalize image array (scale pixel values between 0 and 1)
        image_array = image_array / 255.0 
        
        # Add batch dimension to the image
        image_array = np.expand_dims(image_array, axis=0)
        return image_array
    except Exception as e:
        st.error(f"Error processing the image: {e}")
        return None


# Streamlit App Layout and Prediction Logic
def main():
    st.title("Welcome to Deepfake Detection")
    st.markdown(
    """
    <div style="font-size: 22px; font-weight: bold; text-align: left; color: black;">
        When in doubt, check with us
    </div>
    """,
    unsafe_allow_html=True
)
    st.image('DeepfakeBanner.jpg', use_column_width=True)
    
    st.markdown(
        """
       <div style="text-align: center; margin-top: 20px; font-size: 24px; font-weight: bold; color: red;">
            Seeing is no longer believing. <br>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
        body {
            background-image: url('background.jpg');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    

    # Load the model
    model_path = 'improved_vgg16.keras'  # Change this to your model's path
    model, model_error = load_deepfake_model(model_path)

    if model_error:
        st.error(model_error)
        return

    # File uploader for image
    uploaded_file = st.file_uploader("Upload your file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image
        image_array = preprocess_image(uploaded_file)

        if st.button("Submit"):
            if image_array is not None and model is not None:
                st.write("Running deepfake detection...")

                try:
                    # Predict with the model
                    prediction = model.predict(image_array)

                    # Assuming the model outputs 0 for real and 1 for fake
                    if prediction[0][0] > 0.5:
                        st.write("This is a **fake** image.")
                    else:
                        st.write("This is a **real** image.")
                    st.success("Detection completed!")
                except Exception as e:
                    st.error(f"Error during prediction: {e}")


if __name__ == "__main__":
    main()
