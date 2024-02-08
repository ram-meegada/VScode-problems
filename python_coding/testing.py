# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.
# Example 1:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

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