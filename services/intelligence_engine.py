def generate_reasoning(result):

    text = []

    groups = result.get("groups", [])
    props = result.get("properties", {})

    if "Alcohol" in groups:
        text.append(
            "This molecule contains a hydroxyl (-OH) functional group, classifying it as an alcohol."
        )

        text.append(
            "Alcohols are polar compounds capable of forming hydrogen bonds."
        )

        text.append(
            "Primary alcohols generally undergo oxidation to aldehydes and eventually carboxylic acids."
        )

    if "Carboxylic Acid" in groups:
        text.append(
            "The carboxyl group makes this molecule acidic and capable of donating protons."
        )

    if "Aldehyde" in groups:
        text.append(
            "Aldehydes are highly reactive and are easily oxidized into carboxylic acids."
        )

    if "Ketone" in groups:
        text.append(
            "Ketones contain a carbonyl group and are resistant to mild oxidation."
        )

    if "Amine" in groups:
        text.append(
            "Amines behave as weak bases because of the lone pair present on nitrogen."
        )

    if props.get("LogP", 0) > 2:
        text.append(
            "The relatively high LogP value indicates that the compound is more soluble in organic solvents than in water."
        )

    if props.get("H-Bond Donors", 0) > 0:
        text.append(
            "Hydrogen bond donors increase intermolecular attraction and influence boiling point."
        )

    if props.get("Ring Count", 0) > 0:
        text.append(
            "The presence of ring structures increases molecular rigidity and may influence chemical stability."
        )

    return " ".join(text)