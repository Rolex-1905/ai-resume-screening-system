import streamlit as st
import tempfile
import re
import pandas as pd
from main import run_pipeline


# ===============================
# Helper function
# ===============================

def extract_skills_from_matching(matching_text):

    matched = []
    missing = []

    matched_section = False
    missing_section = False

    for line in matching_text.split("\n"):

        if "Matched Skills" in line:
            matched_section = True
            missing_section = False
            continue

        if "Missing Skills" in line:
            matched_section = False
            missing_section = True
            continue

        if matched_section and "-" in line:
            matched.append(line.replace("-", "").strip())

        if missing_section and "-" in line:
            missing.append(line.replace("-", "").strip())

    return matched, missing


# ===============================
# Page configuration
# ===============================

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Screening System")

st.markdown("""
Upload multiple resumes and evaluate candidates automatically
using an AI-powered ATS screening pipeline.
""")


# ===============================
# Inputs
# ===============================

uploaded_resumes = st.file_uploader(
    "Upload Multiple Resumes (Strong / Average / Weak)",
    type=["txt", "pdf"],
    accept_multiple_files=True
)

job_description_input = st.text_area(
    "Paste Job Description Here",
    height=200
)


# ===============================
# Analyze button
# ===============================

if st.button("Analyze Resumes"):

    if not uploaded_resumes:

        st.warning("Please upload at least 3 resumes.")

    elif job_description_input.strip() == "":

        st.warning("Please paste a job description.")

    else:

        # Save job description
        with open("job_description.txt", "w", encoding="utf-8") as f:
            f.write(job_description_input)

        st.success("Processing resumes...")


        candidate_scores = []
        comparison_data = []


        # ===============================
        # Process each resume
        # ===============================

        for uploaded_resume in uploaded_resumes:

            file_extension = uploaded_resume.name.split(".")[-1]

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=f".{file_extension}"
            ) as tmp:

                tmp.write(uploaded_resume.read())
                resume_path = tmp.name


            result = run_pipeline(resume_path)

            st.markdown("---")

            st.subheader(f"Evaluation Report: {uploaded_resume.name}")


            # ===============================
            # Extracted Information
            # ===============================

            st.markdown("### Extracted Skills")

            extracted_skills = result["extracted"]["Skills"]

            for skill in extracted_skills:
                st.write(f"• {skill}")

            st.markdown("### Experience")

            st.write(result["extracted"]["Experience"])


            # ===============================
            # Matching Section
            # ===============================

            st.markdown("### Matching Result")

            matching_text = result["matched"]

            st.write(matching_text)


            matched_skills, missing_skills = extract_skills_from_matching(matching_text)


            # ===============================
            # Score Extraction
            # ===============================

            score_text = result["score"]

            match = re.search(r'\d+', score_text)

            score_number = int(match.group()) if match else 0


            candidate_scores.append(
                (uploaded_resume.name, score_number)
            )


            comparison_data.append({

                "Candidate": uploaded_resume.name,

                "Score": score_number,

                "Match Level":
                    "Strong" if score_number >= 85
                    else "Average" if score_number >= 50
                    else "Weak",

                "Matched Skills": ", ".join(matched_skills),

                "Missing Skills": ", ".join(missing_skills)
            })


            # ===============================
            # Score Display
            # ===============================

            st.markdown("### Candidate Match Score")

            st.metric(
                label="Score",
                value=f"{score_number}%"
            )

            st.progress(score_number / 100)


            # ===============================
            # Badge Classification
            # ===============================

            if score_number >= 85:

                st.success("🟢 Strong Candidate")

            elif score_number >= 50:

                st.warning("🟡 Average Candidate")

            else:

                st.error("🔴 Weak Candidate")


            # ===============================
            # Explanation Section
            # ===============================

            explanation_match = re.search(
                r'Explanation:\s*(.*)',
                score_text,
                re.DOTALL
            )

            explanation_text = (
                explanation_match.group(1)
                if explanation_match
                else score_text
            )

            st.markdown("### Explanation")

            st.write(explanation_text)


        # ===============================
        # Final Ranking Section
        # ===============================

        st.markdown("---")

        st.subheader("📊 Final Candidate Ranking")

        candidate_scores.sort(
            key=lambda x: x[1],
            reverse=True
        )

        for rank, (name, score) in enumerate(
            candidate_scores,
            start=1
        ):

            st.write(
                f"{rank}. {name} — {score}%"
            )


        # ===============================
        # Comparison Dashboard Table
        # ===============================

        st.markdown("---")

        st.subheader("📊 Candidate Comparison Dashboard")

        comparison_df = pd.DataFrame(comparison_data)

        st.dataframe(
            comparison_df,
            use_container_width=True
        )


        # ===============================
        # Best Candidate Recommendation
        # ===============================

        st.markdown("---")

        st.subheader("🏆 Recommended Candidate")

        best_candidate = candidate_scores[0]

        best_name = best_candidate[0]

        best_score = best_candidate[1]


        st.success(
            f"Top Candidate: {best_name} ({best_score}%)"
        )


        if best_score >= 85:

            st.info(
                "Candidate strongly matches required skills and experience."
            )

        elif best_score >= 50:

            st.info(
                "Candidate moderately matches requirements. Further evaluation recommended."
            )

        else:

            st.info(
                "Candidate does not meet minimum requirements."
            )


        # ===============================
        # Skill Gap Suggestions
        # ===============================

        st.markdown("---")

        st.subheader("📘 Skill Improvement Suggestions")

        for candidate in comparison_data:

            if candidate["Missing Skills"]:

                st.warning(
                    f"{candidate['Candidate']} should improve: "
                    f"{candidate['Missing Skills']}"
                )


        st.success("Screening completed successfully.")