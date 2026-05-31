from dotenv import load_dotenv
import os

load_dotenv()

from langchain_openai import ChatOpenAI
from prompts.extract_prompt import extract_prompt

llm = ChatOpenAI(model="gpt-4o-mini")

extract_chain = extract_prompt | llm