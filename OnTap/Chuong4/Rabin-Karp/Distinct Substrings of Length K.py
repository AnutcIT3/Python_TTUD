# Cho xâu $S$ độ dài $N$ và số nguyên dương $K$. 
# Hãy sử dụng Rabin-Karp Rolling Hash 
# để đếm xem trong $S$ có bao nhiêu xâu con liên tiếp 
# độ dài $K$ đôi một khác nhau.
k = int(input().strip())
s = int(input().strip())
n = len(s)

if k > n or k <= 0:
    print(0)
else:
    base = 256
    mod = 10*9+7
    h = pow(base,k-1,mod)

    distinct_hashes = set()
    curr_hash = 0

    for i in range(k):
        curr_hash = (curr_hash*base + ord(s[i])) % mod
    distinct_hashes.add(curr_hash)

    for i in range(n - k):
        curr_hash = (curr_hash - ord(s[i])*h) % mod
        curr_hash = (curr_hash*base + ord(s[i])) % mod
        curr_hash = (curr_hash + mod) % mod
    print(len(distinct_hashes))