from database.all_compounds import get_all_compounds
from database.search_database import search_compound
from chemistry.similarity import similarity


def similarity_search_menu():

    compound = input("\nEnter compound name : ").strip().lower()

    result = search_compound(compound)

    if result is None:
        print("\nCompound not found in local database.")
        print("Search it once from PubChem first.\n")
        return

    smiles = result[5]

    if not smiles:
        print("\nNo SMILES available.\n")
        return

    compounds = get_all_compounds()

    scores = []

    for name, other_smiles in compounds:

        if name == compound:
            continue

        score = similarity(smiles, other_smiles)

        scores.append((name, score))

    scores.sort(key=lambda x: x[1], reverse=True)

    print("\nMost Similar Compounds")
    print("-" * 40)

    for name, score in scores[:5]:
        print(f"{name:<20} {score}")