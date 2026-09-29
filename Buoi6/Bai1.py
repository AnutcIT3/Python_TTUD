import sys

# Khai báo Segment Tree
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [float('inf')] * (4 * self.n)
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        left_node = 2 * node + 1
        right_node = 2 * node + 2
        
        self._build(data, left_node, start, mid)
        self._build(data, right_node, mid + 1, end)
        self.tree[node] = min(self.tree[left_node], self.tree[right_node])

    def query(self, L, R):
        return self._query(0, 0, self.n - 1, L, R)

    def _query(self, node, start, end, L, R):
        if R < start or end < L:
            return float('inf')
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_min = self._query(2 * node + 1, start, mid, L, R)
        right_min = self._query(2 * node + 2, mid + 1, end, L, R)
        return min(left_min, right_min)


# def main():
    # 1. Nhập n và q (Dòng 1)
    line1 = input().split()
    n, q = int(line1[0]), int(line1[1])

    # 2. Nhập mảng A (Dòng 2 - có thể gõ trên 1 dòng hoặc nhiều dòng)
    A = []
    while len(A) < n:
        A.extend(map(int, input().split()))

    # Khởi tạo cây Segment Tree
    st = SegmentTree(A)

    # 3. Nhập q truy vấn và lưu kết quả
    results = []
    for _ in range(q):
        line = input().split()
        while not line:  # Bỏ qua dòng trống nếu vô tình nhấn Enter
            line = input().split()
        L, R = int(line[0]) - 1, int(line[1]) - 1
        results.append(st.query(L, R))

    # 4. In kết quả ra màn hình
    for res in results:
        print(res)

# if __name__ == '__main__':
#     main()