# Một dự án phần mềm gồm $N$ module (từ $0$ đến $N-1$) 
# và $M$ ràng buộc phụ thuộc $(u, v)$ 
# có nghĩa là module $u$ phải được biên dịch xong 
# trước khi biên dịch module $v$. Hãy in ra một thứ tự biên dịch hợp lệ. 
# Nếu tồn tại phụ thuộc vòng (lỗi biên dịch), in ra IMPOSSIBLE
from collections import deque
line1 = input().split()
while not line1:
    line1 = input().split()
n,m = int(line1[0]), int(line1[1])

adj = [[] for _ in range(n)]
in_degree = [0]*n

for _ in range(m):
    edge = input().split()
    while not edge:
        edge = input().split()
    u,v = int(edge[0]), int(edge[1])
    adj[u].append(v)
    in_degree[v] +=1
q = deque([i for i in range(n) if in_degree[i] == 0])
order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            q.append(v)
if len(order) == n:
    print(*order)
else:
    print("IMPOSSIBLE")
