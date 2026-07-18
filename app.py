from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename


from utils.file_reader import extract_text
from utils.text_preprocessing import preprocess_text
from utils.skill_extractor import extract_skills
from utils.job_info_extractor import extract_job_info
from utils.resume_matcher import extract_resume_details
from utils.suggestion_generator import generate_suggestions
from utils.job_summary import generate_job_summary
from utils.interview_generator import generate_interview_questions
from utils.chatbot import get_chatbot_response
from flask import jsonify
# ===========================
# PDF Report Imports
# ===========================

from flask import send_file
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib.units import inch


app = Flask(__name__)
# ==========================
# Store Latest Analysis
# ==========================

latest_analysis = {}

# ==========================
# Upload Configuration
# ==========================

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder automatically
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ==========================
# Check Allowed File
# ==========================

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )

# ==========================
# Home Page
# ==========================

# ============================================================
# PDF REPORT GENERATOR
# ============================================================

def create_pdf_report():

    pdf_file = "Resume_Analysis_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER

    heading_style = styles["Heading2"]

    normal_style = styles["BodyText"]

    elements = []

    # ========================================================
    # TITLE
    # ========================================================

    elements.append(
        Paragraph(
            "AI Resume Analysis Report",
            title_style
        )
    )

    elements.append(Spacer(1, 20))

    # ========================================================
    # ATS SCORE
    # ========================================================

    elements.append(
        Paragraph(
            "<b>ATS Score</b>",
            heading_style
        )
    )

    ats_table = Table([
        ["ATS Score", f"{latest_analysis['ats_score']} %"]
    ])

    ats_table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(-1,0),colors.green),

        ("TEXTCOLOR",(0,0),(-1,-1),colors.white),

        ("ALIGN",(0,0),(-1,-1),"CENTER"),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BOTTOMPADDING",(0,0),(-1,-1),8)

    ]))

    elements.append(ats_table)

    elements.append(Spacer(1,20))

    # ========================================================
    # JOB INFORMATION
    # ========================================================

    elements.append(
        Paragraph(
            "<b>Job Information</b>",
            heading_style
        )
    )

    job = latest_analysis["job_info"]

    job_table = Table([

        ["Job Title", job["job_title"]],

        ["Company", job["company"]],

        ["Location", job["location"]],

        ["Salary", job["salary"]],

        ["Experience", job["experience"]],

        ["Employment Type", job["employment_type"]],

        ["Education", job["education"]]

    ])

    job_table.setStyle(TableStyle([

        ("BACKGROUND",(0,0),(0,-1),colors.lightblue),

        ("GRID",(0,0),(-1,-1),1,colors.black),

        ("BOTTOMPADDING",(0,0),(-1,-1),6)

    ]))

    elements.append(job_table)

    elements.append(Spacer(1,20))
        # ========================================================
    # Resume Skills
    # ========================================================

    elements.append(Paragraph("<b>Resume Skills</b>", heading_style))

    for skill in latest_analysis["resume_skills"]:
        elements.append(Paragraph(f"• {skill}", normal_style))

    elements.append(Spacer(1,15))


    # ========================================================
    # Matched Skills
    # ========================================================

    elements.append(Paragraph("<b>Matched Skills</b>", heading_style))

    for skill in latest_analysis["matched_skills"]:
        elements.append(Paragraph(f"✔ {skill}", normal_style))

    elements.append(Spacer(1,15))


    # ========================================================
    # Missing Skills
    # ========================================================

    elements.append(Paragraph("<b>Missing Skills</b>", heading_style))

    for skill in latest_analysis["missing_skills"]:
        elements.append(Paragraph(f"✘ {skill}", normal_style))

    elements.append(Spacer(1,15))


    # ========================================================
    # AI Suggestions
    # ========================================================

    elements.append(Paragraph("<b>AI Resume Suggestions</b>", heading_style))

    for suggestion in latest_analysis["suggestions"]:
        elements.append(Paragraph(f"• {suggestion}", normal_style))

    elements.append(Spacer(1,15))


    # ========================================================
    # Job Summary
    # ========================================================

    elements.append(Paragraph("<b>Job Summary</b>", heading_style))

    summary = latest_analysis["job_summary"]

    elements.append(
        Paragraph(
            f"<b>Job Title:</b> {summary['job_title']}",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Experience:</b> {summary['experience']}",
            normal_style
        )
    )

    elements.append(
        Paragraph(
            f"<b>Education:</b> {summary['education']}",
            normal_style
        )
    )

    elements.append(Spacer(1,15))


    # ========================================================
    # Interview Questions
    # ========================================================

    elements.append(
        Paragraph(
            "<b>Interview Questions</b>",
            heading_style
        )
    )

    interview = latest_analysis["interview_questions"]

    for skill, questions in interview.items():

        elements.append(
            Paragraph(
                f"<b>{skill}</b>",
                normal_style
            )
        )

        for q in questions:
            elements.append(
                Paragraph(
                    f"• {q}",
                    normal_style
                )
            )

        elements.append(Spacer(1,10))


    # ========================================================
    # Generate PDF
    # ========================================================

    doc.build(elements)

    return pdf_file

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        # Get uploaded files
        resume_file = request.files.get("resume_file")
        job_file = request.files.get("job_file")

        # Validation
        if not resume_file or resume_file.filename == "":
            return "Please upload your Resume."

        if not job_file or job_file.filename == "":
            return "Please upload your Job Description."

        if allowed_file(resume_file.filename) and allowed_file(job_file.filename):

            # Save Resume
            resume_filename = secure_filename(resume_file.filename)
            resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_filename)
            resume_file.save(resume_path)

            # Save Job Description
            job_filename = secure_filename(job_file.filename)
            job_path = os.path.join(app.config["UPLOAD_FOLDER"], job_filename)
            job_file.save(job_path)

            # Read files
            resume_text = extract_text(resume_path)
            jd_text = extract_text(job_path)

            resume_data = extract_resume_details(resume_path)

            resume_technical = resume_data["technical_skills"]
            resume_soft = resume_data["soft_skills"]

            # Process JD
            job_info = extract_job_info(jd_text)
            cleaned_text = preprocess_text(jd_text)
            skills = extract_skills(cleaned_text)

            # Extract skills
            technical_skills = skills["technical"]
            soft_skills = skills["soft"]

            # Generate Job Summary
            job_summary = generate_job_summary(
                job_info,
                technical_skills,
                soft_skills
            )

            # Generate Interview Questions
            interview_questions = generate_interview_questions(technical_skills)
            global latest_job_info
            global latest_technical_skills
            global latest_soft_skills

            latest_job_info = job_info
            latest_technical_skills = technical_skills
            latest_soft_skills = soft_skills
            # ==========================
            # Compare Resume & JD Skills
            # ==========================

            jd_skills = skills["technical"]

            matched_skills = list(set(jd_skills) & set(resume_technical))
            missing_skills = list(set(jd_skills) - set(resume_technical))

            # ==========================
            # ATS Score
            # ==========================

            if len(jd_skills) > 0:
                ats_score = round((len(matched_skills) / len(jd_skills)) * 100)
            else:
                ats_score = 0

            # Generate AI Suggestions
            suggestions = generate_suggestions(missing_skills)
            # ==========================
            # Save Latest Analysis
            # ==========================

            global latest_analysis

            latest_analysis = {
                "ats_score": ats_score,
                "job_info": job_info,
                "resume_skills": resume_technical,
                "matched_skills": matched_skills,
                "missing_skills": missing_skills,
                "suggestions": suggestions,
                "job_summary": job_summary,
                "interview_questions": interview_questions
            }




            return render_template(
            "result.html",
            extracted_text=jd_text,
            cleaned_text=cleaned_text,
            technical_skills=technical_skills,
            soft_skills=soft_skills,
            job_info=job_info,
            resume_skills=resume_technical,
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            ats_score=ats_score,
            suggestions=suggestions,
            job_summary=job_summary,
            interview_questions=interview_questions
        )

        return "❌ Only PDF, DOCX and TXT files are allowed."

    return render_template("index.html")


@app.route("/chatbot", methods=["POST"])
def chatbot():

    data = request.get_json()

    user_question = data.get("message", "")

    response = get_chatbot_response(
        user_question,
        latest_job_info,
        latest_technical_skills,
        latest_soft_skills
    )

    return jsonify({
        "response": response
    })

    # ============================================================
# DOWNLOAD PDF REPORT
# ============================================================

@app.route("/download_pdf")
def download_pdf():

    pdf_file = create_pdf_report()

    return send_file(
        pdf_file,
        as_attachment=True,
        download_name="AI_Resume_Analysis_Report.pdf"
    )

# ==========================
# Run App
# ==========================

if __name__ == "__main__":
    app.run(debug=True)