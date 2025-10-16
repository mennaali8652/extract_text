import streamlit as st
import os, io, subprocess
from PIL import Image
import pytesseract
from pdf2image import convert_from_bytes
from langchain_community.document_loaders import PyPDFLoader

st.title("📄 File Text Extractor")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "png", "jpg", "jpeg", "txt", "docx", "pptx"])

def extract_text_from_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes)).convert("L")
    return pytesseract.image_to_string(image).strip()

def extract_text_from_scanned_pdf(file_bytes):
    images = convert_from_bytes(file_bytes)
    text = ""
    for img in images:
        gray = img.convert("L")
        text += pytesseract.image_to_string(gray) + "\n"
    return text.strip()

def extract_text_from_pdf_text(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return "\n".join([d.page_content for d in docs]).strip()

def convert_to_pdf(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()
    if file_extension == ".pdf":
        return file_path
    elif file_extension in [".txt", ".docx", ".pptx"]:
        output_dir = os.path.dirname(file_path)
        output_pdf_path = f"{file_name}.pdf"
        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", "pdf", file_path, "--outdir", output_dir],
            check=True
        )
        return output_pdf_path
    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

if uploaded_file is not None:
    filename = uploaded_file.name.lower()
    file_bytes = uploaded_file.read()
    
    with open(filename, "wb") as f:
        f.write(file_bytes)

    extracted_text = ""
    file_type = ""

    if filename.endswith(".pdf"):
        try:
            text = extract_text_from_pdf_text(filename)
            if text:
                extracted_text = text
                file_type = "pdf_text"
            else:
                extracted_text = extract_text_from_scanned_pdf(file_bytes)
                file_type = "pdf_scanned"
        except:
            extracted_text = extract_text_from_scanned_pdf(file_bytes)
            file_type = "pdf_scanned"

    elif filename.endswith((".jpg", ".jpeg", ".png")):
        extracted_text = extract_text_from_image(file_bytes)
        file_type = "image"

    elif filename.endswith((".txt", ".docx", ".pptx")):
        pdf_path = convert_to_pdf(filename)
        extracted_text = extract_text_from_pdf_text(pdf_path)
        file_type = "converted_to_pdf"

    if extracted_text:
        st.subheader(f"✅ Extracted Content ({file_type})")
        st.text_area("Text", extracted_text, height=400)
    else:
        st.error("❌ No text could be extracted.")
