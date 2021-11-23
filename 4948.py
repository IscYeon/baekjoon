while True:
    n = int(input())
    m = 2*n
    if n == 0:
        break
    else:
        sosu = [0] * (m+1)
        for i in range(2, m+1):
            if sosu[i] == 0:
                for j in range(i+i,m+1,i):
                    sosu[j] = 1

        total = sosu[n+1:m+1]
        print(total.count(0))
