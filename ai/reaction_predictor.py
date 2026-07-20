from ai.reaction_database import REACTIONS


def predict_reaction(compound, reaction):

    compound = compound.lower().strip()
    reaction = reaction.lower().strip()

    return REACTIONS.get(
        (compound, reaction),
        None
    )