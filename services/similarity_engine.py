from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

from services.compound_service import get_compound_data

DATABASE = [
    "methanol",
    "ethanol",
    "propanol",
    "butanol",
    "benzene",
    "toluene",
    "phenol",
    "aniline",
    "acetone",
    "acetic acid"
]


def find_similar(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return []

    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2)

    results = []

    for compound in DATABASE:

        data = get_compound_data(compound)

        if not data:
            continue

        mol2 = Chem.MolFromSmiles(data["smiles"])

        if mol2 is None:
            continue

        fp2 = AllChem.GetMorganFingerprintAsBitVect(mol2, 2)

        score = DataStructs.TanimotoSimilarity(fp, fp2)

        if score > 0:
            results.append({
                "name": compound.title(),
                "score": round(score * 100, 1)
            })

    results.sort(key=lambda x: x["score"], reverse=True)

    return results[:5]