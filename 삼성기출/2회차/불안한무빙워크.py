# 20241003
# 16:57
# 1 / 2

# 20055_컨베이어벨트위의로봇

"""
풀이 시간: 17분 (15:41 ~ 15:58)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (15:41 - 15:47)


2. 구현 (15:47 - 15:57)
    이전 풀이 때는 이동처리하면서 n-1에 도달했을 때 내려주지 않아서, 직관적이지는 않았는데,
    이번에는 이동 후 바로 내려줌 처리를 해서, 조금 더 직관적으로 이해가 쉬운 구현을 했다고 생각합니다.

    원래는 사람들의 위치인 people 배열을 오름차순으로 관리하기 위해 reverse하고자 했으나,
    구현 중에 굳이 그럴 필요 없이 내림차순으로 관리해도 이상이 없음을 확인했습니다.
    그래서 구현 막바지에 해당 요소들을 변경했습니다.


3. 디버깅 (-)


4. 런타임에러 (15:57 - 15:58)
    구현 막바지에 바꿨던 부분들 중 미처 바꿔주지 못한 부분이 있어 틀렸습니다.
"""

from collections import deque

n, k = map(int, input().split())
stables = deque(map(int, input().split()))

people = []
out_of_order_cnt = 0

turn = 0
while out_of_order_cnt < k:
    turn += 1

    people = [p + 1 for p in people]
    stables.rotate(1)

    if people and people[0] == n - 1:
        people.pop(0)

    next_people = []
    for person in people:
        if (next_people and next_people[-1] == person + 1) or not stables[person + 1]:
            next_people.append(person)
        else:
            stables[person + 1] -= 1
            if not stables[person + 1]:
                out_of_order_cnt += 1
            next_people.append(person + 1)
    people = next_people

    if people and people[0] == n - 1:
        people.pop(0)

    if stables[0]:
        stables[0] -= 1
        if not stables[0]:
            out_of_order_cnt += 1
        people.append(0)

print(turn)
