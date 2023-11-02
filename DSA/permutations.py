def permute(s):
  out = []
  if len(s) == 1:
    return s
  else:
    for i,let in enumerate(s):
      rem_permutations = permute(s[:i] + s[i+1:])
      for perm in rem_permutations:
        out += [let + perm]
  return out


nums = 'abc'
result = permute(nums)
print(result)