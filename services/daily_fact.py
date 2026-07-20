import random

FACTS = [

"Benzene was discovered by Michael Faraday in 1825.",

"Diamond and graphite are both pure carbon.",

"Water expands when it freezes.",

"The smell of almonds is associated with benzaldehyde.",

"Graphene is one atom thick.",

"Gold can be hammered into sheets only a few atoms thick.",

"DNA contains billions of atoms in a single molecule.",

"The human body contains about 60 different chemical elements."

]

def get_daily_fact():
    return random.choice(FACTS)