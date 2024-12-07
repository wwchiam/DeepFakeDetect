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

# Load the model (ensure it's uploaded to the right directory in your GitHub or the correct path in your environment)
@st.cache_resource
def load_deepfake_model():
    try:
        # Load model from correct path (ensure the path is correct)
        model = load_model('improved_vgg16.keras')  # Adjust the path if necessary
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

# Function to preprocess the image
def preprocess_image(image, target_size=(224, 224)):
    """Load and preprocess an image for prediction."""
    try:
        # Load the image (in-memory image file)
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

# Load the model
model = load_deepfake_model()

# File uploader section
st.subheader("Upload your image")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

# If an image is uploaded, show the file and add a submit button
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    # Preprocess the image for prediction
    image_array = preprocess_image(uploaded_file)

    # Submit button to start deepfake detection
    if st.button("Submit"):
        if image_array is not None and model is not None:
            # Run the deepfake detection model on the image
            st.write("Running deepfake detection on the uploaded image...")

            try:
                # Make the prediction
                prediction = model.predict(image_array)
                
                # Assuming the model outputs a probability of being fake (greater than 0.5)
                # You may need to modify this depending on your model's output
                if prediction[0][0] > 0.5:
                    st.write("This is a **fake** image.")
                else:
                    st.write("This is a **real** image.")
                st.success("Detection completed!")
            except Exception as e:
                st.error(f"Error during prediction: {e}")
        else:
            st.error("Error processing the image or loading the model.")
