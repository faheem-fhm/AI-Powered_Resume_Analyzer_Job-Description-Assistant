from utils.job_info_extractor import extract_job_info

sample = """
Job Title: Data Analyst

Company: ABC Technologies

Experience: 2-4 Years

Location: Chennai

Salary: ₹6 LPA

Employment Type: Full Time

Education: B.Tech

Python SQL Power BI
"""

info = extract_job_info(sample)

print(info)