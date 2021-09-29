num = int(input())
numOriginal = num
count = 0

while True:
    tens = num // 10                                 #덧셈 파트 시작
    units = num % 10
    numList = [tens, units]
    tuSum = numList[0] + numList[1]
#-------------------------------------
    tens2 = tuSum // 10                              #이어붙이기 파트 시작
    units2 = tuSum % 10
    numList2 = [tens2, units2]
    if numList[1] == 0:
        num = numList2[1]
    else:
        numNew = str(numList[1])+str(numList2[1])
        num = int(numNew)

    count = count + 1

    if num == numOriginal:
        break

print(count)
