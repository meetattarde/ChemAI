import requests
from datetime import datetime


def fetch_compound(name):

    url = (
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{name}/property/"
        f"MolecularFormula,MolecularWeight,IUPACName,CanonicalSMILES,InChIKey/JSON"
    )

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        json_data = response.json()

        print("\n========== PUBCHEM RESPONSE ==========")
        print(json_data)
        print("======================================\n")

        properties = json_data["PropertyTable"]["Properties"][0]

        return {
            "name": name.lower(),
            "formula": properties.get("MolecularFormula", ""),
            "molecular_weight": properties.get("MolecularWeight", 0),
            "iupac_name": properties.get("IUPACName", ""),
            "smiles": properties.get("ConnectivitySMILES", ""),
            "inchikey": properties.get("InChIKey", ""),
            "pubchem_cid": properties.get("CID", None),
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    except Exception as e:
        print("PubChem Error:", e)
        return None