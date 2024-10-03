# 20241003
# 27:00
# 1 / 1

# 20058_마법사상어와파이어스톰

"""
풀이 시간: 27분 (17:33 ~ 18:00)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (17:33 - 17:38)
    이전 풀이방식과 구상이 많이 달랐습니다.
    이전 풀이에서는 분할정복과 레벨별 회전 시의 (dy,dx)를 룩업테이블로 담아뒀고,
    이번 풀이는 for문을 통해 특정 레벨의 영역에서 좌상단/우상단/우하단/좌하단 슬라이싱해서 회전처리 했습니다.
    두 구상 모두 꼼꼼히 구현만 해주면 큰 이상 없는 구상이라고 생각합니다.


2. 구현 (17:38 - 17:52)
    2**(L-1) * 2**(L-1) 배열을 시계방향90도 회전으로 처음에 구현했습니다.
    체크포인트에서 이게 아님을 깨닫고,
    2**(L-1) * 2**(L-1) 배열 4개를 시계방향으로 회전시켜주는 것으로 수정했습니다.


3. 디버깅 (17:52 - 17:59)
    마지막에 출력만을 위한 BFS 코드에서 아래의 2개의 실수가 있었습니다.
    얼음이 없어도 군집으로 계산한 것, 얼음 없는 칸에서도 BFS 시작한 것
    기본 제공 테케들에서 거를 수 있는 실수들이었습니다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or 2**n <= y or x < 0 or 2**n <= x


n, q = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(2**n)]
rotation_levels = list(map(int, input().split()))

for rotation_level in rotation_levels:
    if rotation_level:
        for i in range(0, 2**n, 2**rotation_level):
            for j in range(0, 2**n, 2**rotation_level):

                top_left = [area[row][j:j + 2**(rotation_level - 1)] for row in range(i, i + 2**(rotation_level - 1))]
                top_right = [area[row][j + 2**(rotation_level - 1):j + 2**rotation_level] for row in range(i, i + 2**(rotation_level - 1))]
                bottom_right = [area[row][j + 2**(rotation_level - 1):j + 2**rotation_level] for row in range(i + 2**(rotation_level - 1), i + 2**rotation_level)]
                bottom_left = [area[row][j:j + 2**(rotation_level - 1)] for row in range(i + 2**(rotation_level - 1), i + 2**rotation_level)]

                for y in range(2**(rotation_level - 1)):
                    for x in range(2**(rotation_level - 1)):
                        area[i + y][j + x] = bottom_left[y][x]
                        area[i + y][j + 2**(rotation_level - 1) + x] = top_left[y][x]
                        area[i + 2**(rotation_level - 1) + y][j + 2**(rotation_level - 1) + x] = top_right[y][x]
                        area[i + 2**(rotation_level - 1) + y][j + x] = bottom_right[y][x]

    new_area = [row[:] for row in area]
    for i in range(2**n):
        for j in range(2**n):
            if area[i][j]:
                near_ice_cnt = 0
                for di, dj in direction:
                    ni, nj = i + di, j + dj
                    if oob(ni, nj) or not area[ni][nj]:
                        continue
                    near_ice_cnt += 1

                if near_ice_cnt < 3:
                    new_area[i][j] -= 1
    area = new_area

print(sum(map(sum, area)))

max_answer = 0
visited = [[0] * 2**n for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if not visited[i][j] and area[i][j]:
            visited[i][j] = 1

            queue = deque()
            queue.append((i, j))

            group_cnt = 1

            while queue:
                y, x = queue.popleft()
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx] or not area[ny][nx]:
                        continue
                    visited[ny][nx] = 1
                    queue.append((ny, nx))
                    group_cnt += 1

            max_answer = max(max_answer, group_cnt)
print(max_answer)
