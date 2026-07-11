from chemistry.summary import molecule_summary
from pprint import pprint

smiles = input("Enter SMILES: ")

summary = molecule_summary(smiles)

pprint(summary)