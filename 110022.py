import sys
t = sys.stdin.readline()
t = int(t)

for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    sum = x + y
    x, y = str(x), str(y)
    caseSeq = str(i+1)
    print("Case #"+caseSeq+": "+x+" + "+y+" =", sum)
