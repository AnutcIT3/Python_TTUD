# Cho danh sách $N$ từ khóa cấm (từ nhạy cảm). 
# Sau đó cho $Q$ truy vấn, 
# mỗi truy vấn là một từ kiểm tra $S$. 
# Hãy kiểm tra xem từ $S$ có bắt đầu bằng bất kỳ từ 
# khóa cấm nào trong danh sách hay không 
# (in YES nếu vi phạm, NO nếu hợp lệ).
line1 = input().split()
while not line1:
    line1 = input().split()
n, q = int(line1[0]), int(line1[1])

trie = {}
for _ in range(n):
    bad_word = input().strip()
    curr = trie
    for ch in bad_word:
        if ch not in curr:
            curr[ch] = {}
        curr = curr[ch]
    curr['#'] = True

for _ in range(q):
    word = input().strip()
    curr = trie
    violated = False
    for ch in word:
        if '#' in curr:
            violated = True
            break
        if ch not in curr:
            break
        curr = curr[ch]
    if '#' in curr:
        violated = True
        
    print("YES" if violated else "NO")