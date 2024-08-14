# 20240814
# 04:09
# 1 / 1

from heapq import heapify, heappop, heappush

n = int(input())
cards = [int(input()) for _ in range(n)]
heapify(cards)

sm = 0
for _ in range(n - 1):
    value = heappop(cards) + heappop(cards)
    sm += value
    heappush(cards, value)

print(sm)


# 아래는 이분탐색 풀이 코드. 이분탐색 index체크 필수..!!
"""
n = int(input())
cards = [int(input()) for _ in range(n)]
cards.sort()

sm = 0
for len_cards in range(n - 2, -1, -1):
    value = cards.pop(0) + cards.pop(0)
    sm += value

    if not cards:
        break

    left, right = 0, len_cards
    while left <= right:
        middle = (left + right) // 2

        if middle == len_cards:
            left = len_cards + 1
            break

        mid_value = cards[middle]

        if mid_value == value:
            left = middle + 1
            break
        elif mid_value > value:
            right = middle - 1
        else:  # mid_value < value
            left = middle + 1

    cards.insert(left, value)  # insert(마지막 인덱스, 값) 하면 맨 끝이 아니라, 그 앞에 추가되므로 right는 len(cards)로 설정해야 함.

print(sm)
"""