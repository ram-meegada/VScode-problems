# Example 1:

# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:

# Input: s = "abcd", k = 2
# Output: "bacd"

def answer(s, k):
	start = 2*k
	for i in range(start, len(s), 2*k):
		print(i, s[i])
		if len(s[i:]) > k and len(s[i:]) < 2*k:
			s = s[:i+1:-1] + s[i+1:]
	return s

s = "abcdefg"
k = 2
result = answer(s, k)
print(result)