from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
Extract only:

Skills
Tools
Experience

Return JSON only.

Resume:
{resume}
"""
)