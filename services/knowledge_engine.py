from knowledge.functional_group import FUNCTIONAL_GROUP_RULES


def build_knowledge(groups):

    knowledge = []

    for group in groups:

        info = FUNCTIONAL_GROUP_RULES.get(group)

        if info:

            knowledge.extend(info["facts"])

    return knowledge