# ột lớp học có $N$ sinh viên (đánh số từ $1$ đến $N$) 
# và $M$ mối quan hệ bạn bè trực tiếp $(u, v)$.
# Nếu $A$ là bạn $B$, $B$ là bạn $C$ thì $A, B, C$ thuộc cùng một nhóm. 
#Hãy đếm xem lớp có bao nhiêu nhóm bạn bè độc lập và kiểm tra xem có mối quan hệ nào tạo thành vòng tròn khép kín (chu trình) hay không.

line1 = input().split()
while not line1: 
    line1 = input().split()
n,m = int(line1[0]), int(line1[1])

# Khởi tạo DSU (1-indexed)
parent = list(range(n+1))
rank = [0]*(n+1)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]
groups = n
cycles = 0

for _ in range(m):
    edge = input().split()
    while not edge:
        edge = input().split()
    u,v = int(edge[0]), int(edge[1])

    ru,rv = find(u), find(v)
    if ru==rv:
        cycles +=1
    else:
        if rank[ru] < rank[rv]:
            ru,rv= rv,ru
        parent[rv]=ru
        if rank[ru] == rank[rv]:
            rank[ru] += 1
        groups -= 1
print(groups)
print(cycles)
