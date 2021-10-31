import math
testcase = int(input())

for i in range(testcase):
    H, W, N = map(int, input().split())
    if N <= H*W:
        w = math.ceil(N/H)
        h = N%H
        if h == 0:
            h = H
        print(str(h) + '{0:02d}'.format(w))
