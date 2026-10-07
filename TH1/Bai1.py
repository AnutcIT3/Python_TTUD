# Dùng Union-Find đếm số "đảo bạn bè" (nhóm bạn bè liên thông) từ danh sách các cặp bạn bè cho trước
class UnionFind:
    def __init__(self, n):
        self.cha = list(range(n))
        self.hang = [0] * n
 
    def tim(self, x):
        if self.cha[x] != x:
            self.cha[x] = self.tim(self.cha[x])   # nen duong di
        return self.cha[x]
 
    def hop(self, x, y):
        rx, ry = self.tim(x), self.tim(y)
        if rx == ry:
            return False              # da cung tap hop -> tao chu trinh
        if self.hang[rx] < self.hang[ry]:
            rx, ry = ry, rx
        self.cha[ry] = rx              # hop theo hang
        if self.hang[rx] == self.hang[ry]:
            self.hang[rx] += 1
        return True

# bai toan
def dem_dao_ban_be(n, cac_cap):
    uf = UnionFind(n)
    for a, b in cac_cap:
        uf.hop(a, b)
    return uf.so_nhom
print(dem_dao_ban_be(6, [(0, 1), (1, 2), (3, 4)]))

