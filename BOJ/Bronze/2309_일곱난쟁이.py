# 20240722
# 04:49

from copy import deepcopy

the_short = [int(input()) for _ in range(9)]
sum_the_short = sum(the_short)
answer = []

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum_the_short - the_short[i] - the_short[j] == 100:
            answer = deepcopy(the_short)
            answer.remove(the_short[i])
            answer.remove(the_short[j])
            answer.sort()
            break

print(*answer, sep="\n")


# 이중반복문 탈출 위한 플래그 추가하면 아래와 같이 됨.
'''
from copy import deepcopy

the_short = [int(input()) for _ in range(9)]
sum_the_short = sum(the_short)
done = False
answer = []

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum_the_short - the_short[i] - the_short[j] == 100:
            answer = deepcopy(the_short)
            answer.remove(the_short[i])
            answer.remove(the_short[j])
            answer.sort()
            done = True
            break
    if done:
        break

print(*answer, sep="\n")
'''


# 투포인터로 푼다면 아래와 같이.
'''
the_short = [int(input()) for _ in range(9)]
the_short.sort()

target = sum(the_short) - 100
start, end = 0, 8

while start < end:
    now = the_short[start] + the_short[end]
    if now == target:
        del the_short[end]
        del the_short[start]
        break
    elif now < target:
        start += 1
    else:  # elif now > target:
        end -= 1

print(*the_short, sep="\n")
'''