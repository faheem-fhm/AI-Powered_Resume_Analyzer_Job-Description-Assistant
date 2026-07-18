# AI Resume Analyzer & Job Description Skill Extractor

## Overview

AI Resume Analyzer is a Flask-based web application that helps job seekers evaluate their resumes against job descriptions. It extracts skills, calculates ATS compatibility, identifies missing skills, generates interview questions, provides resume improvement suggestions, and exports professional PDF reports.

---

## Features

- Resume Upload (PDF, DOCX, TXT)
- Job Description Upload
- Text Extraction
- NLP Text Preprocessing
- Technical & Soft Skill Extraction
- ATS Score Calculation
- Resume vs Job Description Matching
- Missing Skill Detection
- AI Resume Improvement Suggestions
- Job Summary Generation
- AI Interview Question Generator
- AI Chatbot Assistant
- PDF Report Download
- Responsive Dashboard

---

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- NLP
- spaCy
- NLTK
- Scikit-learn
- PDFMiner
- python-docx
- ReportLab

---

## Project Structure

```
AI_JOB_EXTRACTOR/
│── app.py
│── requirements.txt
│── runtime.txt
│── templates/
│── static/
│── utils/
│── uploads/
│── data/
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI_JOB_EXTRACTOR.git
```

Move into the project folder

```bash
cd AI_JOB_EXTRACTOR
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the spaCy model

```bash
python -m spacy download en_core_web_sm
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Future Improvements

- User Authentication
- Analysis History
- Database Integration
- Excel Report Export
- Cloud Deployment
- Docker Support

---

## Author

**Mohamed Faheem**

GitHub: https://github.com/faheem-fhm

LinkedIn: https://www.linkedin.com/in/mohamed-faheemfhm