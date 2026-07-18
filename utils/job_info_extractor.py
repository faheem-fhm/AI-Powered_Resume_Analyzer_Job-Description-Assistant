import re
import spacy

nlp = spacy.load("en_core_web_sm")


def extract_job_info(text):

    info = {
        "job_title": "Not Found",
        "company": "Not Found",
        "experience": "Not Found",
        "location": "Not Found",
        "salary": "Not Found",
        "employment_type": "Not Found",
        "education": "Not Found",
        "required_skills": [],
        "preferred_skills": [],
        "responsibilities": []
    }

    lower_text = text.lower()

    # -----------------------------
    # Job Title
    # -----------------------------
    job_titles = [

    # ==========================
    # Data Roles
    # ==========================
    "Data Analyst Intern",
    "Senior Data Analyst",
    "Junior Data Analyst",
    "Lead Data Analyst",
    "Data Analyst",

    "Data Scientist Intern",
    "Junior Data Scientist",
    "Senior Data Scientist",
    "Data Scientist",

    "Data Engineer Intern",
    "Junior Data Engineer",
    "Senior Data Engineer",
    "Data Engineer",

    "Business Intelligence Intern",
    "Business Intelligence Analyst",
    "BI Analyst",
    "BI Developer",

    "Business Analyst Intern",
    "Junior Business Analyst",
    "Business Analyst",

    "Power BI Intern",
    "Power BI Developer",
    "Power BI Analyst",

    "Tableau Developer",
    "Tableau Analyst",

    "Database Developer",
    "Database Administrator",
    "SQL Developer",

    # ==========================
    # AI / ML Roles
    # ==========================
    "AI Engineer Intern",
    "AI Engineer",

    "Machine Learning Intern",
    "Machine Learning Engineer Intern",
    "Machine Learning Engineer",

    "Deep Learning Engineer",
    "Computer Vision Engineer",
    "NLP Engineer",
    "Generative AI Engineer",
    "LLM Engineer",
    "Prompt Engineer",
    "AI Research Engineer",
    "AI Research Scientist",

    # ==========================
    # Software Roles
    # ==========================
    "Software Engineer Intern",
    "Software Developer Intern",
    "Software Engineer",
    "Software Developer",

    "Python Developer Intern",
    "Python Developer",

    "Java Developer Intern",
    "Java Developer",

    "C++ Developer",
    "C# Developer",
    ".NET Developer",

    # ==========================
    # Web Development
    # ==========================
    "Full Stack Developer Intern",
    "Full Stack Developer",

    "Frontend Developer Intern",
    "Frontend Developer",

    "Backend Developer Intern",
    "Backend Developer",

    "Web Developer Intern",
    "Web Developer",

    "React Developer",
    "Angular Developer",
    "Node.js Developer",

    # ==========================
    # Cloud / DevOps
    # ==========================
    "DevOps Engineer Intern",
    "DevOps Engineer",

    "Cloud Engineer",
    "Cloud Architect",

    "AWS Engineer",
    "Azure Engineer",
    "Google Cloud Engineer",

    "Site Reliability Engineer",

    # ==========================
    # Cyber Security
    # ==========================
    "Cyber Security Intern",
    "Cyber Security Analyst",
    "Security Engineer",
    "Network Security Engineer",
    "SOC Analyst",
    "Ethical Hacker",

    # ==========================
    # Testing
    # ==========================
    "QA Intern",
    "QA Engineer",
    "Test Engineer",
    "Automation Test Engineer",
    "Manual Test Engineer",

    # ==========================
    # Mobile
    # ==========================
    "Android Developer",
    "iOS Developer",
    "Flutter Developer",
    "React Native Developer",

    # ==========================
    # Embedded / IoT
    # ==========================
    "Embedded Engineer",
    "Firmware Engineer",
    "IoT Engineer",
    "Robotics Engineer",

    # ==========================
    # Networking
    # ==========================
    "Network Engineer",
    "System Administrator",
    "Linux Administrator",

    # ==========================
    # Support
    # ==========================
    "Technical Support Engineer",
    "Application Support Engineer",

    # ==========================
    # Internship Generic
    # ==========================
    "Software Intern",
    "Engineering Intern",
    "Data Intern",
    "AI Intern",
    "ML Intern",
    "Developer Intern",
    "Graduate Engineer Trainee",
    "Graduate Trainee",
    "Intern"
]

    for title in job_titles:
        if title.lower() in lower_text:
            info["job_title"] = title
            break

    # -----------------------------
    # Company
    # -----------------------------
    company_patterns = [
        r"company\s*[:\-]?\s*(.+)",
        r"organization\s*[:\-]?\s*(.+)"
    ]

    for pattern in company_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            info["company"] = match.group(1).strip().split("\n")[0]
            break

    # -----------------------------
    # Experience
    # -----------------------------
    experience_patterns = [
        r"\d+\s*[–-]\s*\d+\s*years?",
        r"\d+\+\s*years?",
        r"freshers?"
    ]

    for pattern in experience_patterns:
        match = re.search(pattern, lower_text, re.IGNORECASE)
        if match:
            info["experience"] = match.group().title()
            break

    # -----------------------------
    # Salary
    # -----------------------------
    salary_patterns = [
        r"₹\s*\d+\s*LPA\s*[–-]\s*₹?\d+\s*LPA",
        r"\d+\s*LPA\s*[–-]\s*\d+\s*LPA",
        r"₹\s*\d+\s*LPA",
        r"\d+\s*LPA"
    ]

    for pattern in salary_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            info["salary"] = match.group().strip()
            break

    # -----------------------------
    # Location
    # -----------------------------
    cities = [
        "Chennai",
        "Bangalore",
        "Hyderabad",
        "Pune",
        "Mumbai",
        "Delhi",
        "Remote"
    ]

    for city in cities:
        if city.lower() in lower_text:
            info["location"] = city
            break

    # -----------------------------
    # Employment Type
    # -----------------------------
    employment_types = [
        "Internship",
        "Full Time",
        "Part Time",
        "Hybrid",
        "Remote",
        "Contract"
    ]

    for emp in employment_types:
        if emp.lower() in lower_text:
            info["employment_type"] = emp
            break

    # -----------------------------
    # Education
    # -----------------------------
    education_keywords = [
        "b.tech",
        "b.e",
        "b.sc",
        "mca",
        "bachelor"
    ]

    for edu in education_keywords:
        if edu in lower_text:
            info["education"] = edu.upper()
            break

    # -----------------------------
    # Required Skills
    # -----------------------------
    if "required skills" in lower_text:
        info["required_skills"].append("Required Skills")

    # -----------------------------
    # Preferred Skills
    # -----------------------------
    if "preferred skills" in lower_text:
        info["preferred_skills"].append("Preferred Skills")

        # -----------------------------
    # Responsibilities
    # -----------------------------

    responsibility_keywords = [
        "responsibilities",
        "key responsibilities",
        "job responsibilities",
        "roles and responsibilities",
        "duties"
    ]

    lines = text.split("\n")

    capture = False

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        if any(keyword in clean_line.lower() for keyword in responsibility_keywords):
            capture = True
            continue

        if capture:

            # Stop when another section starts
            if any(word in clean_line.lower() for word in [
                "qualification",
                "education",
                "benefits",
                "salary",
                "experience",
                "skills"
            ]):
                break

            info["responsibilities"].append(clean_line)

    # -----------------------------
    # spaCy NER
    # -----------------------------
    doc = nlp(text)

    for ent in doc.ents:

        if (
            ent.label_ == "ORG"
            and info["company"] == "Not Found"
            and ent.text.lower() not in [
                "python",
                "sql",
                "excel",
                "tensorflow",
                "flask",
                "power bi",
                "numpy",
                "pandas"
            ]
        ):
            info["company"] = ent.text

        if (
            ent.label_ == "GPE"
            and info["location"] == "Not Found"
        ):
            info["location"] = ent.text

    info["required_skills"] = list(set(info["required_skills"]))
    info["preferred_skills"] = list(set(info["preferred_skills"]))

    return info