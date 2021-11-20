import math

N = int(input())
numbers = list(map(int, input().split(' ', N-1)))

count = 0
for i in numbers:
    last = math.ceil(math.sqrt(i)) + 1
    if i != 1:
        count += 1
    for j in range(2, last):
        if i == j:
            break
        if i%j == 0:
            count -= 1
            break

print(count)
