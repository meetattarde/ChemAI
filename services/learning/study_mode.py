MODES = {

    "NCERT":
"""
Explain exactly according to NCERT.
Avoid unnecessary details.
Focus on board exams.
""",

    "NEET":
"""
Teach like a top NEET faculty.
Mention important exceptions.
Include NCERT points.
Highlight common MCQs.
""",

    "JEE":
"""
Explain deeply.
Focus on conceptual understanding.
Include reasoning.
""",

    "College":
"""
Use undergraduate chemistry.
Include scientific terminology.
""",

    "Research":
"""
Answer professionally.
Use advanced chemistry language.
Include current scientific concepts when appropriate.
"""
}


def get_mode_prompt(mode):

    return MODES.get(mode, MODES["NCERT"])