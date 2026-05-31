from dotenv import load_dotenv
import os
import json

from utils.resume_parser import extract_resume_text

load_dotenv()

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain


def clean_json_output(text):

    # Remove markdown formatting if exists
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(text)

    except:
        return {"Skills": [], "Tools": [], "Experience": ""}


def run_pipeline(resume_file_path, job_description_path="job_description.txt"):

    from utils.resume_parser import extract_resume_text
    resume_text = extract_resume_text(resume_file_path)

    with open(job_description_path, "r", encoding="utf-8") as f:
        job_description = f.read()


    # STEP 1 — Extraction
    extracted = extract_chain.invoke({
        "resume": resume_text
    })

    extracted_output = extracted.content


    # Convert extraction output to structured JSON
    extracted_json = clean_json_output(extracted_output)


    candidate_skills = extracted_json.get("Skills", [])


    # STEP 2 — Matching
    matched = match_chain.invoke({
        "skills": candidate_skills,
        "job_description": job_description
    })

    matched_output = matched.content


    # STEP 3 — Scoring + Explanation
    score = score_chain.invoke({
        "match_result": matched_output
    })

    score_output = score.content


    return {
        "extracted": extracted_json,
        "matched": matched_output,
        "score": score_output
    }