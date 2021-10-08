'''
subjectNum = int(input())
if subjectNum > 1000:
    quit()

scoreList = map(int, list(input().split()))
scoreList = list(scoreList)
for i in scoreList:
    if i > 100 or i < 0:
        quit()
if any(scoreList) == False or subjectNum != len(scoreList):
    quit()

maxScore = max(scoreList)
sum = 0
for i in scoreList:
    newScore = i / maxScore * 100
    sum += newScore

average = sum/len(scoreList)
print(average)
'''

subjectNum = int(input())
if subjectNum > 1000:
    quit()

scoreList = map(int, list(input().split()))
scoreList = list(scoreList)
for i in scoreList:
    if i > 100 or i < 0:
        quit()
if any(scoreList) == False:
    quit()

maxScore = max(scoreList)
for i in range(subjectNum):
    scoreList[i] = scoreList[i] / maxScore * 100

print(sum(scoreList)/subjectNum)
