import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing
import os
import uuid  # Dùng để tạo một ID duy nhất cho mỗi ảnh

@st.cache
def load_model() -> ocr.Reader:
    return ocr.Reader(["en"], model_storage_directory=".")

def save_uploaded_file(image):
    # Tạo một thư mục để lưu ảnh nếu chưa tồn tại
    if not os.path.exists("Photo"):
        os.makedirs("Photo")
    # Tạo tên file duy nhất bằng cách sử dụng UUID
    unique_filename = str(uuid.uuid4()) + ".jpg"
    saved_image_path = os.path.join("./Photo", unique_filename)
    image.save(saved_image_path)
    return saved_image_path

def resize_image(image, target_size=(300, 300)):
    resized_image = image.resize(target_size)
    return resized_image

def process(image):
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
        return letters_only

def save_image(image):
    input_image = Image.open(image)  # read image
    # Lưu và hiển thị ảnh đã xử lý
    resized_image = resize_image(input_image, target_size=(300, 300))
    saved_image_path = save_uploaded_file(resized_image)
    st.write("Tên của ảnh:", os.path.basename(saved_image_path))
    st.image(saved_image_path)  # Hiển thị ảnh đã lưu
    return saved_image_path

# Sử dụng hàm process và save_image
col3, col4 = st.columns([0.5, 0.5], gap="small")
with col3:
    with st.container(border=True):
        st.header("Nghiệm thu vật liệu cọc:")
        col5, col6 = st.columns([0.2, 0.8])
        with col5:
            st.write("Đoạn cọc 1:")
        with col6:
            image = st.file_uploader(label="Upload your image here", type=["png", "jpg", "jpeg"])
            if image:
                letters_only = process(image)
                saved_image_path = save_image(image)
                file_img = str("./")+str(saved_image_path)
                st.image(file_img)  # Hiển thị ảnh đã lưu
