REACTION_OPTIONS = {

    "benzene": [
        "nitration",
        "chlorination",
        "bromination",
        "sulphonation",
        "friedel-crafts alkylation",
        "friedel-crafts acylation"
    ],

    "ethanol": [
        "oxidation",
        "dehydration",
        "esterification",
        "combustion",
        "sodium",
        "pcl5",
        "socl2"
    ],

    "ethanal": [
        "oxidation",
        "reduction",
        "tollens test",
        "fehling test"
    ],

    "ethene": [
        "hydration",
        "hydrogenation",
        "halogenation",
        "polymerisation",
        "oxidation"
    ]
}


def available_reactions(compound):

    compound = compound.lower().strip()

    return REACTION_OPTIONS.get(compound, [])