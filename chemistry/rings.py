from rdkit import Chem


def ring_information(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    ring_info = mol.GetRingInfo()

    return {
        "Ring Count": ring_info.NumRings(),
        "Aromatic Rings": ring_info.NumRings()
    }