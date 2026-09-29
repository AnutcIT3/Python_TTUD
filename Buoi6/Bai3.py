import sys

# 1. Cấu trúc Trie dạng Dictionary tối giản
def tao_nut():
    # Mỗi nút gồm: {'con': {}, 'ket_thuc': False}
    return {'con': {}, 'ket_thuc': False}

# 2. Thao tác 1 s: Thêm từ vào Trie
def them(goc, tu):
    nut = goc
    for ch in tu:
        if ch not in nut['con']:
            nut['con'][ch] = tao_nut()
        nut = nut['con'][ch]
    nut['ket_thuc'] = True

# 3. Thao tác 2 s: Kiểm tra từ có trong Trie hay không
def tim(goc, tu):
    nut = goc
    for ch in tu:
        if ch not in nut['con']:
            return False
        nut = nut['con'][ch]
    return nut['ket_thuc']

# --- LUỒNG CHẠY TRỰC TIẾP ---

# Khởi tạo gốc Trie
goc = tao_nut()

# Đọc số lượng thao tác Q
line1 = sys.stdin.readline().split()
while not line1:
    line1 = sys.stdin.readline().split()
q = int(line1[0])

# Xử lý Q thao tác
for _ in range(q):
    line = sys.stdin.readline().split()
    while not line:
        line = sys.stdin.readline().split()
    
    loai = line[0]
    s = line[1]
    
    if loai == '1':
        them(goc, s)
    elif loai == '2':
        if tim(goc, s):
            print("YES")
        else:
            print("NO")