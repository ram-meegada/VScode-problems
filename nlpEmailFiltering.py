import asyncio, json
import nltk
from django.core.mail import send_mail
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# from chatbotContent import data

class EmailFilter:
    def __init__(self):
        self.categories = {
            'ambiguity' : [],
            'promotions': ["offer", "discount", "sale", "special", "promo", "deal", "coupon", "bargain", "promotion", "save"],
            'social': ["friend", "party", "invitation", "celebration", "gathering", "event", "get-together", "hangout", "reunion", "meetup", "anniversary"],
            'spam' : ["free", "limited time", "urgent", "exclusive offer", "congratulation", "discount", "lottery", "winner", "inheritance", "cash prize", "won", "guarantee", "act now", "click here", "double your", "make money", "investment", "risk-free", "viagra", "prescription", "online pharmacy"],
            'non_spam' : ["meeting", "reminder", "collaboration", "project", "update", "account", "invoice", "payment", "confirmation", "receipt", "newsletter", "subscription", "invitation", "request", "feedback", "thank", "job opportunity", "personal", "family", "friend"]
        }
        self.stop_words = set(stopwords.words('english'))

    def main_process(self, subject, body):
        tokens = self.tokenized_list(subject+' '+body)
        print(tokens)
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
                tokens.append(self.lemmatize_word(token))
        return tokens
    def lemmatize_word(self, token):
        pos_tag_word = pos_tag([token])[0][1]
        lemmatizer = WordNetLemmatizer()
        if pos_tag_word.lower()[0] == 'v':
            return lemmatizer.lemmatize(token.lower(), pos='v')
        elif pos_tag_word.lower()[0] == 'n':
            return lemmatizer.lemmatize(token.lower(), pos='n')  
        else:
            return lemmatizer.lemmatize(token.lower(), pos='a')

def email_filtering_func(subject_of_mail, body_of_mail):    
    email = EmailFilter()
    subject = subject_of_mail
    body = body_of_mail
    final_category = email.main_process(subject, body)
    return final_category
# email_filtering_func("looking", 'restaurants')



# Test with sentences
sentences = [
    "Hi, my name is John Smith.",
    "Call me Alex.",
    "My full name is Elizabeth Thompson.",
    "You can refer to me as TechEnthusiast.",
    "I'm the artist formerly known as Ava.",
    "Hello, I'm Emily.",
]
def sentence_classification():
    pos_tag_word = pos_tag([token])[0][1]
    lemmatizer = WordNetLemmatizer()
    if pos_tag_word.lower()[0] == 'v':
        return lemmatizer.lemmatize(token, pos='v')
    elif pos_tag_word.lower()[0] == 'n':
        return lemmatizer.lemmatize(token, pos='n')  
    else:
        return lemmatizer.lemmatize(token, pos='a')