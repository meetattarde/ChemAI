from rdkit import Chem


def count_atoms(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    atoms = {}

    for atom in mol.GetAtoms():

        symbol = atom.GetSymbol()

        atoms[symbol] = atoms.get(symbol, 0) + 1

    return atoms