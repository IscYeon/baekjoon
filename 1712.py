a, b, c = map(int, input().split())

if b >= c:
    x = -1
else:
    x = a/(c-b)
    x += 1

print(int(x))


# 21억까지 접근하고 시간제한도 있으므로 반복문으로는 풀수 없음
'''
import sys
input = sys.stdin.readline()

fixed_cost, variable_cost, price = map(int, input.split())
BEPnum = 0
total_cost = 0
profit = 0

if price < variable_cost:
    BEPnum = -1

while price > variable_cost:
    BEPnum += 1
    print(BEPnum)
    total_cost = variable_cost * BEPnum
    print(total_cost)
    profit = price * BEPnum
    print(profit)
    if profit > fixed_cost + total_cost:
        break

print(BEPnum)
'''
