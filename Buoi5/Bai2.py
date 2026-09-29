#Dùng Rabin-Karp kiểm tra xem một đoạn văn có chứa nguyên văn một câu từ văn bản gốc hay không (phát hiện đạo văn đơn giản).
def rabin_karp(van_ban, mau, base=256, mod=10**9+7):
    n, m = len(van_ban), len(mau)
    if m > n: return []
    h = pow(base, m - 1, mod)
    hash_mau = hash_vb = 0
    for i in range(m):                 # tinh hash cua so dau tien
        hash_mau = (hash_mau * base + ord(mau[i])) % mod
        hash_vb = (hash_vb * base + ord(van_ban[i])) % mod
    ket_qua = []
    for i in range(n - m + 1):
        if hash_mau == hash_vb:
            ket_qua.append(i)           # xac nhan lai de tranh dung do
        if i < n - m:
            hash_vb = (hash_vb - ord(van_ban[i]) * h) % mod
            hash_vb = (hash_vb * base + ord(van_ban[i+m])) % mod
    return ket_qua

van_ban = input("nhap van ban: ")
print(rabin_karp(van_ban, "ban la nhat"))   # [8]