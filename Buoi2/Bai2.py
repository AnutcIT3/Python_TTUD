#Tự cài thuật toán sinh cấu hình kế tiếp để liệt kê mọi tổ hợp chập k của {1,...,n} theo thứ tự từ điển (không dùng itertools).
def to_hop_ke_tiep(a, n, k):
    """
    Sinh tổ hợp chập k kế tiếp của {1, ..., n}.
    Trả về cấu hình mới hoặc None nếu đã là cấu hình cuối cùng.
    """
    i = k - 1
    # 1. Tìm vị trí i từ phải sang chưa đạt giá trị tối đa (n - k + i + 1)
    while i >= 0 and a[i] == n - k + i + 1:
        i -= 1

    # 2. Nếu đã là cấu hình cuối cùng (ví dụ: [n-k+1, ..., n])
    if i < 0:
        return None

    # 3. Tăng a[i] lên 1
    a[i] += 1

    # 4. Đặt các phần tử từ i + 1 đến k - 1 thành các giá trị tối thiểu hợp lệ tiếp theo
    for j in range(i + 1, k):
        a[j] = a[j - 1] + 1

    return a


def liet_ke_to_hop(n, k):
    # Cấu hình khởi đầu: [1, 2, ..., k]
    a = list(range(1, k + 1))

    while a is not None:
        print(a)
        a = to_hop_ke_tiep(a, n, k)


# Ví dụ: Liệt kê tổ hợp chập 3 của {1, 2, 3, 4, 5}
n = 5
k = 3
print(f"Danh sach to hop chap {k} cua {n}:")
liet_ke_to_hop(n, k)