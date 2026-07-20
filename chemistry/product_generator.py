REACTION_RULES = {

    ("primary_alcohol", "oxidation"): {
        "product_class": "aldehyde",
        "reaction_type": "Oxidation"
    },

    ("aldehyde", "oxidation"): {
        "product_class": "carboxylic_acid",
        "reaction_type": "Oxidation"
    },

    ("alkene", "hydration"): {
        "product_class": "alcohol",
        "reaction_type": "Addition"
    },

    ("benzene", "nitration"): {
        "product_class": "nitrobenzene",
        "reaction_type": "Electrophilic Aromatic Substitution"
    }

}