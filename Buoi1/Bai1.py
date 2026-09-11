n = int(input("nhap so so nguyen: "))
ds = []
for i in range(n):
    a = int(input(f"nhap so thu {i+1}: "))
    ds.append(a)
print(ds, sum(ds), sum(ds)/n, max(ds), min(ds))