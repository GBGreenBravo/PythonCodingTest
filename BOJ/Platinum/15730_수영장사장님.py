# 20241022
# 57:16
# 1 / 3

"""
주요 로직 (step 기반 BFS 활용):
    주변에 나보다 낮은 높이 없는 칸 찾으면, 물 채우기 시작.
    주변 높이들 중 최소값으로 현재 칸 변경하고,
    1) 현재 높이와 같은 곳 모두 BFS로 찾음.
    2) 찾은 칸들에 대해서 검사
        - 현재 칸이 테두리에 위치하거나 or 주변 높이 중 더 낮은 게 있다면 => possible = False
        - 위가 아니라면, next_height 최소값 갱신
    3) possible하다면,
        - 현재 높이 칸들(group_indexes) next_height로 변경
        - now_height를 next_height로 갱신
        - 1)부터 다시
"""

# BFS 기본 코드인, queue에 (ny, nx)를 넣어주지 않아서 2번 틀림.


from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or N <= yy or xx < 0 or M <= xx


def is_border(yy, xx):
    return yy < 1 or N - 1 <= yy or xx < 1 or M - 1 <= xx


N, M = map(int, input().split())
origin_area = [list(map(int, input().split())) for _ in range(N)]
area = [row[:] for row in origin_area]

for i in range(1, N - 1):
    for j in range(1, M - 1):
        near_heights = []
        for di, dj in direction:
            ni, nj = i + di, j + dj
            near_heights.append(area[ni][nj])
        if min(near_heights) < area[i][j]:
            pass
        elif min(near_heights) >= area[i][j]:
            area[i][j] = min(near_heights)

            visited = [[0] * M for _ in range(N)]
            visited[i][j] = 1

            queue = deque()
            queue.append((i, j))

            group_indexes = [(i, j)]
            possible = True
            now_height = area[i][j]

            while queue:
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or visited[ny][nx] or area[ny][nx] != now_height:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
                        group_indexes.append((ny, nx))

                next_queue = deque()
                next_height = 10_001
                for y, x in group_indexes:
                    if is_border(y, x):
                        possible = False
                        break
                    appended = False
                    for dy, dx in direction:
                        ny, nx = y + dy, x + dx
                        if area[ny][nx] != now_height:
                            next_height = min(next_height, area[ny][nx])
                            if not appended:
                                next_queue.append((y, x))
                                appended = True
                    if next_height < now_height:
                        possible = False
                        break

                if not possible:
                    break

                for gy, gx in group_indexes:
                    area[gy][gx] = next_height
                queue = next_queue
                now_height = next_height

answer = 0
for i in range(N):
    for j in range(M):
        answer += area[i][j] - origin_area[i][j]
print(answer)
