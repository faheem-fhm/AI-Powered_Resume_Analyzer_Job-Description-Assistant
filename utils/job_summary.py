def generate_job_summary(job_info, technical_skills, soft_skills):
    """
    Generate a concise summary of the job description.
    """

    summary = {
        "job_title": job_info.get("job_title", "Not Found"),
        "experience": job_info.get("experience", "Not Found"),
        "education": job_info.get("education", "Not Found"),
        "technical_skills": technical_skills,
        "soft_skills": soft_skills,
        "responsibilities": job_info.get("responsibilities", [])
    }

    return summary