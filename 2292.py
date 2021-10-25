#numbers = list(range(5,10))
#print(numbers)

x = int(input())
n_max = 1
n = 0
while True:
    n_max = n_max + (6*n)
    #print(n_max)
    if n_max >= x:
        break
    n += 1

print(n+1)

'''
x = int(input())
n_max = 1
n = 0
for i in range(1000000000):
    n_max = n_max + (6*n)
    #print(n_max)
    if n_max >= x:
        break
    n += 1

print(n+1)
'''
