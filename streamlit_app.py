import streamlit as st

# Set the browser tab name
st.set_page_config(page_title="WW's Deepfake Detection App 🎈")

# Title and description of the app
st.title("🎈 Deepfake Detection")
st.write(
    "Not sure if that picture or video is real? Let us reveal the truth."
)

# File uploader section
st.subheader("Upload your image or video")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png", "mp4", "mov"])

# If a file is uploaded, show the file and add a submit button
if uploaded_file is not None:
    # Display the uploaded file
    if uploaded_file.type in ["image/jpeg", "image/png", "image/jpg"]:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    elif uploaded_file.type in ["video/mp4", "video/quicktime"]:
        st.video(uploaded_file, caption="Uploaded Video")
    
    # Submit button to start deepfake detection
    if st.button("Submit"):
        # Add logic for deepfake detection here
        st.write("Running deepfake detection on the uploaded file...")
        # Placeholder for deepfake detection function
        # For example, you can call a function like: detect_deepfake(uploaded_file)
        st.success("Detection completed!")
