a,b,c = map(int,input().split())

A = (a+b)%c
B = ((a%c)+(b%c))%c
C = (a*b)%c
D = ((a%c)*(b%c))%c

print(A)
print(B)
print(C)
print(D)
