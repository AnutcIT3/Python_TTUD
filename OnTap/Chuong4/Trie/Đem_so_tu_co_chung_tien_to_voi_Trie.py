# Cho danh sách $N$ từ. Sau đó trả lời $Q$ truy vấn, 
# mỗi truy vấn cho một tiền tố, đếm số từ trong từ điển bắt đầu bằng tiền tố đó.
line1 = input().split()
while not line1:
    line1 = input().split()
n,q = int(line1[0]), int(line1[1])

trie = {}
for _ in range(n):
    w = input().strip()
    curr = trie
    for ch in w:
        if ch not in curr:
            curr[ch] = {'_count':0}
        curr = curr[ch]
        curr['_count']+=1
for _ in range(q):
    pref = input().strip()
    curr = trie
    found = True
    for ch in pref:
        if ch not in curr:
            found  = False
            break
        curr = curr[ch]
    if found:
        print(curr['_count'])
    else:
        print(0)