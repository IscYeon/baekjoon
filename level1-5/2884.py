H, M = map(int,input().split())

if 0 < H <= 23:
    if M >= 45:
        M = M - 45
        H = H
    elif M < 45:
        M = (M - 45) + 60
        H = H - 1
elif H == 0:
    if M >= 45:
        M = M - 45
        H = H
    elif M < 45:
        M = (M - 45) + 60
        H = 23
print(H, M)

#아래는 다른사람 답안, 입력값을 리스트로 받아서 꺼내는방식이 신기해서 참고용으로 가져옴

'''
HM = list(map(int,input().split()))
print(HM)
H,M = HM[0],HM[1]
print(H,M)
if H>0:
#M 이 45보다 작을때:
    if M<45:
        H-=1
        M +=15
    #M 이 45 이상일떄:
    else:
        M-=45
elif H == 0:
    if M<45:
        H =23
        M+=15
    else:
        M-=45
print(H,M)
'''
