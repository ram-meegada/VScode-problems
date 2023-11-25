# <!-- 2839. Check if Strings Can be Made Equal With Operations I
# Easy
# 160
# 20
# Companies
# You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.
# You can apply the following operation on any of the two strings any number of times:
# Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.
# Return true if you can make the strings s1 and s2 equal, and false otherwise.
# Example 1:
# Input: s1 = "abcd", s2 = "cdab"
# Output: true
# Explanation: We can do the following operations on s1:
# - Choose the indices i = 0, j = 2. The resulting string is s1 = "cbad".
# - Choose the indices i = 1, j = 3. The resulting string is s1 = "cdab" = s2.

# Example 2:
# Input: s1 = "abcd", s2 = "dacb"
# Output: false
# Explanation: It is not possible to make the two strings equal. -->

def solution(s1, s2):
    a = s1[2]+s1[1]+s1[0]+s1[3]
    if a == s2:
        return True
    b = s1[0]+s1[3]+s1[2]+s1[1]
    if b == s2:
        return True
    c = a[0]+a[3]+a[2]+a[1]
    if c == s2:
        return True
    return False

s1 = "abcd"
s2 = "dacb"
result = solution(s1, s2)
print(result)