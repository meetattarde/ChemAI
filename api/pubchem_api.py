import requests


def get_compound(name):

    url = (
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{name}/property/MolecularFormula,MolecularWeight,IUPACName/JSON"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()["PropertyTable"]["Properties"][0]

    return {
        "name": name.lower(),
        "formula": data["MolecularFormula"],
        "weight": data["MolecularWeight"],
        "iupac": data.get("IUPACName", "Not Available")
    }