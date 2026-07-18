def get_chatbot_response(user_question, job_info, technical_skills, soft_skills):
    """
    Generate chatbot responses based on the uploaded Job Description.
    """

    question = user_question.lower()

    # Skills
    if "skill" in question:
        if technical_skills:
            return "Required Technical Skills: " + ", ".join(technical_skills)
        return "No technical skills were found."

    # Soft Skills
    elif "soft skill" in question:
        if soft_skills:
            return "Required Soft Skills: " + ", ".join(soft_skills)
        return "No soft skills were found."

    # Experience
    elif "experience" in question:
        return f"Required Experience: {job_info.get('experience', 'Not Found')}"

    # Education
    elif "education" in question or "qualification" in question:
        return f"Required Education: {job_info.get('education', 'Not Found')}"

    # Job Title
    elif "job title" in question or "role" in question or "position" in question:
        return f"Job Title: {job_info.get('job_title', 'Not Found')}"

    # Company
    elif "company" in question:
        return f"Company: {job_info.get('company', 'Not Found')}"

    # Location
    elif "location" in question:
        return f"Location: {job_info.get('location', 'Not Found')}"

    # Salary
    elif "salary" in question:
        return f"Salary: {job_info.get('salary', 'Not Found')}"

    # Employment Type
    elif "employment" in question or "full time" in question or "part time" in question:
        return f"Employment Type: {job_info.get('employment_type', 'Not Found')}"

    # Responsibilities
    elif "responsibilit" in question or "duty" in question:
        responsibilities = job_info.get("responsibilities", [])

        if responsibilities:
            return "Responsibilities:\n- " + "\n- ".join(responsibilities)

        return "Responsibilities not found."

    # Default
    return (
        "I can answer questions about:\n"
        "• Skills\n"
        "• Experience\n"
        "• Education\n"
        "• Job Title\n"
        "• Company\n"
        "• Location\n"
        "• Salary\n"
        "• Employment Type\n"
        "• Responsibilities"
    )