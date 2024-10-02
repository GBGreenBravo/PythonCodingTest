# 20241001
# 55:22
# 1 / 3

# 17779_게리맨더링2

"""
풀이 시간: 55분 (16:30 - 17:25)
풀이 시도: 1 / 3


1. 문제 정독 & 풀이 구상 (16:30 - 16:35)
    이전 풀이방식이 조금은 독특한 풀이였기에,
    조금 더 보편적인 (코드리뷰에서 봤던) 풀이로 구현해보고자 했습니다.
    (얼핏 본 풀이가 내 풀이가 되는 게 아니라, 직접 구현해봐야 내 풀이가 됨을 확인할 수 있었던 문제였습니다.)


2. 구현 (16:35 - 16:49)


3. 디버깅 (16:49 - 17:02)
    우상단 벽의 길이를 구할 때, 유효한 범위를 설정해주지 않아, 해당 이슈에 대한 디버깅에 시간이 많이 소요됐습니다.
    특히 프린트를 찍을 곳을 잘못 설정해서, 디버깅모드로 해당 중복 실수를 확인하고 바로잡을 수 있었습니다.


4. 틀렸습니다 (17:02 - 17:23)
    문제 구상에 대해 벽 길이가 서로 다른 경우도 손으로 그려보고 확인했어야 하는데, 그렇지 않아서 실수했던 부분이 있었습니다.


5. 틀렸습니다 (17:23 - 17:25)
    위와 같은 이유로 틀렸습니다.

    실제 시험에서는 더 꼼꼼히 구상 단계에서 다양한 케이스를 미리 그려보고, 검증해야 할 것입니다.
"""


def check(sy, sx, length1, length2):
    group_flag = [[0] * n for _ in range(n)]

    for row in range(sy + 1):
        for col in range(sx + 1):
            group_flag[row][col] = 2
        for col in range(sx + 1, n):
            group_flag[row][col] = 3

    group_flag[sy][sx] = 1
    y, lx, rx = sy, sx, sx
    ld, rd = 0, 0
    for _ in range(length1 + length2):
        y += 1
        ld += 1
        rd += 1
        lx -= 1 if ld <= length1 else -1
        rx += 1 if rd <= length2 else -1
        left = 2 if ld < length1 else 4
        right = 3 if rd <= length2 else 5
        for col in range(lx):
            group_flag[y][col] = left
        for col in range(lx, rx + 1):
            group_flag[y][col] = 1
        for col in range(rx + 1, n):
            group_flag[y][col] = right

    for row in range(sy + length1 + length2 + 1, n):
        for col in range(sx - length1 + length2):
            group_flag[row][col] = 4
        for col in range(sx - length1 + length2, n):
            group_flag[row][col] = 5

    group_cnt = [None] + [0] * 5
    for y in range(n):
        for x in range(n):
            group_cnt[group_flag[y][x]] += area[y][x]

    global min_answer
    min_answer = min(min_answer, max(group_cnt[1:]) - min(group_cnt[1:]))


n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

min_answer = 100 * n**2
for i in range(0, n - 2):
    for j in range(1, n - 1):

        for l1 in range(1, j + 1):
            for l2 in range(1, min(n - 1 - (i + l1), n - 1 - j) + 1):
                check(i, j, l1, l2)

print(min_answer)
