from ai.reaction_database import REACTIONS


def get_reaction(compound, reaction):

    if not reaction:
        return None

    compound = compound.lower().strip()
    reaction = reaction.lower().strip()

    return REACTIONS.get((compound, reaction))