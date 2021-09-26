import sys

n, x = map(int, sys.stdin.readline().split())
vList = list(map(int, sys.stdin.readline().split()))

resultList = list()

if len(vList) == n:
    for i in vList:
        if i < x:
            resultList.append(i)
        else:
            continue

for j in resultList:
    print(j, end=" ")
