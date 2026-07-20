def compare_compounds(compound1, compound2):

    if compound1 is None or compound2 is None:
        return None

    comparison = {

        "Formula": (
            compound1.get("formula"),
            compound2.get("formula")
        ),

        "Molecular Weight": (
            compound1.get("molecular_weight"),
            compound2.get("molecular_weight")
        ),

        "IUPAC Name": (
            compound1.get("iupac_name"),
            compound2.get("iupac_name")
        ),

        "SMILES": (
            compound1.get("smiles"),
            compound2.get("smiles")
        ),

        "PubChem CID": (
            compound1.get("pubchem_cid"),
            compound2.get("pubchem_cid")
        )

    }

    return comparison