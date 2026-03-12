def search_knowledge(question):

    knowledge = {
        "AI": "Artificial Intelligence is a field of computer science.",
        "Machine Learning": "Machine learning is a subset of AI.",
        "LLM": "Large Language Models can generate human-like text."
    }

    for key in knowledge:
        if key.lower() in question.lower():
            return knowledge[key]

    return "No relevant knowledge found."
