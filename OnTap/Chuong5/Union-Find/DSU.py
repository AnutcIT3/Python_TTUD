# Một trung tâm dữ liệu có $N$ máy chủ ($1 \dots N$). 
# Ban đầu mỗi máy chủ đứng riêng lẻ. Có $Q$ thao tác thuộc 2 loại:
# 1 u v: Kết nối máy chủ $u$ và máy chủ $v$ bằng dây mạng.
# 2 u: Hỏi xem cụm mạng hiện tại đang chứa máy chủ $u$ 
# có tổng cộng bao nhiêu máy chủ?
line1 = input().split()
while not line1:
    line1 = input().split()
n, q = int(line1[0]), int(line1[1])
parent = list(range(n+1))
sz = [1]*(n+1)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

for _ in range(q):
    qr = input().split()
    while not qr:
        qr = input().split()
    t = int(qr[0])
    if t == 1:
        u,v = int(qr[1]),int(qr[2])
        ru,rv = find(u),find(v)
        if ru != rv:
            if sz[ru] < sz[rv]:
                ru,rv = rv,ru
            parent[ru] = ru
            sz[ru] += sz[rv]
    else:
        u = int(qr[1])
        print(sz[find(u)])


    