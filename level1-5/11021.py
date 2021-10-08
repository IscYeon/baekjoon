import sys
t = sys.stdin.readline()
t = int(t)

for i in range(t):
    x, y = map(int, sys.stdin.readline().split())
    cSequance = str(i+1)
    print("Case #"+cSequance+":", x + y)

# should change int to str
