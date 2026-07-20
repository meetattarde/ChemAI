from api.pubchem_api import fetch_compound

from chemistry.properties import calculate_properties
from chemistry.functional_groups import detect_functional_groups
from chemistry.lipinski import lipinski_analysis
from chemistry.atom_counter import count_atoms
from chemistry.rings import ring_information
from chemistry.formula import molecular_formula
from chemistry.structure import generate_structure
from services.reasoning_service import get_reasoning


def get_compound_data(compound):

    result = fetch_compound(compound)

    if not result:
        return None

    result["properties"] = calculate_properties(result["smiles"])
    result["groups"] = detect_functional_groups(result["smiles"])
    result["lipinski"] = lipinski_analysis(result["smiles"])
    result["atoms"] = count_atoms(result["smiles"])
    result["rings"] = ring_information(result["smiles"])
    result["formula2"] = molecular_formula(result["smiles"])
    result["image"] = generate_structure(
        result["smiles"],
        result["name"]
    )
    
    result["reasoning"] = get_reasoning(result)
    return result