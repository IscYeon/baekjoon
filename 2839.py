#!/usr/bin/env python3

N = int(input())
bag = -1

if N%5 == 0:
    bag = N//5
elif N%5 == 1:
    bag = N//5 - 1
    bag += 2
elif N%5 == 4 and N != 4:
    bag = N//5 - 1
    bag += 3
elif N%5 == 3:
    bag = N//5 + 1
elif N%5 == 2 and N != 7:
    bag = N//5 - 2
    bag += 4

print(bag)
