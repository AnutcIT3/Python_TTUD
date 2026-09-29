def rabin_karp(van_ban, mau, base=256, mod=10**9+7):
    n, m = len(van_ban), len(mau)
    if m > n: return []
    h = pow(base, m - 1, mod)
    hash_mau = hash_vb = 0
    for i in range(m):                 # tinh hash cua so dau tien
        hash_mau = (hash_mau * base + ord(mau[i])) % mod
        hash_vb = (hash_vb * base + ord(van_ban[i])) % mod
    # ket_qua = []
    a=0
    for i in range(n - m + 1):
        if hash_mau == hash_vb:
            # ket_qua.append(i)      
            a+=1
        if i < n - m:
            hash_vb = (hash_vb - ord(van_ban[i]) * h) % mod
            hash_vb = (hash_vb * base + ord(van_ban[i+m])) % mod
    return a
    # return ket_qua

print(rabin_karp("abcxabcdabcdabcy", "abcdabcy"))   # [8]
