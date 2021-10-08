num = int(input())

for i in range(num):
    tot = 0
    Ocount = 0
    quiz = list(input())
    for j in range(len(quiz)):
        if quiz[j] == 'X':
            Ocount = 0
        else:
            Ocount += 1
            tot = tot + Ocount
    print(tot)
