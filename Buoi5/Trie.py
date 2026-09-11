class TrieNode:
    def __init__(self):
        self.con = {}          # ky tu -> TrieNode con
        self.ket_thuc = False   # co phai cuoi 1 tu hay khong
 
class Trie:
    def __init__(self):
        self.goc = TrieNode()
 
    def them(self, tu):
        nut = self.goc
        for ch in tu:
            if ch not in nut.con:
                nut.con[ch] = TrieNode()
            nut = nut.con[ch]
        nut.ket_thuc = True
 
    def _di_toi(self, s):
        nut = self.goc
        for ch in s:
            if ch not in nut.con: return None
            nut = nut.con[ch]
        return nut
 
    def tim(self, tu):
        nut = self._di_toi(tu)
        return nut is not None and nut.ket_thuc
def goi_y(trie, tien_to):
    nut = trie._di_toi(tien_to)
    if nut is None: return []
    ket_qua = []
    def duyet(nut, tu_hien_tai):
        if nut.ket_thuc:
            ket_qua.append(tu_hien_tai)
        for ch, con in nut.con.items():
            duyet(con, tu_hien_tai + ch)
    duyet(nut, tien_to)
    return ket_qua
 
t = Trie()
for tu in ["python", "pytorch", "java", "javascript"]:
    t.them(tu)
 
print(t.tim("python"))       # True
print(goi_y(t, "py"))        # ['python', 'pytorch']
print(goi_y(t, "java"))      # ['java', 'javascript']
