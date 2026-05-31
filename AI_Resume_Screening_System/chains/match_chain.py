from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from prompts.match_prompt import match_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

match_chain = match_prompt | llm