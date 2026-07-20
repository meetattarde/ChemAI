from .study_mode import get_mode_prompt
from .memory import get_history


def build_prompt(compound_data, question, study_mode="NCERT", user_id="default"):

    history = get_history(user_id)

    history_text = ""

    for msg in history:
        history_text += f"{msg['role']}: {msg['message']}\n"

    prompt = f"""
You are ChemAI, an expert Chemistry Teacher.

Study Mode:
{get_mode_prompt(study_mode)}

Previous Conversation:
{history_text}

Compound Information

Name:
{compound_data.get("name")}

Formula:
{compound_data.get("formula")}

Molecular Weight:
{compound_data.get("molecular_weight")}

IUPAC Name:
{compound_data.get("iupac_name")}

SMILES:
{compound_data.get("smiles")}

Functional Groups:
{compound_data.get("groups")}

Properties:
{compound_data.get("properties")}

Safety:
{compound_data.get("safety")}

Reactivity:
{compound_data.get("reactivity")}

ChemAI Analysis:
{compound_data.get("brain")}

User Question:
{question}

Instructions:

- Answer scientifically.
- Keep answers accurate.
- Never invent chemistry facts.
- If asked for mechanisms, explain step by step.
- Follow the selected study mode.
- If the user asks a follow-up question, use the previous conversation.

"""

    return prompt