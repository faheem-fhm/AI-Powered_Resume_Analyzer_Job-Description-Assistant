def generate_suggestions(missing_skills):
    """
    Generate AI-style suggestions based on missing skills.
    """

    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Learn {skill}.")
        suggestions.append(f"Add {skill} projects to your resume.")
        suggestions.append(f"Include {skill} in your Skills section if you have experience.")

    if len(missing_skills) == 0:
        suggestions.append("Excellent! Your resume matches the job description very well.")
        suggestions.append("Keep your resume updated with your latest projects and certifications.")

    return suggestions