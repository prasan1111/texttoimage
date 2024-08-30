import streamlit as st
import requests
import io
from PIL import Image

# Set the API URL and headers
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

# Define the function to query the model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit application layout
st.title("Text-to-Image Generator")
st.write("Enter a description below to generate an image.")

# User input for the text description
text_input = st.text_input("Enter your description:")

# Generate the image when the button is clicked
if st.button("Generate Image"):
    if text_input:
        with st.spinner("Generating image..."):
            image_bytes = query({"inputs": text_input})
            image = Image.open(io.BytesIO(image_bytes))
            
            # Display the generated image
            st.image(image, caption=f"Generated Image for: '{text_input}'", use_column_width=True)
    else:
        st.error("Please enter a description to generate an image.")