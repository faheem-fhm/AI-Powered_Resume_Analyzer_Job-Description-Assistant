import pdfplumber
from docx import Document


def read_txt(filepath):

    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def read_pdf(filepath):

    text = ""

    with pdfplumber.open(filepath) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(filepath):

    document = Document(filepath)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


def extract_text(filepath):

    extension = filepath.split(".")[-1].lower()

    if extension == "txt":
        return read_txt(filepath)

    elif extension == "pdf":
        return read_pdf(filepath)

    elif extension == "docx":
        return read_docx(filepath)

    return "Unsupported File"