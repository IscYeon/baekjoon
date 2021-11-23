M, N=map(int,input().split())

prime=[0]*(N+1)

for i in range (2, N+1):
    if prime[i] == 0:
        for j in range (i+i, N+1, i):
            prime[j] = 1

for i in range(M,N+1):
    if i<2:
        continue
    elif prime[i] == 0:
        print(i)
