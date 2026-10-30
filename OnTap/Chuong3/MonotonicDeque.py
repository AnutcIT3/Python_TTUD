# Cho mảng $A$ gồm $N$ số nguyên và số nguyên $K$. 
# Tìm giá trị nhỏ nhất của mọi cửa sổ trượt kích thước $K$ từ trái sang phải.
from collections import deque

line1 = input().split()
while not line1:
    line1 = input().split()
n, k = int(line1[0]), int(line1[1])

line2 = input().split()
while not line2 or len(line2) < n:
    line2.extend(input().split())
a = [int(x) for x in line2[:n]]

dq = deque()
res = []

for i in range(n):
    # Loại bỏ chỉ số đã vượt quá cửa sổ trượt
    if dq and dq[0] <= i - k:
        dq.popleft()
    # Loại bỏ các giá trị lớn hơn a[i] ở cuối deque để duy trì dãy tăng dần
    while dq and a[dq[-1]] >= a[i]:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        res.append(a[dq[0]])

print(*res)