import os
import requests

conversation_memory = {}

API_KEY = os.getenv("OPENROUTER_API_KEY")
print("API Key:", API_KEY)

URL = "https://openrouter.ai/api/v1/chat/completions"


def build_prompt(compound, question):

    history = conversation_memory.get("history", "")

    return f"""
You are ChemAI, an expert Organic Chemistry Assistant.

Previous Conversation:
{history}

Compound Name:
{compound['name']}

Formula:
{compound['formula']}

IUPAC Name:
{compound['iupac_name']}

SMILES:
{compound['smiles']}

Functional Groups:
{", ".join(compound['groups'])}

Properties:
{compound['properties']}

Safety:
{compound['safety']}

ChemAI Analysis:
{compound['brain']}

User Question:
{question}

Answer in simple, scientifically accurate language.
"""


def ask_ai(compound, question):

    prompt = build_prompt(compound, question)

    conversation_memory["history"] = (
        conversation_memory.get("history", "")
        + f"\nUser: {question}"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost:5000",
        "X-Title": "ChemAI"
    }

    data = {
        "model": "google/gemini-2.5-flash",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 800,
        "temperature": 0.3
    }

    response = requests.post(
        URL,
        headers=headers,
        json=data
    )

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]

    return str(result)