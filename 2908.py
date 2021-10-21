n, m = map(str, input().split())
n = n[::-1]
m = m[::-1]

if n > m:
    print(n)
elif n < m:
    print(m)
