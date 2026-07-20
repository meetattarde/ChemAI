from rdkit import Chem

from chemistry.reaction_smarts import REACTIONS


def execute(smiles, reaction_name):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    reaction = REACTIONS.get(reaction_name)

    if reaction is None:
        return None

    products = reaction.RunReactants((mol,))

    if not products:
        return None

    product = products[0][0]

    Chem.SanitizeMol(product)

    return Chem.MolToSmiles(product)