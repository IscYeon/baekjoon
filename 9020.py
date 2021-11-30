sosu = [0 for i in range(10001)]
sosu[1] = 1
for i in range(2, 101):
    for j in range(i * 2, 10001, i):
        sosu[j] = 1

T = int(input())
for i in range(T):
    a = int(input())
    b = a//2
    for j in range(b, 1, -1):
        if sosu[a - j] == 0 and sosu[j] == 0:
            print(j, a - j)
            break
