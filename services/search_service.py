from database.search_database import search_compound


def smart_search():

    compound = input("\nEnter compound name: ")

    result = search_compound(compound)

    if result:

        print("\nCompound Found!")
        print(f"Name : {result[1]}")
        print(f"Formula : {result[2]}")
        print(f"Molecular Weight : {result[3]}")

        # Show IUPAC Name only if it exists
        if len(result) > 4:
            print(f"IUPAC Name : {result[4]}")
        else:
            print("IUPAC Name : Not Available")

    else:

        print("\nCompound not found in local database.")
        print("Searching PubChem... (Coming in next step)")
