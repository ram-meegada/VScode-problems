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
    for i in range(0, len(s1)):
        if i == 2:
            break
        third = s1[i+2]
        first = s1[i]
        print(third, first)
        print(third + s1[1] + first + s1[3], '------', s1[0] + third + s1[2] + first)
        if (third + s1[1] + first + s1[3] == s2) or (s1[0] + third + s1[2] + first == s2):
            return True
        if s1 == s2:
            return True
        else:
            third = s1[i+2]
            first = s1[i]
            if i == 0:
                s1 = third + s1[1] + first + s1[3]
            elif i == 1:
                s1 = s1[0] + third + s1[2] + first
            if s1 == s2: return True
    return False

s1 = "bnxw"
s2 = "bwxn"
result = solution(s1, s2)
print(result)