from spellchecker import SpellChecker
from textblob import TextBlob


spell = SpellChecker()

def correct_spelling(text):
    corrected_words = spell.correction(text)
    return corrected_words

input_text = 'restarent'

corrected_text = correct_spelling(input_text)

print(corrected_text)