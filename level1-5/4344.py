num = int(input())

for i in range(num):
    case = list(map(int, input().split()))
    studentNo = case[0]
    averageClass = (sum(case) - case[0]) / case[0]
    averageOver = 0
    for j in range(1,studentNo+1):
        if case[j] > averageClass:
            averageOver = averageOver + 1

    if averageOver == 0:
        averagePer = 0
        print("{:.3f}%".format(averagePer))
    else:
        averagePer = (averageOver/studentNo) * 100
        print("{:.3f}%".format(averagePer))
