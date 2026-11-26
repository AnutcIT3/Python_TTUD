# Cho xâu văn bản $T$ và xâu mẫu $P$. 
#Tìm tất cả các vị trí chỉ số (0-indexed) bắt đầu của $P$ xuất hiện trong $T$.
text = input().strip()
pattern = input().strip()
n,m = len(text), len(pattern)
# Xây dựng bảng LPS
lps = [0]*m
length = 0
i=1
while i < m:
    if pattern[i] == pattern[length]:
        length +=1
        lps[i] = length
        i+=1
    elif length > 0:
        length = lps[length - 1]
    else:
        lps[i] = 0
        i += 1
# so khớp KMP
res = []
i = 0
j = 0
while i < n:
    if text[i] == pattern[j]:
        i += 1
        j += 1
        if j == m:
            res.append(i-j)
            j = lps[j-1]
    elif j>0:
        j = lps[j-1]
    else: 
        i+=1
print(len(res))
if res:
    print(*res)
