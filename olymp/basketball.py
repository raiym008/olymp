first = 0
second = 0
r = 0

while r < 4:
    n = list(map(int, input().split()))

    first += n[0]
    second += n[1]

    r += 1

if first > second:
    print(1)
elif second > first:
    print(2)
else:
    print('DRAW')