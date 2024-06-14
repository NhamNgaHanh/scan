import streamlit as st
import easyocr
from PIL import Image

def ocr_image(image):
    # Sử dụng EasyOCR để nhận diện văn bản
    reader = easyocr.Reader(['en']) # Chỉ định ngôn ngữ (ở đây là tiếng Anh)
    result = reader.readtext(image)
    return result

def main():
    st.title("Ứng dụng OCR sử dụng EasyOCR và Streamlit")

    uploaded_image = st.file_uploader("Tải lên hình ảnh", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Đọc hình ảnh từ file đã tải lên
        image = Image.open(uploaded_image)
        st.image(image, caption='Hình ảnh được tải lên', use_column_width=True)

        if st.button('Nhận diện văn bản'):
            # Thực hiện OCR trên hình ảnh và hiển thị kết quả
            result = ocr_image(image)
            for detection in result:
                st.write(detection[1]) # Hiển thị văn bản đã nhận diện

if __name__ == "__main__":
    main()
