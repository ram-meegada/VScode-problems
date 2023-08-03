import nltk
import os, json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
from conversation import data

class text_filter:
    def __init__(self):
        self.data = data
        self.stop_words = set(stopwords.words('english'))

    def main_process(self, user_input):
        tokens = self.tokenized_list(user_input)
        print(tokens, 'tokens tokens =================-------------------')
        category_scores = {category:0 for category in self.categories}
        for token in tokens:
            for keys, values in self.categories.items():
                if token in values:
                    category_scores[keys] += 1
        print(category_scores)            
        arranged_category_scores = [(i,j) for i,j in sorted(category_scores.items(), key=lambda v:v[1], reverse=True)]
        return arranged_category_scores[0][0]

    def tokenized_list(self, text):
        tokens_list = word_tokenize(text.lower())
        tokens = []
        for token in tokens_list:
            if token not in self.stop_words:
                pos_tag_word = pos_tag([token])[0][1]
                lemmatizer = WordNetLemmatizer()
                if pos_tag_word.lower()[0] == 'v':
                    tokens.append(lemmatizer.lemmatize(token.lower(), pos='v'))
                elif pos_tag_word.lower()[0] == 'n':
                    tokens.append(lemmatizer.lemmatize(token.lower(), pos='n'))    
                else:
                    tokens.append(lemmatizer.lemmatize(token.lower(), pos='a'))
        return tokens

filter = text_filter()
user_input = input("Enter Here:-")
print(filter.main_process(user_input))




# def email_filtering_func(subject_of_mail, body_of_mail):    
#     email = EmailFilter()
#     subject = subject_of_mail
#     body = body_of_mail
#     final_category = email.main_process(subject, body)
#     return final_category