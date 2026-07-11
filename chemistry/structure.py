from rdkit import Chem
from rdkit.Chem import Draw
import os


IMAGE_FOLDER = "images"


def generate_structure(smiles, compound_name):

    os.makedirs(IMAGE_FOLDER, exist_ok=True)

    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        return None

    image_path = os.path.join(
        IMAGE_FOLDER,
        f"{compound_name}.png"
    )

    Draw.MolToFile(
        molecule,
        image_path,
        size=(600, 600)
    )

    return image_path