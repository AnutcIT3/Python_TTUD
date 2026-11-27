# Cho hai chuỗi $A$ và $B$ có cùng độ dài $N$. 
# Chuỗi $B$ được gọi là chuỗi xoay vòng của $A$ 
# nếu có thể cắt một đoạn ở đầu $A$ chuyển xuống cuối $A$ để thu được $B$ 
# (ví dụ: "abcde" xoay thành "cdeab"). 
# Hãy dùng Rabin-Karp kiểm tra xem $B$ 
# có phải là chuỗi xoay vòng của $A$ không (YES hoặc NO).
a = input().strip()
b = input().strip()

if len(a) != len(b):
    print("NO")
elif a == b:
    print("YES")
else:
    text = a + a
    n,m = len(text),len(b)
    base = 256
    mod = 10**9 + 7
    h = pow(base,m-1,mod)

    hash_b = 0
    hash_t = 0
    for i in range(m):
        hash_b = (hash_b*base + ord(b[i])) % mod
        hash_t = (hash_t*base + ord(text[i])) % mod
    found = False
    for i in range(n-m+1):
        if hash_b == hash_t:
            if text[i:i+m]==b:
                found = True
        if i < n - m:
            hash_t = (hash_t - ord(text[m])*h) % mod
            hash_t = (hash_t * base + ord(text[i+m])) % mod
            hash_t = (hash_t + mod) % mod
    print("YES" if found else "NO")


