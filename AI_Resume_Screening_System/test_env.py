from dotenv import load_dotenv
import os

load_dotenv()

print("OPENAI KEY:", os.getenv("OPENAI_API_KEY"))
print("LANGCHAIN KEY:", os.getenv("LANGCHAIN_API_KEY"))