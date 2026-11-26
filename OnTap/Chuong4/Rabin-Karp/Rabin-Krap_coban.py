text = input().strip()
pattern = input().strip()
n,m= len(text), len(pattern)
base = 256
mod = 10**9 + 7
h = pow(base, m-1, mod)
hash_p = 0
hash_t = 0
for i in range(m):
    hash_p = (hash_p*base + ord(pattern[i])) % mod
    hash_t = (hash_p*base + ord(text[i])) % mod
res = []

for i in range(n - m + 1):
        if hash_p == hash_t:
            # Xác minh lại để tránh đụng độ hash (Hash Collision)
            if text[i : i + m] == pattern:
                res.append(i)

        # Cập nhật Rolling Hash cho cửa sổ tiếp theo
        if i < n - m:
            hash_t = (hash_t - ord(text[i]) * h) % mod
            hash_t = (hash_t * base + ord(text[i + m])) % mod
            hash_t = (hash_t + mod) % mod

print(len(res))
if res:
    print(*res)

