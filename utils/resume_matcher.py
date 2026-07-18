from utils.file_reader import extract_text
from utils.text_preprocessing import preprocess_text
from utils.skill_extractor import extract_skills

def extract_resume_details(filepath):

    text = extract_text(filepath)
    cleaned_text = preprocess_text(text)
    skills = extract_skills(cleaned_text)

    return {
        "text": text,
        "technical_skills": skills["technical"],
        "soft_skills": skills["soft"]
    }