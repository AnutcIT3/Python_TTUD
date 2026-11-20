a = input().strip()
b = input().strip()

if len() != len(b):
    print("NO")
else:
    text = a+a
    pattern = b
    n,m = len(text), len(pattern)

    lps = [0]*m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1 
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length -1]
        else:
            lps[i] = 0
            i+=1
    # tim pattern trong text
    i = j = 0
    found = False
    while i < n:
        if text[i] == pattern[j]:
            i+=1
            j+=1
            if j == m:
                found = True
                break
        elif j > 0 :
            j = lps[j-1]
        else: i += 1
    print("YES" if found else "NO")
