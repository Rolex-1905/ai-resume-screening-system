from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from prompts.score_prompt import score_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

score_chain = score_prompt | llm