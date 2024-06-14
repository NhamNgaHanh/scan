import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing
from easyocr import Reader
import os
import uuid  # Dùng để tạo một ID duy nhất cho mỗi ảnh

@st.cache
def load_model() -> Reader:
    return ocr.Reader(["en"], model_storage_directory=".")

def save_uploaded_file(image):
    # Tạo một thư mục để lưu ảnh nếu chưa tồn tại
    if not os.path.exists("Photo"):
        os.makedirs("Photo")
    # Tạo tên file duy nhất bằng cách sử dụng UUID
    unique_filename = str(uuid.uuid4()) + ".jpg"
    saved_image_path = os.path.join("Photo", unique_filename)
    image.save(saved_image_path)
    return saved_image_path

def resize_image(image, target_size=(300, 300)):
    resized_image = image.resize(target_size)
    return resized_image

def process_and_save_image(image):
    saved_image_path = None
    HA1 = None

    if image is not None:
        input_image = Image.open(image)  # read image
        reader = load_model()  # load model
        result = reader.readtext(np.array(input_image))
        result_text = []  # empty list for results
        for text in result:
            result_text.append(text[1])
        st.session_state["HA11"] = result_text
        HA1 = st.session_state.get("HA11", [])
        with st.container(height=150, border=True):
            for line in HA1:
                # Loại bỏ ký tự từ kí tự thứ năm trở đi
                # Kiểm tra nếu ký tự là một ký tự chữ cái hoặc số
                letters_only = ''.join(c for i, c in enumerate(line) if i < 4 or (c.isalpha() or c.isdigit() or c.isspace()))
                st.write(letters_only)

        # Lưu và hiển thị ảnh đã xử lý
        resized_image = resize_image(input_image, target_size=(300, 300))
        saved_image_path = save_uploaded_file(resized_image)
        st.write("Tên của ảnh:", os.path.basename(saved_image_path))
        st.image(saved_image_path)  # Hiển thị ảnh đã lưu
    else:
        st.write("Upload an Image")

    return saved_image_path, HA1


# Sử dụng hàm process_and_save_image
image = st.file_uploader(label="Upload your image here", type=["png", "jpg", "jpeg"])
saved_image_path = process_and_save_image(image)
st.image(saved_image_path)  # Hiển thị ảnh đã lưu
