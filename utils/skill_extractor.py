import json
import re

# Load skill database
with open("data/skills.json", "r", encoding="utf-8") as file:
    skills_db = json.load(file)

technical_skills = skills_db["technical_skills"]
soft_skills = skills_db["soft_skills"]


def extract_skills(cleaned_text):

    text = cleaned_text.lower()

    technical_found = []
    soft_found = []

    # Extract Technical Skills
    for skill in technical_skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            technical_found.append(skill)

    # Extract Soft Skills
    for skill in soft_skills:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            soft_found.append(skill)

    technical_found = sorted(list(set(technical_found)))
    soft_found = sorted(list(set(soft_found)))

    return {
        "technical": technical_found,
        "soft": soft_found
    }