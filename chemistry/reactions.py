from rdkit import Chem


def reaction_sites(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    atoms = []

    for atom in mol.GetAtoms():

        atoms.append({
            "Atom": atom.GetIdx(),
            "Element": atom.GetSymbol(),
            "Degree": atom.GetDegree(),
            "Hybridization": str(atom.GetHybridization()),
            "Aromatic": atom.GetIsAromatic()
        })

    return atoms