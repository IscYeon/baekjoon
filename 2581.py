import math

M = int(input())
N = int(input())

sosu = []
for i in range(M, N+1):
    last = math.ceil(math.sqrt(i)) + 1
    sosu.append(i)
    if i == 0 or i == 1:
        sosu.remove(i)
    for j in range(2, last):
        if i == 2 or i == 3:
            break
        if i%j == 0:
            sosu.remove(i)
            break

if not sosu:
    print(-1)
else:
    print(sum(sosu))
    print(sosu[0])
