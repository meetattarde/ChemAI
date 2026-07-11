from rdkit import Chem
from rdkit.Chem import Descriptors


def get_descriptors(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    return {
        "Exact Mass": round(Descriptors.ExactMolWt(mol), 4),
        "Heavy Atom Count": Descriptors.HeavyAtomCount(mol),
        "Valence Electrons": Descriptors.NumValenceElectrons(mol),
        "Radical Electrons": Descriptors.NumRadicalElectrons(mol),
        "Fraction CSP3": round(Descriptors.FractionCSP3(mol), 3)
    }