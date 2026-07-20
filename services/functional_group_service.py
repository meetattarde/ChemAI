FUNCTIONAL_GROUP_INFO = {

    "Alcohol": {
        "description": "Contains a hydroxyl (-OH) group.",
        "properties": [
            "Polar",
            "Forms hydrogen bonds",
            "Usually soluble in water"
        ],
        "common_reactions": [
            "Oxidation",
            "Dehydration",
            "Esterification"
        ]
    },

    "Carboxylic Acid": {
        "description": "Contains a carboxyl (-COOH) group.",
        "properties": [
            "Weak Acid",
            "Polar",
            "Hydrogen bonding"
        ],
        "common_reactions": [
            "Esterification",
            "Neutralization",
            "Reduction"
        ]
    },

    "Aldehyde": {
        "description": "Contains terminal carbonyl group.",
        "properties": [
            "Polar",
            "Reactive"
        ],
        "common_reactions": [
            "Oxidation",
            "Reduction",
            "Addition"
        ]
    },

    "Ketone": {
        "description": "Contains internal carbonyl group.",
        "properties": [
            "Polar"
        ],
        "common_reactions": [
            "Reduction",
            "Nucleophilic Addition"
        ]
    },

    "Alkene": {
        "description": "Contains C=C double bond.",
        "properties": [
            "Unsaturated"
        ],
        "common_reactions": [
            "Hydrogenation",
            "Hydration",
            "Halogenation"
        ]
    },

    "Alkyne": {
        "description": "Contains C≡C triple bond.",
        "properties": [
            "Unsaturated"
        ],
        "common_reactions": [
            "Hydrogenation",
            "Hydration"
        ]
    },

    "Aromatic Ring": {
        "description": "Contains aromatic benzene ring.",
        "properties": [
            "Highly stable",
            "Resonance stabilized"
        ],
        "common_reactions": [
            "Nitration",
            "Sulphonation",
            "Halogenation"
        ]
    },

    "Amine": {
        "description": "Contains amino (-NH₂) group.",
        "properties": [
            "Basic",
            "Polar"
        ],
        "common_reactions": [
            "Acylation",
            "Diazotization"
        ]
    }

}


def get_group_information(groups):

    info = []

    for group in groups:

        if group in FUNCTIONAL_GROUP_INFO:

            info.append(FUNCTIONAL_GROUP_INFO[group])

    return info