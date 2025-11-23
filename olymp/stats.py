n = int(input())
a = list(map(int, input().split()))

c = []
b = []

for i in a:
    if i % 2 == 0:
        c.append(i)
    else:
        b.append(i)

print(*b)
print(*c)

if len(c) >= len(b):
    print("YES")
else:
    print("NO")