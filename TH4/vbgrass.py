
# Cho một bản đồ cánh đồng kích thước $R \times C$. 
# Mỗi khóm cỏ được mô tả là 1 ký tự '#' riêng lẻ hoặc 2 ký tự '#' nằm kề nhau (chung 1 cạnh).
# Yêu cầu đếm tổng số khóm cỏ. 
# 1. Đọc R và C
line1 = input().split()
while not line1:
    line1 = input().split()
R, C = int(line1[0]), int(line1[1])

# 2. Đọc R dòng mô tả cánh đồng
grid = []
for _ in range(R):
    line = input().strip()
    while not line:
        line = input().strip()
    grid.append(line)

# 3. Đếm số khóm cỏ
count = 0
for i in range(R):
    for j in range(C):
        if grid[i][j] == '#':
            has_top = (i > 0 and grid[i - 1][j] == '#')
            has_left = (j > 0 and grid[i][j - 1] == '#')
            
            if not has_top and not has_left:
                count += 1

# 4. In kết quả
print(count)
