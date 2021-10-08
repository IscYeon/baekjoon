def formula(n):
    nList = list(n)
    print(nList, end='')
    nAdd = 0
    for i in nList:
        nAdd = nAdd + int(i)
    return int(n) + nAdd

'''
test = input()
print(formula(test))
'''

formulaList = []

for j in range(0, 1001):
    result = formula(str(j))
    print(result)
    formulaList.append(result)

formulaListSet = set(formulaList)
formulaList = list(formulaListSet)
formulaList.sort()
print(formulaList)
