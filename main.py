
main_code = '''
def extract_skills(text):
    skill_list = [
        "Python", "Machine Learning", "Data Analysis", "SQL",
        "Pandas", "NumPy", "Communication", "NLP",
        "Deep Learning", "Excel", "Tableau", "GitHub", "Jupyter"
    ]
    found = []
    for skill in skill_list:
        if skill.lower() in text.lower():
            found.append(skill)
    return found

def extract_resume_details(resume_text):
    skills = extract_skills(resume_text)

    experience = "Not mentioned"
    if "2 years" in resume_text.lower():
        experience = "2 years"
    elif "fresher" in resume_text.lower():
        experience = "Fresher"
    elif "no technical experience" in resume_text.lower():
        experience = "No technical experience"

    tools = []
    tool_list = ["Jupyter", "GitHub", "Tableau", "Excel", "MS Office", "Jupyter Notebook"]
    for tool in tool_list:
        if tool.lower() in resume_text.lower():
            tools.append(tool)

    return {
        "Skills": skills,
        "Experience": experience,
        "Tools": tools
    }

def match_resume_to_jd(resume_text, job_text):
    resume_details = extract_resume_details(resume_text)
    resume_skills = resume_details["Skills"]
    jd_skills = extract_skills(job_text)

    matched = [skill for skill in jd_skills if skill in resume_skills]
    missing = [skill for skill in jd_skills if skill not in resume_skills]

    return {
        "Matched Skills": matched,
        "Missing Skills": missing,
        "Experience Match": resume_details["Experience"],
        "Overall Match Summary": f"Matched {len(matched)} out of {len(jd_skills)} required skills."
    }

def calculate_score(match_result, job_text):
    total = len(extract_skills(job_text))
    matched = len(match_result["Matched Skills"])
    if total == 0:
        return 0
    return round((matched / total) * 100)

def generate_explanation(match_result, score):
    return (
        f"Candidate matched {len(match_result['Matched Skills'])} required skills. "
        f"Matched skills: {', '.join(match_result['Matched Skills']) if match_result['Matched Skills'] else 'None'}. "
        f"Missing skills: {', '.join(match_result['Missing Skills']) if match_result['Missing Skills'] else 'None'}. "
        f"Experience: {match_result['Experience Match']}. "
        f"Final Fit Score: {score}/100."
    )

def run_clean_pipeline(resume_text, candidate_name, job_description):
    print(f"\\n===== {candidate_name} =====\\n")

    extracted = extract_resume_details(resume_text)
    print("STEP 1: EXTRACT")
    print(extracted)

    matched = match_resume_to_jd(resume_text, job_description)
    print("\\nSTEP 2: MATCH")
    print(matched)

    score = calculate_score(matched, job_description)
    explanation = generate_explanation(matched, score)

    scored = {
        "Score": score,
        "Explanation": explanation
    }

    print("\\nSTEP 3: SCORE")
    print(scored)

    return {
        "candidate": candidate_name,
        "extracted": extracted,
        "matched": matched,
        "scored": scored
    }

job_description = """
Data Scientist Job

Required Skills:
- Python
- Machine Learning
- Data Analysis
- SQL
- Pandas
- NumPy
- Communication
"""

strong_resume = """
Name: Aditi
Skills: Python, Machine Learning, SQL, Pandas, NumPy, NLP, Deep Learning
Experience: 2 years in data science projects
Tools: Jupyter, GitHub, Tableau
"""

average_resume = """
Name: Rahul
Skills: Python, Data Analysis, Pandas, Excel
Experience: Fresher with internship
Tools: Jupyter Notebook, Excel
"""

weak_resume = """
Name: Sneha
Skills: Communication, teamwork, MS Word
Experience: No technical experience
Tools: MS Office
"""

result_strong = run_clean_pipeline(strong_resume, "Strong Candidate", job_description)
result_average = run_clean_pipeline(average_resume, "Average Candidate", job_description)
result_weak = run_clean_pipeline(weak_resume, "Weak Candidate", job_description)

with open("final_results.txt", "w") as f:
    for result in [result_strong, result_average, result_weak]:
        f.write(f"Candidate: {result['candidate']}\\n")
        f.write("EXTRACTED:\\n")
        f.write(str(result["extracted"]) + "\\n\\n")
        f.write("MATCHED:\\n")
        f.write(str(result["matched"]) + "\\n\\n")
        f.write("SCORED:\\n")
        f.write(str(result["scored"]) + "\\n")
        f.write("=" * 50 + "\\n")
'''

with open("main.py", "w") as f:
    f.write(main_code)

print("main.py created ✅")
