from rdkit import Chem

FUNCTIONAL_GROUPS = {
    "Alcohol": "[OX2H]",
    "Phenol": "c[OX2H]",
    "Carboxylic Acid": "[CX3](=O)[OX2H1]",
    "Aldehyde": "[CX3H1](=O)",
    "Ketone": "[#6][CX3](=O)[#6]",
    "Amine": "[NX3;H2,H1;!$(NC=O)]",
    "Amide": "[NX3][CX3](=O)",
    "Ester": "[CX3](=O)[OX2][#6]",
    "Ether": "[OD2]([#6])[#6]",
    "Alkene": "[CX3]=[CX3]",
    "Alkyne": "[CX2]#[CX2]",
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

        if pattern is not None and mol.HasSubstructMatch(pattern):
            detected.append(name)

    return detected