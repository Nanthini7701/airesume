import re
import fitz  # PyMuPDF
import docx
import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS_DB = [
    "python", "django", "flask", "html", "css", "javascript",
    "react", "sql", "mysql", "postgresql", "api", "rest",
    "machine learning", "ai", "git", "github"
]


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    return ""


def extract_email(text):
    match = re.search(r"[\\w\\.-]+@[\\w\\.-]+", text)
    return match.group(0) if match else None


def extract_phone(text):
    match = re.search(r"(\\+91|0)?[6-9][0-9]{9}", text)
    return match.group(0) if match else None


def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None


def extract_skills(text):
    text = text.lower()
    skills = [skill for skill in SKILLS_DB if skill in text]
    return list(set(skills))


def calculate_ats_score(skills):
    if not skills:
        return 30
    score = min(100, 40 + len(skills) * 8)
    return score
