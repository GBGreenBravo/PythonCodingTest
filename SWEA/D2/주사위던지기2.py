# 20240806
# 05:45
# 1 / 1


def dice(number, arr):
    if number == n:
        sorted_arr = tuple(sorted(arr))
        if sorted_arr not in dice_set:  # 이전과 중복되지 않는 조합이라면, 출력하고 dice_set에 조합 추가.
            print(*arr)
            dice_set.add(sorted_arr)
        return

    for i in range(1, 7):
        dice(number + 1, arr + [i])


t = int(input())
for test in range(1, t + 1):
    n = int(input())
    print(f"#{test}")

    dice_set = set()  # 중복조합을 거르기 위한 set
    dice(0, [])


# set 비교할 필요 없이, 이전에 굴렸던 주사위보다 작은 수는 안 굴리면 됨.
"""
def dice(number, arr, mx_dice):  # dice 굴린 횟수, 이전에 굴린 dice 배열, 이전에 굴린 최대 dice
    if number == n:
        print(*arr)
        return
 
    for i in range(mx_dice, 7):  # 이전에 굴렸던 주사위보다 작은 수는 안 굴리면 중복되는 조합 안 나옴.
        dice(number + 1, arr + [i], i)
 
 
t = int(input())
for test in range(1, t + 1):
    n = int(input())
    print(f"#{test}")
 
    dice(0, [], 1)
"""