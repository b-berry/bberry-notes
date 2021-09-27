# Input:  A DNA string Pattern
# Output: The complementary string of Pattern (with every nucleotide replaced by its complement).
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

input_s = "AAAACCCGGT"
result = Complement(input_s)
print(result)
