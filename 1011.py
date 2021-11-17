#!/usr/bin/env python3

testCase = int(input())



for i in range(testCase):
    start, end = map(int, input().split())
    distance = end - start
    howMany = 0

    if distance <= 3:
        howMany += distance
    elif distance == 4:
        howMany += 3
    else:
        a = 1
        b = 4
        c = 3
        for i in range(distance):
            if b >= distance:
                break
            a = b
            c = c + 2
            b = b + c
        if b == distance:
            howMany = c
        elif distance > b - ((c//2) + 1):
            howMany = c
        else:
            howMany = c - 1

    print(howMany)
