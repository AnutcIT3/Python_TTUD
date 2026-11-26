s = input().strip()
n = len(s)

lps = [0]*n
length = 0
i = 1
while i < n:
    if s[i] == s[length]:
        length +=1
        lps[i]=length
        i+=1
    elif length > 0:
        length = lps[length - 1]
    else:
        lps[i] = 0
        i+=1
L = lps[n-1]
period = n - L

# kiểm tra nếu n chia hết cho (n - L)
if L > 0 and n % period == 0:
    print(period)
else: print(n)
