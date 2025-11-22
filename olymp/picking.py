x, y, z = map(int, input().split())
total = x + y

if z > total:
    print("Impossible")
else:
    print(total - z)