from database.search_database import search_compound
from database.database_manager import save_compound
from api.pubchem_api import fetch_compound
from chemistry.structure import generate_structure


def display_result(data):

    print("\n========== COMPOUND ==========\n")

    print("Name :", data["name"])
    print("Formula :", data["formula"])
    print("Molecular Weight :", data["molecular_weight"])
    print("IUPAC Name :", data["iupac_name"])
    print("SMILES :", data["smiles"])
    print("InChIKey :", data["inchikey"])
    print("PubChem CID :", data["pubchem_cid"])

    image = generate_structure(
        data["smiles"],
        data["name"]
    )

    if image:
        print("\nStructure Image :", image)
    else:
        print("\nStructure could not be generated.")


def search_compound_menu():

    compound = input("\nEnter compound name : ").strip().lower()

    result = search_compound(compound)

    if result:

        data = {
            "name": result[1],
            "formula": result[2],
            "molecular_weight": result[3],
            "iupac_name": result[4],
            "smiles": result[5],
            "inchikey": result[6],
            "pubchem_cid": result[7]
        }

        print("\nFound in local database.")
        display_result(data)
        return

    print("\nNot found locally.")
    print("Searching PubChem...\n")

    data = fetch_compound(compound)

    if data is None:
        print("Compound not found.")
        return

    save_compound(data)

    print("Downloaded from PubChem.")
    display_result(data)

    print("\nSaved into local database.")