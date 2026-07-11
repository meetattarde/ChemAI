from rdkit import Chem

FUNCTIONAL_GROUPS = {
    "Alcohol": "[OX2H]",
    "Phenol": "c[OX2H]",
    "Carboxylic Acid": "C(=O)[OX2H1]",
    "Aldehyde": "CX3H1",
    "Ketone": "#6][CX3[#6]",
    "Amine": "[NX3;H2,H1;!$(NC=O)]",
    "Amide": "C(=O)N",
    "Ester": "C(=O)O[#6]",
    "Ether": "OD2[#6]",
    "Alkene": "C=C",
    "Alkyne": "C#C",
    "Benzene Ring": "c1ccccc1",
    "Halide": "[F,Cl,Br,I]"
}


def detect_functional_groups(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return []

    detected = []

    for name, smarts in FUNCTIONAL_GROUPS.items():

        pattern = Chem.MolFromSmarts(smarts)

        if pattern and mol.HasSubstructMatch(pattern):
            detected.append(name)

    return detected