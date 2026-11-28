# Có $N$ thành phố (đánh số $1 \dots N$) và $M$ tuyến đường 
# dự kiến xây dựng, mỗi tuyến nối hai thành phố $u, v$ với chi phí $w$.
#  Hãy chọn một tập hợp các tuyến đường sao cho 
# tất cả các thành phố đều đi lại được với nhau và tổng chi phí xây dựng 
# là nhỏ nhất. Nếu không thể kết nối hết tất cả thành phố, in ra -1
line1 = input().split()
while not line1:
    line1 = input().split()
n,m = int(line1[0]), int(line1[1])
edges = []
for _ in range(m):
    e = input().split()
    while not e:
        e = input().split()
    u,v,w = int(e[0]),int(e[1]),int(e[2])
    edges.append((w,u,v))

# Sắp xếp cạnh theo trọng số tăng dần
edges.sort()

parent = list(range(n+1))
rank = [0]*(n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

total_cost = 0
edges_used = 0

for w,u,v in edges:
    ru, rv = find(u),find(v)
    if ru != rv:
        if rank[ru] < rank[rv]:
            ru, rv = rv,ru
        parent[ru] = ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
        total_cost += w
        edges_used += 1
        if edges_used == n - 1:
            break

if edges_used == n - 1:
    print(total_cost)
else:
    print(-1)
