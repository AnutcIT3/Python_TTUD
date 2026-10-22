
line1 = input().split()
while not line1:
    line1 = input().split()
n = int(line1[0])

a = []
for _ in range(n):
    line = input().split()
    while not line:
        line = input().split()
    a.append(int(line[0]))

left = [0] * n
stack = []
for i in range(n):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    left[i] = stack[-1] + 1 if stack else 0
    stack.append(i)

right = [0] * n
stack = []
for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] >= a[i]:
        stack.pop()
    right[i] = stack[-1] - 1 if stack else n - 1
    stack.append(i)

max_square_side = 0
for i in range(n):
    width = right[i] - left[i] + 1
    if width >= a[i]:
        max_square_side = max(max_square_side, a[i])

# 6. In kết quả
print(max_square_side)