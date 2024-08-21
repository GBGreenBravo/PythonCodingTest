# 20240821
# 33:00
# 1 / 2


def start_from(bottom_idx):  # bottom_idx를 받아 해당되는 경우의 옆면 최대값을 반환
    mx = 0
    bottom_num = dices[0][bottom_idx]  # 맨 밑면의 숫자

    for dice in dices:
        now_dice = list(dice)  # 현재 주사위
        while True:
            if now_dice[0] == bottom_num:  # 밑면이 되어야 하는 수가 0번 index에 있을 때
                break
            else:
                now_dice.append(now_dice.pop(0))  # index 하나씩 당기기  =>  굳이 배열을 변환시키지 않고, index로만 접근해도 됨.

        mx += max([now_dice[i] for i in range(6) if i != 0 and i != 3])  # 0번인 밑면과 3번인 윗면을 제외한, 옆면 중 최대값
        bottom_num = now_dice[3]  # 다음 반복문을 위해 현재의 윗면을 아랫면으로 저장

    return mx  # 옆면 중 최대값 반환


n = int(input())
dices = []
for _ in range(n):
    a, b, c, d, e, f = map(int, input().split())
    dices.append((a, b, c, f, d, e))  # 0 - 3 / 1 - 4 / 2 - 5 가 반대편이 되도록 재정비

# 밑면 정해지면 윗면도 정해지므로, 6개의 경우만 생각하면 됨. (옆면은 회전 가능하므로 최대값만 조회할 것이기 때문)
print(max(start_from(0), start_from(1), start_from(2), start_from(3), start_from(4), start_from(5)))
# 6개의 숫자가 밑면이 될때의 최대값 중 최대값 출력
