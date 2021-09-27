import urllib3

url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/v_cholerae_oric.txt"

def GetOri(url):
    http = urllib3.PoolManager()
    print("INFO: Fetching string ori from url: {url}...")
    try:
        r = http.request('GET', url, timeout=6.0)
        if r.status == 200:
          ori_raw = r.data.decode('utf-8')
          return ori_raw
    except urllib3.exceptions.NewConnectionError:
        print("ERROR: Failed to GET ori from url: {url}")
        exit(1)

def PatternCount(Text, Pattern):
    print("INFO: Searching for k-mer: {}".format(Pattern))
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count

# First, create a string variable called ori that is equal to the Vibrio cholerae ori. Don't forget to enclose your string in quotes!
ori_raw = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

# Then, print the length of ori
#print("INFO: ori length: {}".format(len(ori_raw)))
print(len(ori_raw))

# Then print  the number of times that the string Pattern = "TGATCA" occurs in the string Text corresponding to the Vibrio cholerae ori
Pattern = "TGATCA"

result = PatternCount(ori_raw, Pattern)
#print("INFO: ori contains: {} instances of {} k-mer".format(result, Pattern))
print(result)
