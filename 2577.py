num1 = int(input())
num2 = int(input())
num3 = int(input())

numMulti = num1 * num2 * num3
numMultiList = list(str(numMulti))

for i in range(10):
    frequancy = numMultiList.count(str(i))
    print(frequancy)
