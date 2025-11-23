k = int(input())
result = []
for i in range(k):
    a = list(map(int, input().split()))

    n = a[0]
    m = a[1]

    d = 19*m + (n + 239)*(n + 366)/2
    result.append(d)

for r in result:
    print(int(r))