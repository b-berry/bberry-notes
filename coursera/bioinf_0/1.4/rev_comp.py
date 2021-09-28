def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

def Complement(Pattern):
    c_map = { 
        "A": "T",
        "C": "G",
        "G": "C",
        "T": "A"
    }
    com_p = ""
    for n in Pattern:
      com_p = com_p + c_map[n]
    return com_p

def Reverse(Pattern):
    rev_p = ""
    for n in Pattern:
      rev_p = n + rev_p
    return rev_p

input_s = "AAAACCCGGT"
result = ReverseComplement(input_s)
print(result)
