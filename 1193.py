
x = int(input())

count = 0
count_sum = 0

while x > count_sum:
    count += 1
    count_sum += count
    #print(count)
    #print(count_sum)

count_sum -= count
#print(count_sum)

if count%2 == 1: # 홀수일때
    bot = x - count_sum
    top = count - bot + 1
else: # 짝수일때
    top = x - count_sum
    bot = count - top + 1

print(f"{top}/{bot}")
