import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")

if AZURE_OPENAI_KEY is None:
    raise ValueError("Missing AZURE_OPENAI_KEY in environment variables")