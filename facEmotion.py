# dependencies
import streamlit as st
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# streamlit page setup
st.title("Facial Emotion Detection")
st.write("Upload an image to detect emotions.")

# image uploading section
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# when an image is uploaded my friend
if uploaded_image is not None:
    # converting the uploaded image to OpenCV format
    img = Image.open(uploaded_image)
    img_np = np.array(img)
    
    # displaying the uploaded image
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # running DeepFace analysis for emotion detection
    try:
        result = DeepFace.analyze(img_np, actions=['emotion'])

        # showing emotion analysis results
        st.write("Emotion Analysis Result:")
        for emotion, score in result[0]['emotion'].items():
            st.write(f"{emotion}: {score:.2f}%")
    
    except Exception as e:
        st.error("Error analyzing image. Please try a different image.")

