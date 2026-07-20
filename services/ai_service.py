import os
import requests

from services.learning.learning_engine import prepare_prompt
from services.learning.memory import add_message

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"


def ask_ai(compound_data, question, study_mode="NCERT", explain_level="standard"):

    prompt = prepare_prompt(
        compound_data,
        question,
        study_mode=study_mode,
        explain_level=explain_level,
        user_id="default"
    )

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
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

        answer = result["choices"][0]["message"]["content"]

        add_message(
            "default",
            "ChemAI",
            answer
        )

        return answer

    return str(result)