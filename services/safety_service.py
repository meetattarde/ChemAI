from ai.safety import safety_analysis


def get_safety(compound):

    if not compound:
        return None

    return safety_analysis(compound)