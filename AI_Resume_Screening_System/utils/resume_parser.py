from pypdf import PdfReader


def extract_text_from_pdf(file_path):

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:

        text += page.extract_text() + "\n"

    return text


def extract_resume_text(file_path):

    if file_path.endswith(".pdf"):

        return extract_text_from_pdf(file_path)

    else:

        with open(file_path, "r", encoding="utf-8") as f:

            return f.read()