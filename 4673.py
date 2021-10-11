def formula(a):
    aList = list(a)
    aAdd = 0
    for i in aList:
        aAdd = aAdd + int(i)
    return int(a) + aAdd

numList = []

for i in range(0, 10000):
    result = formula(str(i))
    numList.append(result)

numListSet = set(numList)
numList = list(numListSet)
numList.sort()
#print(numList)

for j in range(0, 10000):
    if numList[j] > 10000:
        break
    elif numList[j+1] - numList[j] == 1:
        continue
    else:
        print(numList[j] + 1)









# 다른 사람 풀이

'''
def d(n):
    not_make = []
    make = []
    for i in range(10000):
        a = list(map(int, str(i)))
        i += sum(a)
        if i not in not_make and i <= 10000:
            not_make.append(i)
    for p in range(n, 10000):
        if p not in not_make:
            print(p)
    return

d(1)
'''
