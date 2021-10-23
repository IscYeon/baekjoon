#!/usr/bin/env python3
test_case = int(input())
groupWords = test_case

for i in range(test_case):
    words = input()
    check_words = []
    check_words.append(words[0])
    for j in range(1, len(words)):
        if words[j] != words[j-1] and words[j] in check_words:
            groupWords -= 1
            break
        else:
            check_words.append(words[j])

print(groupWords)
