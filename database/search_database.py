from database.search_database import search_compound
from database.database_manager import save_compound
from api.pubchem_api import get_compound


def smart_search():

    compound = input("\nEnter compound name : ")

    result = search_compound(compound)

    if result:

        print("\nFound in Local Database\n")

        print("Name :", result[1])
        print("Formula :", result[2])
        print("Weight :", result[3])

        if len(result) > 4:
            print("IUPAC :", result[4])

    else:

        print("\nSearching PubChem...\n")

        data = get_compound(compound)

        if data is None:

            print("Compound Not Found.")

            return

        print("Downloaded Successfully!\n")

        print("Name :", data["name"])
        print("Formula :", data["formula"])
        print("Weight :", data["weight"])
        print("IUPAC :", data["iupac"])

        save_compound(
            data["name"],
            data["formula"],
            data["weight"],
            data["iupac"]
        )

        print("\nSaved into ChemAI Database!")