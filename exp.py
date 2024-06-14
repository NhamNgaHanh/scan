import streamlit as st
from PIL import Image
import pytesseract

def ocr_image(image):
    # Sử dụng Tesseract để nhận diện văn bản
    text = pytesseract.image_to_string(image)
    return text

def main():
    st.title("Ứng dụng OCR sử dụng Streamlit")

    uploaded_image = st.file_uploader("Tải lên hình ảnh", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Đọc hình ảnh từ file đã tải lên
        image = Image.open(uploaded_image)
        text = ocr_image(image)
        st.write(text)

if __name__ == "__main__":
    main()
