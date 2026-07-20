from rdkit import Chem

from chemistry.functional_groups import detect_functional_groups


def suggest_reactions(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return []

    groups = detect_functional_groups(smiles)

    reactions = []

    if "Alcohol" in groups:
        reactions.extend([
            "Oxidation",
            "Dehydration",
            "Esterification"
        ])

    if "Alkene" in groups:
        reactions.extend([
            "Hydration",
            "Hydrogenation",
            "Halogenation"
        ])

    if "Alkyne" in groups:
        reactions.extend([
            "Hydrogenation",
            "Hydration"
        ])

    if "Benzene Ring" in groups:
        reactions.extend([
            "Nitration",
            "Sulfonation",
            "Chlorination",
            "Friedel-Crafts Alkylation",
            "Friedel-Crafts Acylation"
        ])

    if "Carboxylic Acid" in groups:
        reactions.extend([
            "Esterification",
            "Reduction"
        ])

    return sorted(set(reactions))