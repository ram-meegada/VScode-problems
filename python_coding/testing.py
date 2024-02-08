from collections import Counter
# Example 1:
# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:
# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

<<<<<<< Updated upstream
# import logging

# a = 5
# b = 0
# try:
#     c = a/b
#     logging.info(f"the result is {c}")
# except Exception as error:
#     logging.exception(f"exception occurred. the error is {error}")    


# try:
#   c = a / b
# except Exception as e:
#   logging.error("Exception occurred", exc_info=True)
    
# words = ["apple", "banana", "cherry"]
# lengths_good = dict((w, len(w)) for w in words)    
# lengths_bad = {w: len(w) for w in words}
# print(lengths_good["banana"], type(lengths_good))
# print(lengths_bad, type(lengths_bad))
import pandas as pd

content = pd.read_excel("testing.xlsx", engine='openpyxl')
df_no_duplicates = content.drop_duplicates()
duplicate_rows = content[content.duplicated()]
# print("content", content, len(content), '--------------')
print("df_no_duplicates", df_no_duplicates, len(df_no_duplicates), '--------------')
print(duplicate_rows, "duplicate_rows-------", len(duplicate_rows))
=======
secret = "1123"
guess = "0111"
# bulls = 0
# cows_count = 0
# secret_cows = {}
# guess_cows = {}
# for i in range(len(secret)):
#     if secret[i] == guess[i]:
#         bulls += 1
#     else:
#         secret_cows[secret[i]] = secret_cows.get(secret[i], 0) + 1
#         guess_cows[guess[i]] = guess_cows.get(guess[i], 0) + 1

# for i,j in secret_cows.items():
#     if guess_cows.get(i):
#         if j >= guess_cows[i]:
#             cows_count += guess_cows[i]
#         else:
#             cows_count += j 
# print(f"{bulls}A{cows_count}B")              

# sh = defaultdict(int)


s, g = Counter(secret), Counter(guess)
# a = sum(i == j for i, j in zip(secret, guess))
# print('%sA%sB' % (a, sum((s & g).values()) - a)) 
b = {1:9, 2:3}
c = {4:5, 1:2}
print(Counter(c) & Counter(b))
>>>>>>> Stashed changes
