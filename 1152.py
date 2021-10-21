str_list = list(input().split(' '))

if str_list[0] == '':
    del(str_list[0])
if str_list[-1] == '':
    del(str_list[-1])

print(len(str_list))
