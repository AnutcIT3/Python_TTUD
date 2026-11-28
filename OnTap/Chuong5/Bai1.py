# Một thành phố có $N$ giao lộ và $M$ con đường hai chiều (đảm bảo liên thông). 
# Chính quyền muốn biến tất cả các con đường này thành đường một chiều sao cho từ bất kỳ giao lộ nào 
# cũng đi đến được mọi giao lộ khác. 
# Nếu không thể thực hiện, hãy in ra 0; nếu có thể, hãy in ra một cách định hướng hợp lệ.

import sys
sys.setrecursionlimit(20000)

line1 = input().split()
while not line1:
    line1 = input().split()
n, m = int(line1[0]), int(line1[1])

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    edge = input().split()
    while not edge:
        edge = input().split()
    u, v = int(edge[0]), int(edge[1])
    adj[u].append(v)
    adj[v].append(u)

num = [0] * (n + 1)
low = [0] * (n + 1)
timer = 0
has_bridge = False
directed_edges = []

def dfs(u, parent):
    global timer, has_bridge
    timer += 1
    num[u] = low[u] = timer
    
    for v in adj[u]:
        if v == parent:
            continue
        if num[v] > 0:
            low[u] = min(low[u], num[v])
            # Chỉ lấy cạnh ngược hướng từ đỉnh thăm sau về đỉnh thăm trước
            if num[v] < num[u]:
                directed_edges.append((u, v))
        else:
            directed_edges.append((u, v))
            dfs(v, u)
            low[u] = min(low[u], low[v])
            if low[v] > num[u]:
                has_bridge = True

dfs(1, 0)

if has_bridge or len(directed_edges) < m:
    print(0)
else:
    for u, v in directed_edges:
        print(u, v)