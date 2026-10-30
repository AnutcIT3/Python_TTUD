line = input().split()
while not line:
    line = input().split()
n, k = int(line[0]), int(line[1])

line_c = input().split()
while not line_c or len(line_c) < k:
    line_c.extend(input().split())
a = [int(x) for x in line_c[:k]]

# Thuật toán sinh tổ hợp kế tiếp
i = k - 1
while i >= 0 and a[i] == n - k + i + 1:
    i -= 1

if i < 0:
    print(-1)
else:
    a[i] += 1
    for j in range(i + 1, k):
        a[j] = a[j - 1] + 1
    print(*a)