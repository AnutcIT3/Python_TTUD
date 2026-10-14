import sys

data = sys.stdin.read().split()
n, m = int(data[0]), int(data[1])
t = [0] + [int(x) for x in data[2:2 + n]]     # t[1..n]

ke = [[] for _ in range(n + 1)]
pos = 2 + n
for _ in range(m):
    u, v = int(data[pos]), int(data[pos + 1])
    pos += 2
    ke[u].append(v)
    ke[v].append(u)

da_tham = [False] * (n + 1)
kq = []

for s in range(1, n + 1):
    if not da_tham[s]:
        da_tham[s] = True
        stack = [s]
        tot_nhat = s                      # người tin cậy nhất trong thành phần
        while stack:                      # DFS bằng stack
            u = stack.pop()
            if t[u] > t[tot_nhat]:
                tot_nhat = u
            for v in ke[u]:
                if not da_tham[v]:
                    da_tham[v] = True
                    stack.append(v)
        kq.append(tot_nhat)

kq.sort()
print(len(kq))
print(*kq)