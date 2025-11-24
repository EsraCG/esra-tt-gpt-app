from src.config import AZURE_OPENAI_KEY
import os
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AZURE_OPENAI_KEY")
API_URL = "https://open-ai-resource-rob.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-08-01-preview"
HEADERS = {
    "Content-Type": "application/json",
    "api-key": AZURE_OPENAI_KEY
}


async def ask_gpt(prompt: str) -> str:
    payload = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]
