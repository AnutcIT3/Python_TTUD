from collections import Counter
from functools import reduce

def common_chars(words):
    if not words:
        return []
    
    # 1. Chuyển từng từ thành một Counter object
    counters = [Counter(word) for word in words]
    
    # 2. Dùng reduce và toán tử & để lấy giao (intersection) của tất cả các Counter
    # Toán tử & giữ lại giá trị tần suất nhỏ nhất giữa các từ
    common = reduce(lambda a, b: a & b, counters)
    
    # 3. Chuyển kết quả Counter thành danh sách các ký tự
    return list(common.elements())

# --- Ví dụ 1: Giữ nguyên số lần lặp (Ví dụ: LeetCode 1002 - Find Common Characters) ---
words1 = ["bella", "label", "roller"]
print("Tất cả ký tự chung (tính cả tần suất):", common_chars(words1))
# Output: ['e', 'l', 'l']

# --- Ví dụ 2: Nếu chỉ muốn lấy danh sách ký tự duy nhất (Unique) ---
words2 = ["cool", "lock", "cook"]
unique_common = list(reduce(lambda a, b: a & b, [Counter(w) for w in words2]).keys())
print("Ký tự chung duy nhất:", unique_common)
# Output: ['c', 'o']