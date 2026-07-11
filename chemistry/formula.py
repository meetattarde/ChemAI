from rdkit import Chem
from rdkit.Chem import rdMolDescriptors


def molecular_formula(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    return rdMolDescriptors.CalcMolFormula(mol)