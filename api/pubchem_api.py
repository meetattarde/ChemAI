import requests
from datetime import datetime


def fetch_compound(name):

    url = (
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{name}/property/"
        "MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES,InChIKey/JSON"
    )

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("PubChem Error:", response.status_code)
            print(response.text)
            return None

        properties = response.json()["PropertyTable"]["Properties"][0]

        return {
            "name": name.lower(),
            "formula": properties.get("MolecularFormula", ""),
            "molecular_weight": properties.get("MolecularWeight", 0),
            "iupac_name": properties.get("IUPACName", ""),
            "smiles": properties.get("CanonicalSMILES", ""),
            "inchikey": properties.get("InChIKey", ""),
            "pubchem_cid": 0,
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    except Exception as e:
        print("Error:", e)
        return None