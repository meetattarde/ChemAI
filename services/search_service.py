from database.search_database import search_compound
from database.database_manager import save_compound
from api.pubchem_api import fetch_compound
from utils.logger import log


def search_compound_menu():

    compound = input("\nEnter compound name : ").strip()

    log(f"Searching for {compound}")

    result = search_compound(compound)

    if result:

        log(f"{compound} found in local database")

        print("\n========== FOUND IN LOCAL DATABASE ==========\n")

        print("Name :", result[1])
        print("Formula :", result[2])
        print("Molecular Weight :", result[3])
        print("IUPAC Name :", result[4])
        print("SMILES :", result[5])
        print("InChIKey :", result[6])
        print("PubChem CID :", result[7])

        return

    log(f"{compound} not found locally")
    log("Searching PubChem")

    print("\nNot found locally.")
    print("Searching PubChem...\n")

    data = fetch_compound(compound)

    if data is None:

        log(f"{compound} not found on PubChem")

        print("Compound not found.")

        return

    save_compound(data)

    log(f"{compound} downloaded from PubChem")
    log(f"{compound} saved into SQLite database")

    print("========== DOWNLOADED ==========\n")

    print("Name :", data["name"])
    print("Formula :", data["formula"])
    print("Molecular Weight :", data["molecular_weight"])
    print("IUPAC Name :", data["iupac_name"])
    print("SMILES :", data["smiles"])
    print("InChIKey :", data["inchikey"])
    print("PubChem CID :", data["pubchem_cid"])

    print("\nSaved to local database.")