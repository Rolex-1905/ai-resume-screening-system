# AI Resume Screening System using LangChain and LangSmith

## Project Objective

The objective of this project is to build an AI-powered resume screening system that automatically evaluates candidate resumes against a job description by extracting skills, comparing them with requirements, assigning a score between 0–100, and providing an explanation using LangChain pipelines with LangSmith tracing for transparency.

---

## Project Problem Statement

Traditional resume screening is:
- Manual  
- Time-consuming  
- Biased  
- Inconsistent  

This project solves the problem by automating candidate evaluation using Large Language Model (LLM) pipelines that ensure faster, standardized, and explainable recruitment decisions.

---

## Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Backend logic and processing |
| LangChain | Pipeline creation and orchestration |
| LangSmith | Tracing and monitoring pipeline execution |
| OpenAI API | LLM-based reasoning and generation |
| Streamlit | Web-based user interface |
| Prompt Engineering | Skill extraction, matching, and scoring logic |

---

## System Workflow
Resume Upload
↓
Skill Extraction
↓
Skill Matching
↓
Score Generation
↓
Explanation Generation
↓
Comparison Dashboard
↓
Best Candidate Recommendation

---

## Project Architecture

The system behaves like an AI-based Applicant Tracking System (ATS):

User uploads resumes → System extracts skills → Compares with job description → Generates score → Provides explanation → Ranks candidates → Recommends best candidate

---

## Project Folder Structure
## Project Structure

```bash
Task_2/
├── AI_Resume_Screening_System/
│   ├── chains/
│   │   ├── extract_chain.py
│   │   ├── match_chain.py
│   │   └── score_chain.py
│   │
│   ├── prompts/
│   │   ├── extract_prompt.py
│   │   ├── match_prompt.py
│   │   └── score_prompt.py
│   │
│   ├── utils/
│   │   └── resume_parser.py
│   │  
│   ├── .env
│   ├── app.py
│   ├── main.py
│   ├── job_description.txt
│   ├── requirements.txt
│   └── test_env.py
│   
├── Outputs/
│   ├── LangSmith_Tracing.jpg
│   ├── Output_1.jpg
│   └── Output_2.jpg
│
├── resumes/
│    ├── Arun Kumar Average.pdf
│    ├── Rahul Sharma Strength.txt
│    └── Ramesh weak.txt
│
└── README.md
```

## Notes (for README clarity)

- project/ contains the full LangChain + Streamlit application
- chains/ → extraction, matching, scoring logic
- prompts/ → LLM prompt templates
- utils/ → resume parsing utilities
- resumes/ → sample test resumes (PDF/TXT)
- Explanation-* files → step-by-step documentation of system reasoning
- test_env.py → environment validation script
- .env → API keys and LangSmith configuration
  
Each module is designed for modularity and separation of concerns.


## How to Run the Project

### 1. Download the Repository

### 2. Navigate to Project Folder
```bash
cd Task_2/AI_Resume_Screening_System
```

### 3. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Add API Keys

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
```

### 6. Run the Application
```bash
streamlit run app.py
```

### 7. Open in Browser
```
http://localhost:8501
```

---

## ⚠️ Notes
- Use Python 3.8+
- Ensure all dependencies are installed
- If Streamlit is missing:
```bash
pip install streamlit
```
## Input Stage

The system accepts:
- Multiple resumes (TXT / PDF formats)
- One job description

These inputs are uploaded via a Streamlit interface.

---

## Skill Extraction

Resumes are processed using a LangChain extraction pipeline.

### Input:
Raw resume text

### Output:
Structured JSON containing:
- Skills
- Tools
- Experience

This converts unstructured resume data into structured format for processing.

---

## Skill Matching

The extracted skills are compared against the job description.

### Output:
- Matched Skills
- Missing Skills
- Experience Match

This helps determine candidate suitability.

---

## Scoring Engine

Each candidate is assigned a score between 0 and 100 based on:
- Skill match percentage
- Missing critical skills
- Experience relevance

### Output Example:
Score: 75

---

## Explanation Generation

The system generates an explanation for each score, providing reasoning such as:
- Missing skills
- Experience gaps
- Strengths of the candidate

This enables explainable AI behavior.

---

## LangChain Pipeline Design

The system uses LCEL (LangChain Expression Language):


Pipeline stages:
- extract_chain
- match_chain
- score_chain

Each stage processes structured input and passes output forward.

---

## LangSmith Tracing

LangSmith is used for monitoring and debugging the pipeline.

It records:
- Inputs
- Outputs
- Prompt execution flow
- Chain-level reasoning

Each resume generates a separate trace run, enabling full transparency of AI decision-making.

---

## Streamlit Web Application

The user interface allows:
- Uploading multiple resumes
- Entering job descriptions
- Viewing results instantly

### Output Display:
- Extracted skills
- Matched skills
- Missing skills
- Score
- Explanation
- Candidate ranking
- Best candidate recommendation

---

## Comparison Dashboard

The system compares candidates in a tabular format:

- Candidate Name
- Score
- Match Level
- Matched Skills
- Missing Skills

This helps recruiters make data-driven decisions.

---

## Candidate Ranking System

Candidates are automatically ranked based on score:

Example:
- Candidate A → 92
- Candidate B → 65
- Candidate C → 12

Sorting is done in descending order of score.

---

## Best Candidate Recommendation

The system automatically selects the highest-scoring candidate as the recommended hire.

Logic:best_candidate = max(score)


---

## Skill Gap Analysis

The system identifies missing skills such as:
- TensorFlow
- PyTorch

This helps recruiters and candidates understand skill gaps.

---

## Score Classification

- 85–100 → Strong Candidate  
- 50–84 → Average Candidate  
- 0–49 → Weak Candidate  

---

## PDF and TXT Support

The system supports resume parsing using:
- TXT files
- PDF files (via pypdf)

---

## Environment Variables

OPENAI_API_KEY=your_key

LANGCHAIN_API_KEY=your_key

LANGCHAIN_TRACING_V2=true


These ensure secure API access and enable LangSmith tracing.

---

## Final System Output

The system generates:
- Extracted skills
- Matched skills
- Missing skills
- Score (0–100)
- Explanation
- Candidate ranking
- Comparison dashboard
- Best candidate recommendation
- Skill improvement suggestions

---

## Summary

This project implements a complete AI-driven ATS (Applicant Tracking System) using LangChain and LangSmith. It automates resume screening by combining LLM-based reasoning, structured prompt pipelines, and real-time traceability to ensure transparency, accuracy, and efficiency in recruitment workflows.
