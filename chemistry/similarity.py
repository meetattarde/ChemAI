from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs


def similarity(smiles1, smiles2):

    mol1 = Chem.MolFromSmiles(smiles1)
    mol2 = Chem.MolFromSmiles(smiles2)

    if mol1 is None or mol2 is None:
        return None

    fp1 = AllChem.GetMorganFingerprintAsBitVect(mol1, 2, 2048)
    fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 2, 2048)

    score = DataStructs.TanimotoSimilarity(fp1, fp2)

    return round(score, 3)