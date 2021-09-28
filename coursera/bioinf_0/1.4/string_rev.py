# Input:  A string Pattern
# Output: The reverse of Pattern
def Reverse(Pattern):
    rev_p = ""
    for n in Pattern:
      rev_p = n + rev_p
    return rev_p

input_s = "AAAACCCGGT"
result = Reverse(input_s)
print(result)
