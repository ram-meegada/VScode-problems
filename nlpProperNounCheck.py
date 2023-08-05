import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def is_proper_noun(word):
    doc = nlp(word)
    for token in doc:
        if token.ent_type_ == "PERSON" or token.ent_type_ == "ORG" or token.ent_type_ == "GPE":
            return True
    return False

words_to_check = ["John", "vikhil", "modi", "ram", "Google"]

for word in words_to_check:
    if is_proper_noun(word):
        print(f"'{word}' is a proper noun.")
    else:
        print(f"'{word}' is not a proper noun.")