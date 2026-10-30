# Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn, mỗi truy vấn gồm 2 chỉ số $L, R$ (1-indexed).
# Hãy in ra tổng các phần tử từ $A[L]$ đến $A[R]$.
from itertools import accumulate
line1 = input().split()
while not line1:
    line1 = input().split()
n,q = int(line1[0]), int(line1[1])

line2 = input().split()
while not line2 or len(line2) < n:
    line2.extend(input().split())
a = [int(x) for x in line2[:n]]

pref = [0] + list(accumulate(a))
for _ in range(q):
    qr = input().split()
    while not qr:
        qr = input().split()
    l,r = int(qr[0]),int(qr[1])
    print(pref[r]- pref[l-1])