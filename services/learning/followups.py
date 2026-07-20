def get_followups(compound):

    name = compound.get("name", "this compound")

    return [

        f"What are the uses of {name}?",

        f"What are the important reactions of {name}?",

        f"Why is {name} chemically stable?",

        f"What are the NEET questions on {name}?",

        f"Explain the mechanism involving {name}.",

        f"What are compounds similar to {name}?"

    ]