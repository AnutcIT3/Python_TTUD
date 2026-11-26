# Cho văn bản $T$ và mẫu $P$. 
# Khác với KMP tiêu chuẩn (tìm cả vị trí chồng lấn, ví dụ "abab" trong "ababab" xuất hiện 2 lần tại 0 và 2), 
# hãy đếm số lần $P$ xuất hiện trong $T$ sao cho 
# các lần xuất hiện không đè lên nhau 
# (ví dụ "abab" trong "ababab" chỉ tính 1 lần).
text = input().split()
pattern = input().strip()

n,m = len(text), len(pattern)
if m == 0 or n < m:
    print(0)
else:
    # 1. Tính LPS
    lps = [0]*m
    length = 0
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
        elif length > 0:
            length = lps[length-1]
        else:
            lps[i] = 0
            i += 1
        
    # 2. So khớp KMP không chồng lấn
    cout =0
    j = 0
    i = 0
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                cout += 1
                j = 0
        elif j > 0:
            j = lps[j-1]
        else:
            i += 1
    print(cout)