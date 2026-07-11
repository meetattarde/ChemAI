from chemistry.properties import calculate_properties
from chemistry.functional_groups import detect_functional_groups
from chemistry.formula import molecular_formula
from chemistry.rings import ring_information
from chemistry.atom_counter import count_atoms
from chemistry.lipinski import lipinski_analysis


def molecule_summary(smiles):

    return {
        "Formula": molecular_formula(smiles),
        "Properties": calculate_properties(smiles),
        "Functional Groups": detect_functional_groups(smiles),
        "Rings": ring_information(smiles),
        "Atoms": count_atoms(smiles),
        "Lipinski": lipinski_analysis(smiles)
    }