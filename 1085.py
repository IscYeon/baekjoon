x, y, w, h = map(int, input().split())

m1 = x
m2 = y
m3 = w - x
m4 = h - y

move = [m1,m2,m3,m4]
move.sort()

print(move[0])
