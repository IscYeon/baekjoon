a = input()
b = input()

a = int(a)
b = int(b)

print(a * (b%10))
print(a * ((b%100)//10))
print(a * (b//100))
print(a * b)
