import streamlit as st
from preprocessing import preprocess_image
from ocr_extraction import extract_text, extract_key_fields
from validation import validate_data
from utils import save_extracted_data
import cv2
import numpy as np

st.title("🏦 Automated Personal Loan Document Processing")

uploaded_file = st.file_uploader("Upload a Loan Application Document", type=["png", "jpg", "jpeg"])

if uploaded_file:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    temp_path = "sample_documents/temp_image.png"
    cv2.imwrite(temp_path, image)

    st.image(image, caption='Uploaded Document', use_column_width=True)

    if st.button("Process Document"):
        preprocessed = preprocess_image(temp_path)
        text = extract_text(preprocessed)
        key_fields = extract_key_fields(text)
        errors = validate_data(key_fields)

        st.subheader("Extracted Information:")
        st.json(key_fields)

        if errors:
            st.error(f"Validation Errors: {errors}")
        else:
            st.success("All required fields extracted successfully!")
            save_extracted_data(key_fields, "extracted_data.json")
