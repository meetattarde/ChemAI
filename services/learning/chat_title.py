def generate_chat_title(question):

    words = question.split()

    if len(words) <= 6:
        return question.title()

    return " ".join(words[:6]).title() + "..."