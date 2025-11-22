n = list(map(int, input().split()))
m1 = n[0]
m2 = n[1]
m3 = n[2]
if m1 > 727 or m2 > 727 or m3 > 727:
    print("Error")
elif m1 < 94 or m2 < 94 or m3 < 94:
    print("Error")
else:
    print(max(n))