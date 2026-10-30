line1 = input().split()
while not line1:
    line1 = input().split()
n, q = int(line1[0]), int(line1[1])

line2 = input().split()
while not line2 or len(line2) < n:
    line2.extend(input().split())
a = [int(x) for x in line2[:n]]

tree = [0] * (4 * n)

def build(node, l, r):
    if l == r:
        tree[node] = a[l]
        return
    mid = (l + r) // 2
    build(2 * node, l, mid)
    build(2 * node + 1, mid + 1, r)
    tree[node] = tree[2 * node] + tree[2 * node + 1]

def update(node, l, r, idx, val):
    if l == r:
        tree[node] = val
        return
    mid = (l + r) // 2
    if idx <= mid:
        update(2 * node, l, mid, idx, val)
    else:
        update(2 * node + 1, mid + 1, r, idx, val)
    tree[node] = tree[2 * node] + tree[2 * node + 1]

def query(node, l, r, ql, qr):
    if qr < l or r < ql:
        return 0
    if ql <= l and r <= qr:
        return tree[node]
    mid = (l + r) // 2
    return query(2 * node, l, mid, ql, qr) + query(2 * node + 1, mid + 1, r, ql, qr)

build(1, 0, n - 1)

for _ in range(q):
    qr = input().split()
    while not qr:
        qr = input().split()
    type_q = int(qr[0])
    if type_q == 1:
        idx, val = int(qr[1]), int(qr[2])
        update(1, 0, n - 1, idx, val)
    else:
        ql, qr_idx = int(qr[1]), int(qr[2])
        print(query(1, 0, n - 1, ql, qr_idx))