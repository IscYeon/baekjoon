T = int(input())

P = ""
for i in range(T):
    R, S = input().split()
    for j in S:
        P += j * int(R)
    print(P)
    P = ""
