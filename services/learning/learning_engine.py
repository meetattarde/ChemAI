from .prompt_builder import build_prompt
from .memory import add_message


def prepare_prompt(compound_data,
                   question,
                   study_mode="NCERT",
                   explain_level="standard",
                   user_id="default"):

    prompt = build_prompt(
        compound_data,
        question,
        study_mode,
        explain_level,
        user_id
    )

    add_message(
        user_id,
        "User",
        question
    )

    return prompt