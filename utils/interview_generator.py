import json
import os


def load_interview_questions():
    """
    Load interview questions from the JSON file.
    """

    current_dir = os.path.dirname(__file__)
    json_path = os.path.join(current_dir, "..", "data", "interview_questions.json")

    try:
        with open(json_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Interview question database not found.")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON format in interview_questions.json")
        return {}


def generate_interview_questions(technical_skills):
    """
    Return interview questions for the extracted technical skills.
    """

    question_db = load_interview_questions()

    interview_questions = {}

    for skill in technical_skills:

        for db_skill in question_db:

            if skill.lower() == db_skill.lower():

                interview_questions[db_skill] = question_db[db_skill]

    return interview_questions