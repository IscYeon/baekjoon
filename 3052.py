numList = list()
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)
numList.append(int(input())%42)

newList = []

for i in numList:
    if i not in newList:
        newList.append(i)

print(len(newList))

'''
numListSet = set(numList)
numList = list(numListSet)
print(len(numList))
'''
