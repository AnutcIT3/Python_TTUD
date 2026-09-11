import heapq
 
a = [3, 1, 4, 1, 5, 9, 2, 6]
print(heapq.nlargest(3, a))   # [9, 6, 5] — cach nhanh, co san
 
# Tu cai bang min-heap kich thuoc k (khi a rat lon / la luong du lieu)
def top_k_lon_nhat(a, k):
    heap = a[:k]
    heapq.heapify(heap)
    for x in a[k:]:
        if x > heap[0]:
            heapq.heapreplace(heap, x)   # thay phan tu nho nhat
    return sorted(heap, reverse=True)
 
print(top_k_lon_nhat(a, 3))   # [9, 6, 5]


