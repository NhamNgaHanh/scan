import easyocr as ocr  # OCR
import streamlit as st  # Web App
from PIL import Image  # Image Processing
import numpy as np  # Image Processing
from easyocr import Reader


def main():
    image = st.file_uploader(label="Upload your image here", type=["png", "jpg", "jpeg"])
    if image is not None:
        input_image = Image.open(image)  # read image
        st.image(input_image)  # display image
        reader = load_model()  # load model
        result = reader.readtext(np.array(input_image))
        result_text = []  # empty list for results
        for text in result:
            result_text.append(text[1])
        st.session_state["HA11"] = result_text
    else:
        st.write("Upload an Image")
HA1 = list st.session_state.get("HA11", None)
with st.container(height=150, border=True):
    for line in HA1:
        # Loại bỏ ký tự từ kí tự thứ năm trở đi
        # Kiểm tra nếu ký tự là một ký tự chữ cái hoặc số
        letters_only = ''.join(c for i, c in enumerate(line) if i > 4 or (c.isalpha() or c.isdigit() or c.isspace()))
        st.write(letters_only)
@st.cache
def load_model() -> Reader:
    return ocr.Reader(["en"], model_storage_directory=".")


if __name__ == "__main__":
    main()
