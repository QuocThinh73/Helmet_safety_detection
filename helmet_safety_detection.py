import streamlit as st
from ultralytics import YOLOv10
import numpy as np
from PIL import Image
import cv2

MODEL_PATH = 'model.pt'
model = YOLOv10(MODEL_PATH)


def helmet_safety_detection(image):
    # Convert the image to numpy array
    image_np = np.array(image.convert("RGB"))

    # Use the model to predict bounding boxes and labels
    results = model.predict(image_np)

    for result in results:
        for box in result.boxes.data:
            x1, y1, x2, y2 = map(int, box[:4])
            label = result.names[int(box[5])]
            score = box[4]

            # Draw bounding box
            cv2.rectangle(image_np, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Draw label and score
            cv2.putText(image_np, f'{label} {score:.2f}', (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image_np


st.title("Helmet Safety Detection")
col1, col2 = st.columns([2, 5])

with col1:
    st.header("Upload Image")
    uploaded_file = st.file_uploader(
        "Choose an image file", type=["jpg", "jpeg", "png"])

with col2:
    st.header("Helmet Safety Detection")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        result_image = helmet_safety_detection(image)
        if result_image is not None:
            st.image(result_image)
