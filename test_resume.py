from utils.resume_matcher import extract_resume_details

resume = extract_resume_details("Mohamed_Faheem_AIML_Engineer.pdf")

print(resume["technical_skills"])
print(resume["soft_skills"])