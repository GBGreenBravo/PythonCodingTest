# 20240723
# 21:47

word = str(input()).upper()
word_dict = {}
for i in word:
    if i not in word_dict.keys():
        word_dict[i] = 1
    else:
        word_dict[i] += 1

mx_word = max(word_dict, key=lambda x: word_dict[x])  # dict에 max(조건 = value)해도, value가 아닌 key가 나온다.
mx1_value = word_dict[mx_word]

del word_dict[mx_word]
if word_dict:
    mx2_value = word_dict[max(word_dict, key=lambda x: word_dict[x])]

    if mx1_value == mx2_value:
        print("?")
    else:
        print(mx_word)
else:
    print(mx_word)

# count() 활용하면 아래와 같이.
"""
word = str(input()).upper()
word_lst = list(set(word))
word_cnt = []

for i in word_lst:
    word_cnt.append(word.count(i))

if word_cnt.count(max(word_cnt)) != 1:
    print("?")
else:
    print(word_lst[word_cnt.index(max(word_cnt))])
"""