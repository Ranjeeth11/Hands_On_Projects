import streamlit as st
import tensorflow as tf
import numpy as np
import os
from PIL import Image

# Load the EDSR model
@st.cache_resource
def load_model():
    try:
        # Get the absolute path to the model file
        model_path = os.path.join(os.path.dirname(__file__), 'edsr_model.h5')
        model = tf.keras.models.load_model(model_path)  # Use the absolute path
        st.success("Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Initialize the model
model = load_model()

# Image preprocessing function
def preprocess_image(image):
    image = image.resize((128, 128))
    input_img = np.array(image) / 255.0
    input_img = np.expand_dims(input_img, axis=0)
    return input_img

# Image post-processing function
def postprocess_image(output_img):
    output_img = np.clip(output_img * 255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(output_img)

# Streamlit app layout
st.title("Image Enhancement App")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Uploaded Image", use_column_width=True)

    input_img = preprocess_image(input_image)

    # Ensure the model is loaded before predicting
    if model:
        try:
            # Predict enhanced image
            enhanced_img = model.predict(input_img)[0]
            enhanced_image = postprocess_image(enhanced_img)
            st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)
        except Exception as e:
            st.error(f"Error during enhancement: {e}")
    else:
        st.error("Model not loaded. Please check your setup.")