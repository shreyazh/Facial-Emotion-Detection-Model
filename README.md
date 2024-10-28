# Facial Emotion Detection Web Application

**Author**: Shreyash Srivastava  
**Description**: This Streamlit application allows users to upload an image and detects emotions present in the face using DeepFace. The app displays the uploaded image alongside the emotion detection results, providing an interactive experience for the user.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Explanation](#code-explanation)

---

## Overview

This application leverages the **DeepFace** library to analyze facial emotions in an uploaded image. It is designed as a **Streamlit** app for an easy-to-use web interface, where users can see emotion analysis results displayed beside their uploaded image. 

## Features

- **Image Upload**: Upload images in `jpg`, `jpeg`, or `png` format.
- **Emotion Detection**: Detects and displays probabilities for various emotions in the uploaded face image.
- **User-Friendly Interface**: Easy-to-use web interface with side-by-side layout for image and results.

## Setup and Installation

To run this project locally, please follow the steps below:

1. Clone the repository or save the code as `app.py`.
2. Install the required packages by running:
   ```bash
   pip install streamlit deepface opencv-python pillow matplotlib
   ```
3. Run the Streamlit app with the following command:
   ```bash
   streamlit run app.py
   ```

4. Open your web browser and go to `http://localhost:8501` to interact with the app.

## Usage

1. **Upload Image**: Click on the "Choose an image..." button to upload an image file.
2. **View Results**: The app will display the uploaded image and show the emotion detection results beside it.

## Project Structure

```
.
├── app.py           # Main Streamlit application code
└── requirements.txt # Required dependencies (optional)
```

## Code Explanation

### Importing Libraries

```python
import streamlit as st
from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
```

- **streamlit**: Used to create a web interface.
- **DeepFace**: Deep learning library for face analysis.
- **opencv-python**: Used for image processing.
- **PIL**: Used to handle image uploads.
- **numpy**: For handling image data in array format.

### Layout and Image Upload

```python
# Streamlit page setup
st.title("Facial Emotion Detection")
st.write("Upload an image to detect emotions.")

# Image upload section
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
```

- `st.title()` and `st.write()` define the page title and subtitle.
- `st.file_uploader()` provides an upload widget for image files.

### Displaying Image and Results

```python
# When an image is uploaded
if uploaded_image is not None:
    # Convert the uploaded image to OpenCV format
    img = Image.open(uploaded_image)
    img_np = np.array(img)

    # Create two columns for displaying the image and results side-by-side
    col1, col2 = st.columns([1, 1])

    # Display the uploaded image in the first column
    with col1:
        st.image(img, caption="Uploaded Image", width=300)

    # Run DeepFace analysis for emotion detection and display results in the second column
    with col2:
        st.write("Emotion Analysis Result:")
        try:
            result = DeepFace.analyze(img_np, actions=['emotion'])

            # Display each emotion with its probability
            for emotion, score in result[0]['emotion'].items():
                st.write(f"{emotion}: {score:.2f}%")
        
        except Exception as e:
            st.error("Error analyzing image. Please try a different image.")
```

- The uploaded image is converted to a NumPy array and displayed using **Streamlit's column layout**.
- `DeepFace.analyze()` is called to detect emotions, and the results are shown beside the image in the second column.

---

With these steps, users can upload an image and receive real-time emotion analysis feedback directly through the web interface.
