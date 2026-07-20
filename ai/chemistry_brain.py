from chemistry.functional_groups import detect_functional_groups


def think(compound):

    thoughts = []

    smiles = compound["smiles"]

    groups = detect_functional_groups(smiles)

    if "Alcohol" in groups:

        thoughts.append(
            "This compound is an alcohol."
        )

        thoughts.append(
            "Alcohols are polar due to the hydroxyl (-OH) group."
        )

        thoughts.append(
            "Alcohols can undergo oxidation and esterification."
        )

    if "Carboxylic Acid" in groups:

        thoughts.append(
            "This compound is acidic."
        )

        thoughts.append(
            "It reacts with bases to form salts."
        )

    if "Alkene" in groups:

        thoughts.append(
            "This compound contains a carbon-carbon double bond."
        )

        thoughts.append(
            "It readily undergoes addition reactions."
        )

    if "Aromatic Ring" in groups:

        thoughts.append(
            "This molecule is aromatic."
        )

        thoughts.append(
            "Aromatic compounds are resonance stabilized."
        )

        thoughts.append(
            "They usually undergo electrophilic substitution."
        )

    return thoughts