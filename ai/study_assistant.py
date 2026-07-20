def answer_question(compound_name, question):

    compound = compound_name.lower()
    question = question.lower()

    if compound == "benzene":

        if "aromatic" in question:
            return (
                "Benzene is aromatic because it is a planar cyclic molecule "
                "with 6 delocalized pi electrons that satisfy Hückel's 4n+2 rule."
            )

        elif "uses" in question:
            return (
                "Benzene is used in the manufacture of plastics, dyes, "
                "detergents, medicines and many industrial chemicals."
            )

        elif "polar" in question:
            return (
                "Benzene is non-polar because its electron distribution is "
                "symmetrical and it has no permanent dipole moment."
            )

    return (
        "Sorry, I don't have an answer for that yet. "
        "This topic will be supported in future ChemAI updates."
    )