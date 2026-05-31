from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["skills", "job_description"],
    template="""
Candidate Skills:
{skills}

Job Description:
{job_description}

Return:

Matched Skills
Missing Skills
Experience Match (Yes/No)
"""
)