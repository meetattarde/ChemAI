def analyze_reactivity(result):

    groups = result.get("groups", [])

    analysis = []

    if "Alcohol" in groups:
        analysis.append("Can undergo oxidation to aldehydes or ketones depending on its structure.")

    if "Aldehyde" in groups:
        analysis.append("Can be oxidized to a carboxylic acid.")

    if "Ketone" in groups:
        analysis.append("Generally resistant to oxidation but can undergo reduction to secondary alcohols.")

    if "Carboxylic Acid" in groups:
        analysis.append("Acidic in nature and readily forms salts and esters.")

    if "Amine" in groups:
        analysis.append("Basic in nature due to the lone pair on nitrogen.")

    if "Alkene" in groups:
        analysis.append("Undergoes electrophilic addition reactions.")

    if "Alkyne" in groups:
        analysis.append("Can undergo addition and oxidation reactions.")

    if "Aromatic Ring" in groups:
        analysis.append("Prefers electrophilic substitution over addition reactions.")

    if "Haloalkane" in groups:
        analysis.append("Can undergo nucleophilic substitution reactions.")

    return analysis