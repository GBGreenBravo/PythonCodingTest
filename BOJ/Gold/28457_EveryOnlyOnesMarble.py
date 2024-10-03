# 20241003
# 1:36:10
# 1 / 2

"""
풀이 시간: 1시간 36분 (10:39 ~ 11:15)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (09:39 - 09:47)


2. 구현 (09:47 - 10:27)


3. 검증 (10:27 - 10:35)


4. 틀렸습니다 (10:35 - 11:15)
    n이 3인 경우에, 주사위 합이 9 이상이면 2바퀴 돌 수도 있음을 간과했음.

    구현 당시에, 황금열쇠 4번에 대해서는 고려했던 부분인데,
    보드 크기를 정확하게 인지하지 않아서 틀렸음.

    => 문제 입력 조건 꼭! 메모하고, 주사위 합 범위(2~12) 같은 것도 적어놓자..!
"""

from collections import deque


def play_game():
    global money, gold_key_idx

    now_position = 0
    society_welfare = 0
    stunned = 0

    while dices:
        aa, bb = dices.popleft()

        if stunned:
            stunned -= 1
            if aa != bb:
                continue
            else:
                stunned = 0
                if not dices:
                    continue
                aa, bb = dices.popleft()

        next_position = now_position + aa + bb
        if next_position >= 4 * n - 4:
            money += start_added_money * (next_position // (4 * n - 4))
            next_position %= 4 * n - 4

        if is_gold_key[next_position]:
            gold_flag, gold_value = gold_keys[gold_key_idx]
            gold_key_idx = (gold_key_idx + 1) % g

            if gold_flag == 1:
                money += gold_value
            elif gold_flag == 2:
                money -= gold_value
                if money < 0:
                    return False
            elif gold_flag == 3:
                money -= gold_value
                society_welfare += gold_value
                if money < 0:
                    return False
            elif gold_flag == 4:
                next_position += gold_value
                if next_position >= 4 * n - 4:
                    next_position %= 4 * n - 4
                    money += start_added_money

            if is_gold_key[next_position]:
                now_position = next_position
                continue

        if next_position in special_indexes:
            if next_position == 0:
                pass
            elif next_position == n - 1:
                stunned = 3
            elif next_position == 2 * n - 2:
                money += society_welfare
                society_welfare = 0
            elif next_position == 3 * n - 3:
                next_position = 0
                money += start_added_money

            now_position = next_position
            continue

        if is_bought[next_position] or money < city_price[next_position]:
            now_position = next_position
            continue

        money -= city_price[next_position]
        is_bought[next_position] = True
        now_position = next_position

    return sum(is_bought) == 4 * n - 4


n, money, start_added_money, g = map(int, input().split())
gold_keys = [tuple(map(int, input().split())) for _ in range(g)]
gold_key_idx = 0

special_indexes = (0, n - 1, 2 * n - 2, 3 * n - 3)
is_gold_key = [False] * (4 * n - 4)
is_bought = [True] * (4 * n - 4)
city_price = [0] * (4 * n - 4)

for ii_idx in range(4 * n - 4):
    if ii_idx in special_indexes:
        continue

    inp = input()
    if inp == 'G':
        is_gold_key[ii_idx] = True
        continue
    _, price = inp.split()
    is_bought[ii_idx] = False
    city_price[ii_idx] = int(price)

l = int(input())
dices = deque([tuple(map(int, input().split())) for _ in range(l)])

print("WIN" if play_game() else "LOSE")
