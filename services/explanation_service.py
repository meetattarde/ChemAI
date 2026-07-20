from rdkit import Chem


def generate_explanation(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return "No explanation available."

    explanation = []

    ring_count = mol.GetRingInfo().NumRings()

    if ring_count:
        explanation.append(
            f"This compound contains {ring_count} ring(s)."
        )

    if any(atom.GetIsAromatic() for atom in mol.GetAtoms()):
        explanation.append(
            "It contains an aromatic system."
        )

    oxygen = sum(
        atom.GetSymbol() == "O"
        for atom in mol.GetAtoms()
    )

    nitrogen = sum(
        atom.GetSymbol() == "N"
        for atom in mol.GetAtoms()
    )

    if oxygen:
        explanation.append(
            "Oxygen atoms increase polarity."
        )

    if nitrogen:
        explanation.append(
            "Nitrogen atoms may contribute to basicity."
        )

    if mol.GetNumHeavyAtoms() > 10:
        explanation.append(
            "This is a relatively large organic molecule."
        )

    explanation.append(
        "Chemical properties depend on functional groups and molecular structure."
    )

    return " ".join(explanation)