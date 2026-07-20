def build_reasoning(compound):

    explanation = []

    explanation.append(

        f"{compound['name'].title()} has the molecular formula "
        f"{compound['formula']}."

    )

    if compound["groups"]:

        explanation.append(

            "It contains the following functional groups: "

            + ", ".join(compound["groups"]) + "."

        )

    if compound["rings"]:

        explanation.append(

            f"Ring Analysis: {compound['rings']}."

        )

    if compound["lipinski"]:

        explanation.append(

            f"Drug-likeness: {compound['lipinski']}."

        )

    return " ".join(explanation)