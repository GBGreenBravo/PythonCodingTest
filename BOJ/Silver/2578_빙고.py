# 20240726
# 12:49

bingo = [list(map(int, input().split())) for _ in range(5)]
nums = [list(map(int, input().split())) for _ in range(5)]


def check_bingo(num):
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == num:
                bingo[i][j] = 0

    cnt = 0
    for i in range(5):
        if sum(bingo[i]) == 0:
            cnt += 1
        if sum([bingo[row][i] for row in range(5)]) == 0:
            cnt += 1
    if sum([bingo[i][i] for i in range(5)]) == 0:
        cnt += 1
    if sum([bingo[i][-i-1] for i in range(5)]) == 0:
        cnt += 1

    return True if cnt >= 3 else False


for i in range(5):
    for j in range(5):
        if check_bingo(nums[i][j]):
            print(i * 5 + j + 1)
            break
    else:
        continue
    break
