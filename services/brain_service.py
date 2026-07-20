from services.knowledge_engine import build_knowledge


def analyze(compound):
    
    knowledge = build_knowledge(compound["groups"])

    return "".join(knowledge)
        
        