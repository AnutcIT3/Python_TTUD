# def binh_phuong_gen(n):
#     for i in range(n):
#         yield i*i

# def fibonacci_vo_han():
#     a,b = 0,1
#     while True:
#         yield a
#         a, b = b, a+b

# gen = fibonacci_vo_han()
# for _ in range(10):
#     print(next(gen),end=" ")
# n = int(input('nhap so n: '))
# for x in binh_phuong_gen(n):
#     print(x)
def sinh_so(n):
    for i in range(1, n + 1):
        yield i
 
def binh_phuong(nums):
    for x in nums:
        yield x * x
 
def loc_le(nums):
    for x in nums:
        if x % 2 != 0:
            yield x
 
# Ghep cac generator thanh 1 "day chuyen" xu ly:
ket_qua = loc_le(binh_phuong(sinh_so(10)))
print(list(ket_qua))   # [1, 9, 25, 49, 81]
def day_nhi_phan_ke_tiep(x):
    """Cong them 1 (nhi phan, co nho) vao day bit x."""
    n = len(x)
    i = n - 1
    while i >= 0 and x[i] == 1:
        x[i] = 0
        i -= 1
    if i < 0:
        return None          # da la 11...1 -> het day
    x[i] = 1
    return x
 
x = [0, 0, 0]
while x is not None:
    print(x)
    x = day_nhi_phan_ke_tiep(x)
# [0,0,0] [0,0,1] [0,1,0] [0,1,1] [1,0,0] [1,0,1] [1,1,0] [1,1,1]
print("Hoan vi")
def hoan_vi_ke_tiep(a):
    n = len(a)
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:      # tim i giam dan tu phai sang
        i -= 1
    if i < 0:
        return None                          # da la hoan vi cuoi cung
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]                  # doi cho a[i], a[j]
    a[i+1:] = reversed(a[i+1:])               # dao nguoc phan duoi
    return a
 
a = [1, 2, 3, 4]
while a is not None:
    print(a)
    a = hoan_vi_ke_tiep(a)
# [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
print("So nguyen to")
def dem_so_dao(luoi):
    n, m = len(luoi), len(luoi[0])
    da_tham = [[False]*m for _ in range(n)]
    def danh_dau(r, c):                       # loang tu (r,c)
        if r<0 or r>=n or c<0 or c>=m or da_tham[r][c] or luoi[r][c]==0:
            return
        da_tham[r][c] = True
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            danh_dau(r+dr, c+dc)
    so_dao = 0
    for i in range(n):
        for j in range(m):
            if luoi[i][j]==1 and not da_tham[i][j]:
                danh_dau(i, j); so_dao += 1
    return so_dao



