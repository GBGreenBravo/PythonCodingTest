# 20240906
# 33:00
# 1 / 1

"""
풀이 시간: 33분 (14:45 ~ 15:18)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:45 - 14:52)
    문제를 읽으며, 2**n에 대해 재귀함수로 풀었던 다른 문제들이 생각났고,
    그러한 재귀함수를 활용하기로 생각했습니다.

    문제풀이를 구상할 때, 하나의 풀이에 3개의 독립적인 부분이 있음을 확인했습니다.
    1) 부분 격자의 시계방향 회전
    2) 얼음 양 줄이기
    3) 답변 출력
    1)과 2)는 Q번의 반복문 내에서, 각각에 대한 함수 호출을 해주면 됐고,
    그 이후에 3)에 따른 답변 출력을 하면 됐습니다.


2. 구현 (14:52 - 15:16)
    부분 격자의 시계방향을 구현하려 할 때,
    N이 6까지기도 하고, Q번의 재귀함수 속에서 매번 시계방향 회전 가중치 (dy, dx)를 계산해주는 것보다,
    N이 0~6일 때의, 가중치 2차원 배열들을 룩업테이블(?)에 담으면 더 편리하겠다는 생각을 했습니다.
    따라서 코드 윗 부분에서 해당 룩업테이블를 불러오는 코드를 먼저 구현해주고, 차례로 구현했습니다.
    따라서 하나의 독립적인 부분이 더 생겨,
    총 4개의 독립적인 부분에 대한 구상&구현으로 정리할 수 있을 것 같습니다.
    0) "2**N * 2**N" 2차원 배열에 대한 시계방향 회전 가중치 (dy, dx) 룩업테이블
    1) 부분 격자의 시계방향 회전
    2) 얼음 양 줄이기
    3) 답변 출력


3. 검증 (15:16 - 15:18)
    구상 단계의 3개의 독립적인 부분에 대해,
    각각 체크포인트를 찍어가며 구현했기 때문에 에러 없이 답변을 출력했습니다.

    앞으로도 이번 문제처럼,
    구상이 끝나고 나서 독립적인 작동을 하는 부분을 나눠,
    그 사이사이를 체크포인트로 설정해야겠습니다.
"""

from collections import deque

# (독립적인 수행 0)
# "2**N * 2**N" 2차원 배열에 대한 시계방향 회전 가중치 (dy, dx) 룩업테이블
# 총 (0~6) 7개담길, 룩업테이블 (좌상단(0, 0) 고정)
clockwise = []
for num in range(7):
    # tmp_arr에, 2**num * 2**num 의 2차원 배열의 각 좌표를 그대로 담음.
    tmp_arr = []
    for i in range(2**num):
        tmp_row = []
        for j in range(2**num):
            tmp_row.append((i, j))
        tmp_arr.append(tmp_row)

    # 시계방향 90도 회전해서, clockwise에 저장
    tmp_arr = [row[::-1] for row in zip(*tmp_arr)]
    clockwise.append(tmp_arr)

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or 2**n <= y or x < 0 or 2**n <= x


# (sy, sx) ~ (ey - 1, ex - 1) 영역에 대해,
# length_two가 stage와
    # 같으면 시계방향 90도 회전시키고
    # 다르면(= 보다 크면), 4개의 영역으로 분할하여 재귀함수 호출
def rotate(sy, sx, length_two):
    length = 2**length_two  # sy -> ey-1 까지의 길이
    ey, ex = sy + length, sx + length

    # length_two가 stage와 같으면, 시계방향 90도 회전 처리
    if length_two == stage:
        next_indexes = clockwise[length_two]  # 현재 length_two의, 시계방향 회전 (dy, dx) 룩업테이블 가져오기

        new_arr = []  # 회전된 값이 들어갈 임시 배열

        for y in range(length):
            new_row = []  # 회전된 값이 들어갈 임시 행
            for x in range(length):
                dy, dx = next_indexes[y][x]   # 시계방향 회전 가중치 (dy, dx)
                ny, nx = sy + dy, sx + dx     # 가중치 반영
                new_row.append(area[ny][nx])  # 시계방향 회전된 좌표의 값으로 저장.
            new_arr.append(new_row)  # 임시 행을, 임시 배열에 추가

        # 임시 배열에 저장된 값을, 실제 배열(area)에 일괄 반영
        for y in range(sy, ey):
            for x in range(sx, ex):
                area[y][x] = new_arr[y - sy][x - sx]

    else:
        rotate(sy, sx, length_two - 1)
        rotate(sy, sx + length//2, length_two - 1)
        rotate(sy + length//2, sx, length_two - 1)
        rotate(sy + length//2, sx + length//2, length_two - 1)


# 모든 좌표를 완전탐색하며, 인접 얼음이 2이하인 경우에는 -=1을 수행하는 함수
def melt_ice():
    melted = []  # -=1이 수행될 좌표들의 배열 (탐색 중에 -=1 하면, 다음에 탐색할 인접좌표에 영향 미치기에)

    for y in range(2**n):
        for x in range(2**n):
            if area[y][x]:  # 현재 칸에 얼음 있다면, 인접 얼음 수 체크
                near_ice = 0
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or not area[ny][nx]:
                        continue
                    near_ice += 1
                if near_ice < 3:  # 인접 얼음 수가 2 이하면
                    melted.append((y, x))

    # 얼음 양 -=1 처리
    for my, mx in melted:
        area[my][mx] -= 1


n, q = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2**n)]  # 각 칸의 얼음 양
stages = list(map(int, input().split()))  # 시전한 단계 L1, L2, ..., LQ

# 파이어스톰 q회 시전
for stage in stages:
    rotate(0, 0, n)  # (독립적인 수행 1) 부분 격자의 시계방향 회전
    melt_ice()       # (독립적인 수행 2) 얼음 양 줄이기


# 아래부터는 (독립적인 수행 3) 답변 출력만을 위한 코드
print(sum(map(sum, area)))  # 남아있는 얼음 총합

mx_area_cnt = 0  # 가장 큰 덩어리의 칸 개수
visited = [[0] * 2**n for _ in range(2**n)]  # BFS를 위한 방문 배열
for i in range(2**n):
    for j in range(2**n):
        if not visited[i][j] and area[i][j]:  # 미방문 & 얼음이 있다면, BFS 수행
            now_cnt = 1  # 현재 얼음 덩어리의 칸 개수
            visited[i][j] = 1

            queue = deque()
            queue.append((i, j))

            while queue:
                ci, cj = queue.popleft()
                for di, dj in direction:
                    ni, nj = ci + di, cj + dj
                    if oob(ni, nj) or visited[ni][nj] or not area[ni][nj]:
                        continue
                    visited[ni][nj] = 1
                    now_cnt += 1
                    queue.append((ni, nj))

            mx_area_cnt = max(mx_area_cnt, now_cnt)  # 얼음 덩어리 칸 개수 최대값 갱신
print(mx_area_cnt)
