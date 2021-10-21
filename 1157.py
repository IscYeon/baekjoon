words = input().upper()
unique_words = list(set(words))

cnt_list = []
for i in unique_words:
    cnt = words.count(i)
    cnt_list.append(cnt)

'''
print(unique_words)
print(cnt_list)
'''

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))
    print(unique_words[max_index])

# print(max_index)
