#  Cho danh sách $N$ từ gốc (roots) 
# và một câu văn bản gồm nhiều từ 
# cách nhau bởi dấu cách. 
# Nếu một từ trong câu bắt đầu bằng một từ gốc 
# trong từ điển, hãy thay thế toàn bộ từ đó 
# bằng từ gốc ngắn nhất tương ứng. 
# Nếu không khớp từ gốc nào, giữ nguyên từ đó.

line1 = input().split()
while not line1:
    line1 = input().split()
n = int(line1[0])

trie = {}
for _ in range(n):
    root = input().strip()
    curr = trie
    for ch in root:
        if ch not in curr:
            curr[ch] = {}
        curr = curr[ch]
    curr['#'] = True

sentence = input().split()
result = []

for word in sentence:
    curr = trie
    prefix = ""
    replaced = False
    for ch in word:
        if ch not in curr:
            break
        curr = curr[ch]
        prefix += ch
        if '#' in curr:
            result.append(prefix)
            replaced = True
            break
    if not replaced:
        result.append(word)

print(*result)