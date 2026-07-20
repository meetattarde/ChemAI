def ask_ai(question, compound=None):

    if compound:

        return f"""
ChemAI Assistant

Question:
{question}

Current Compound:
{compound}

This feature is under development.

Soon ChemAI AI will answer chemistry questions,
reaction mechanisms,
IUPAC doubts,
NEET questions,
and much more.
"""

    return "Ask me anything about Chemistry!"