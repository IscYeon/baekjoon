import sys

input = sys.stdin.readline()
input = int(input)

for i in range(input):
    a, b = map(int,sys.stdin.readline().split())
    print(a + b)
