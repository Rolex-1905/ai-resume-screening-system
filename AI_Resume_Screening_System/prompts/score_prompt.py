from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_result"],
    template="""
Based on the matching result below:

{match_result}

Return:

Score: number between 0–100

Explanation:
Explain briefly why this score was assigned.
"""
)