# 20240723
# 36:36

# for문에서 내부적으로 i를 증감시켜도 반영 안됨. 내부적으로 증감시키고 싶다면 while문 사용해야 함.

croatian_3 = 'dz='
croatian_2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = str(input())

cnt = 0
i = 0
while i < len(word):
    if word[i:i+3] == croatian_3:
        cnt += 1
        i += 2
    elif word[i:i+2] in croatian_2:
        cnt += 1
        i += 1
    else:
        cnt += 1
    i += 1

print(cnt)

# replace()는 기존의 자료형을 변경하지 않고, 새롭게 return함을 유의하자!
"""
croatian_3 = 'dz='
croatian_2 = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
word = str(input())

cnt = 0

cnt += word.count(croatian_3)
word = word.replace(croatian_3, " ")

for c2 in croatian_2:
    cnt += word.count(c2)
    word = word.replace(c2, " ")

cnt += len(word.replace(" ", ""))

print(cnt)
"""