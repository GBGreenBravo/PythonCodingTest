# 20241002
# 29:26
# 1 / 1

# 20061_모노모노도미노2

"""
풀이 시간: 30분 (15:21 - 15:51)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:21 - 15:27)


2. 구현 (15:27 - 15:50)
    이전 풀이와 구상&구현로직은 같으나, 코드가 더 간결해졌습니다.
    체크포인트에서 다 점검해주다가, 빨간 영역이 제대로 내려오지 않음을 확인했습니다.
    red_type의 마지막을 (0, -1)이 아닌 (0, 1)로 적었던 실수를 4분 간의 디버깅을 통해 잡아냈습니다.


3. 디버깅 (-)
"""

yellow_type = (None, ((0, 0),), ((0, 0), (0, 1)), ((0, 0), (1, 0)))
red_type = (None, ((0, 0),), ((0, 0), (1, 0)), ((0, 0), (0, -1)))


def drop_yellow(block_type, c_column):
    global yellow, score

    falling = []
    for tdy, tdx in yellow_type[block_type]:
        falling.append([0 + tdy, c_column + tdx])

    while True:
        for fy, fx in falling:
            if fy + 1 == 6 or yellow[fy + 1][fx]:
                break
        else:
            for idx, fall in enumerate(falling):
                falling[idx][0] += 1
            continue
        break

    for fy, fx in falling:
        yellow[fy][fx] = 1

    removed = []
    for row in range(2, 6):
        if sum(yellow[row]) == 4:
            removed.append(row)
    score += len(removed)
    yellow = [[0] * 4 for _ in range(len(removed))] + [yellow[r] for r in range(6) if r not in removed]

    if sum(yellow[0]):
        yellow = [[0] * 4 for _ in range(2)] + yellow[:4]
    elif sum(yellow[1]):
        yellow = [[0] * 4] + yellow[:5]


def drop_red(block_type, c_column):
    global red, score

    falling = []
    for tdy, tdx in red_type[block_type]:
        falling.append([0 + tdy, c_column + tdx])

    while True:
        for fy, fx in falling:
            if fy + 1 == 6 or red[fy + 1][fx]:
                break
        else:
            for idx, fall in enumerate(falling):
                falling[idx][0] += 1
            continue
        break

    for fy, fx in falling:
        red[fy][fx] = 1

    removed = []
    for row in range(2, 6):
        if sum(red[row]) == 4:
            removed.append(row)
    score += len(removed)
    red = [[0] * 4 for _ in range(len(removed))] + [red[r] for r in range(6) if r not in removed]

    if sum(red[0]):
        red = [[0] * 4 for _ in range(2)] + red[:4]
    elif sum(red[1]):
        red = [[0] * 4] + red[:5]


k = int(input())

yellow = [[0] * 4 for _ in range(6)]
red = [[0] * 4 for _ in range(6)]

score = 0
for _ in range(k):
    tt, aa, bb = map(int, input().split())
    drop_yellow(tt, bb)
    drop_red(tt, 3 - aa)
print(score)
print(sum(map(sum, yellow)) + sum(map(sum, red)))
