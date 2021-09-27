import urllib3

# First, create a string variable called ori that is equal to the Vibrio cholerae ori. Don't forget to enclose your string in quotes!

url = "https://bioinformaticsalgorithms.com/data/realdatasets/Replication/v_cholerae_oric.txt"
http = urllib3.PoolManager()

print("INFO: Fetching string ori from url: {url}...")
try:
    r = http.request('GET', url, timeout=6.0)
    if r.status == 200:
      ori_raw = r.data.decode('utf-8')
      print(ori_raw)
except urllib3.exceptions.NewConnectionError:
    print("ERROR: Failed to GET ori from url: {url}")
    exit(1)

# Then, print the length of ori
print("INFO: ori length: {}".format(len(ori_raw)))
