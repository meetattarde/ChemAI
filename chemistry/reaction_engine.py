from chemistry.functional_groups import detect_functional_groups 
from chemistry.product_generator import generate_product

def classify_compound(smiles):

    groups = detect_functional_groups(smiles)
    
    from chemistry.reaction_rules import REACTION_RULES
    
    def predict_by_rules(compound_name, smiles, reaction):
        compound_type = classify_compound(smiles)
        
        return REACTION_RULES.get(
            (compound_type, reaction.lower())
        )
        
        if rule is none:
            return None
        product = generate_product(
            compound_name,
            rule["product_class"]
        )
        
        rule["predicted_product"] = product
        
        return rule
    
    if "Alcohol" in groups:
        return "primary_alcohol"

    if "Aldehyde" in groups:
        return "aldehyde"

    if "Ketone" in groups:
        return "ketone"

    if "Carboxylic Acid" in groups:
        return "carboxylic_acid"

    if "Alkene" in groups:
        return "alkene"

    if "Alkyne" in groups:
        return "alkyne"

    if "Benzene Ring" in groups:
        return "benzene"

    return "unknown"