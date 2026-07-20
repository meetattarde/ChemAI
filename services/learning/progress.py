def learning_progress(compound):

    score = 0

    if compound.get("properties"):
        score += 20

    if compound.get("groups"):
        score += 20

    if compound.get("reactivity"):
        score += 20

    if compound.get("brain"):
        score += 20

    if compound.get("similar"):
        score += 20

    return score