# Có $N$ trạm phát sóng (từ $0$ đến $N-1$). 
# Có $M$ cặp trạm $(u, v)$ nằm gần nhau 
# nên không được phép dùng chung một tần số 
# (tránh nhiễu sóng). 
#Sử dụng thuật toán Welsh-Powell,
# hãy tính số lượng tần số tối thiểu cần cấp phát và in ra tần số 
# (đánh số từ $0$) của từng trạm.
line1 = input().split()
while not line1:
    line1  =input().split()
n,m = int(line1[0]), int(line1[1])
adj = [[] for _ in range(n)]
for _ in range(m):
    edge = input().split()
    while not edge:
        edge = input().split()
    u,v = int(edge[0],int(edge[1]))
    adj[u].append(v)
    adj[v].append(u)
# Sắp xếp các trạm theo số lượng trạm lân cận (bậc) giảm dần
nodes_sorted = sorted(range(n),key = lambda u: -len(adj[u]))

freq = [-1]*n

for u in nodes_sorted:
    used_freqs = {freq[v] for v in adj[u] if freq[v] != -1 }
    f = 0
    while f in used_freqs:
        f += 1
    freq[u] = f
total_freqs = max(freq) + 1 if n > 0 else 0
print(total_freqs)
print(*freq)
