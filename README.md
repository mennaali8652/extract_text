# 📄 Streamlit File Text Extractor

A simple application built with Streamlit to extract text from different types of files:

- PDF (text-based or scanned)

- Images (JPG, PNG)

- Office files (DOCX, PPTX, TXT → converted to PDF, then text is extracted)

---
## 📄 Streamlit File Text Extractor
``` 
├── assets
├── tests
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```
---

## ⚙️ Requirements
```
- Python 3.9 or later
- Install:
  - [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
  - [Poppler](http://blog.alivate.com.au/poppler-windows/) (for Windows)
  - [LibreOffice](https://www.libreoffice.org/) (to convert DOCX/PPTX/TXT files into PDF)

```
---
## How to run locally

1. Clone the repository from GitHub
```bash
git clone https://github.com/mennaali8652/extract_text.git
```
2. Navigate into the project folder
```bash
cd extract_text
```
3. Install all required Python dependencies
```bash
pip install -r requirements.txt
```

4. Run the Streamlit application in Terminal
```bash
streamlit run app.py
```

---

## 🎥 Demo Video
Here is a quick demo of the application:

![Watch the demo](assets/demo.mp4)

---

## 🧪 Usage
```
- Upload a PDF file, an image, or a DOCX/PPTX/TXT file.

- The application will automatically choose the appropriate method to extract the text.

- The extracted result will be displayed in the application interface.

```
