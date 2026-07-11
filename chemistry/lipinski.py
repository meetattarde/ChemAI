from chemistry.properties import calculate_properties


def lipinski_analysis(smiles):

    properties = calculate_properties(smiles)

    if properties is None:
        return None

    violations = 0

    if properties["Molecular Weight"] > 500:
        violations += 1

    if properties["LogP"] > 5:
        violations += 1

    if properties["H-Bond Donors"] > 5:
        violations += 1

    if properties["H-Bond Acceptors"] > 10:
        violations += 1

    return {
        "Violations": violations,
        "Drug Like": violations <= 1
    }