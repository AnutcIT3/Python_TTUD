import sys

# 1. Hàm Trie dựng cây lưu từ điển
def tao_nut():
    return {'con': {}, 'tu_id': -1}

def them_vao_trie(goc, tu, tu_id):
    nut = goc
    for ch in tu:
        if ch not in nut['con']:
            nut['con'][ch] = tao_nut()
        nut = nut['con'][ch]
    nut['tu_id'] = tu_id

# 2. Thuật toán Rabin-Karp tìm tất cả các lần xuất hiện của các từ trong T
def rabin_karp_multipattern(T, dictionary):
    if not T or not dictionary:
        return {}

    # Nhóm các từ theo độ dài để chạy Rabin-Karp tối ưu
    by_length = {}
    for i, word in enumerate(dictionary):
        l = len(word)
        if l not in by_length:
            by_length[l] = []
        by_length[l].append((word, i))

    counts = [0] * len(dictionary)
    base = 256
    mod = 10**9 + 7
    n = len(T)

    for m, words in by_length.items():
        if m > n:
            continue
        
        # Bảng băm các từ có cùng độ dài m
        word_hashes = {}
        for word, idx in words:
            h_val = 0
            for ch in word:
                h_val = (h_val * base + ord(ch)) % mod
            if h_val not in word_hashes:
                word_hashes[h_val] = []
            word_hashes[h_val].append((word, idx))

        h = pow(base, m - 1, mod)
        curr_hash = 0
        for i in range(m):
            curr_hash = (curr_hash * base + ord(T[i])) % mod

        for i in range(n - m + 1):
            if curr_hash in word_hashes:
                sub = T[i : i + m]
                for word, idx in word_hashes[curr_hash]:
                    if sub == word:
                        counts[idx] += 1
            
            if i < n - m:
                curr_hash = ((curr_hash - ord(T[i]) * h) * base + ord(T[i + m])) % mod

    return counts

# --- LUỒNG CHẠY TRỰC TIẾP ---

# Read input
input_data = sys.stdin.read().split()
if input_data:
    n = int(input_data[0])
    dictionary = input_data[1 : n + 1]
    T = input_data[n + 1] if len(input_data) > n + 1 else ""

    # Tạo Trie chứa các từ
    goc = tao_nut()
    for idx, word in enumerate(dictionary):
        them_vao_trie(goc, word, idx)

    # Đếm số lần xuất hiện bằng Rabin-Karp
    counts = rabin_karp_multipattern(T, dictionary)

    max_count = 0
    best_word = ""

    # Lọc từ có tần suất lớn nhất, ưu tiên thứ tự từ điển nhỏ nhất
    for idx, word in enumerate(dictionary):
        cnt = counts[idx]
        if cnt > max_count:
            max_count = cnt
            best_word = word
        elif cnt == max_count and cnt > 0:
            if word < best_word:
                best_word = word

    if max_count == 0:
        print("NO MATCH")
    else:
        print(f"{best_word} {max_count}")