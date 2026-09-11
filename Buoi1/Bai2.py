def SoNguyenTo (x):
    if x < 2:
        return False
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

for i in range(100):
    if SoNguyenTo(i):
        print(i,end = "\n")
