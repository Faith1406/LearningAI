import json
from difflib import get_close_matches

def load_knowledge(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_knowledge(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=3)

def matches_knowledge(user_question, questions):
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer(question, knowledge):
    for q in knowledge["questions"]:
        if q["question"] == question:
            return q["answer"]

def chatbot(user_input, correction_input=None):
    knowledge = load_knowledge("TheKnowledge.json")
    best_match = matches_knowledge(user_input, [q["question"] for q in knowledge["questions"]])
    if best_match:
        return get_answer(best_match, knowledge), None
    if correction_input and correction_input.strip():
        knowledge["questions"].append({"question": user_input, "answer": correction_input})
        save_knowledge("TheKnowledge.json", knowledge)
        return f"Thanks for teaching me! I've learned: {correction_input}", False
    return None, True    
