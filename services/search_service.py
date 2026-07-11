from database.search_database import search_compound
from database.database_manager import save_compound
from api.pubchem_api import fetch_compound

from chemistry.structure import generate_structure
from chemistry.properties import calculate_properties
from chemistry.functional_groups import detect_functional_groups
from chemistry.lipinski import lipinski_analysis
from chemistry.formula import molecular_formula
from chemistry.atom_counter import count_atoms
from chemistry.rings import ring_information


def display_report(data):

    print("\n" + "=" * 60)
    print("                 CHEMAI REPORT")
    print("=" * 60)

    print("\nCompound Information")
    print("-" * 60)
    print(f"Name              : {data['name']}")
    print(f"Formula           : {data['formula']}")
    print(f"Molecular Weight  : {data['molecular_weight']}")
    print(f"IUPAC Name        : {data['iupac_name']}")
    print(f"SMILES            : {data['smiles']}")
    print(f"InChIKey          : {data['inchikey']}")
    print(f"PubChem CID       : {data['pubchem_cid']}")

    print("\nDEBUG")
    print("SMILES =", repr(data["smiles"]))

    image = generate_structure(data["smiles"], data["name"])

    properties = calculate_properties(data["smiles"])

    groups = detect_functional_groups(data["smiles"])

    lipinski = lipinski_analysis(data["smiles"])

    atoms = count_atoms(data["smiles"])

    rings = ring_information(data["smiles"])

    formula = molecular_formula(data["smiles"])

    print("\nCalculated Properties")
    print("-" * 60)

    for key, value in properties.items():
        print(f"{key:<20}: {value}")

    print("\nFunctional Groups")
    print("-" * 60)

    if groups:
        for group in groups:
            print("✓", group)
    else:
        print("None")

    print("\nAtom Count")
    print("-" * 60)

    for atom, count in atoms.items():
        print(f"{atom}: {count}")

    print("\nRing Information")
    print("-" * 60)

    print(rings)

    print("\nLipinski Rule")
    print("-" * 60)

    print(lipinski)

    print("\nMolecular Formula")
    print("-" * 60)

    print(formula)

    print("\nStructure Image")
    print("-" * 60)

    print(image)

    print("\n" + "=" * 60)


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
        display_report(data)
        return

    print("\nSearching PubChem...\n")

    data = fetch_compound(compound)
    print(data)

    if data is None:
        print("Compound not found.")
        return

    save_compound(data)

    display_report(data)

    print("\nSaved to local database.")