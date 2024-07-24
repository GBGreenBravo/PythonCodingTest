# 20240724
# 04:43

n = int(input())

group_word_cnt = 0

for _ in range(n):
    word = str(input())
    word_set = [word[0]]
    for w in word:
        if w == word_set[-1]:
            continue
        else:
            word_set.append(w)

    if len(word_set) == len(set(word_set)):
        group_word_cnt += 1

print(group_word_cnt)
