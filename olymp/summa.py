n = int(input())
s = 0
if n > 0:
    for i in range(1, n + 1):
        s = s + i

elif n < 1:
    for i in range(n, 2):
        s = s + i

print(s)