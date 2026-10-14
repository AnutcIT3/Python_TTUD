import sys

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])

# Danh sách kề
ke = [[] for _ in range(n + 1)]
pos = 2
for _ in range(m):
    u, v = int(data[pos]), int(data[pos + 1])
    pos += 2
    ke[u].append(v)
    ke[v].append(u)

da_tham = [False] * (n + 1)
so_khu_vuc = 0
lon_nhat = 0

for s in range(1, n + 1):
    if not da_tham[s]:
        so_khu_vuc += 1
        da_tham[s] = True
        stack = [s]
        kich_thuoc = 0
        while stack:                      # DFS dùng stack
            u = stack.pop()
            kich_thuoc += 1
            for v in ke[u]:
                if not da_tham[v]:
                    da_tham[v] = True     # đánh dấu khi đẩy vào stack
                    stack.append(v)
        if kich_thuoc > lon_nhat:
            lon_nhat = kich_thuoc

print(so_khu_vuc)
print(lon_nhat)