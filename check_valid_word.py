import nltk
from nltk.corpus import wordnet

# Download WordNet data
# nltk.download("wordnet")

def is_valid_word(word):
    return bool(wordnet.synsets(word))

words_to_check = ["aple", "xylophone", "python", "iii", "please"]
for word in words_to_check:
    if is_valid_word(word):
        print(f"'{word}' is a valid word.")
    else:
        print(f"'{word}' is not a valid word.")


       