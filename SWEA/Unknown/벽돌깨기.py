# 20240930
# 26:05
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or h <= y or x < 0 or w <= x


# 벽돌을 던질 column index 순열이 저장된 dfs_arr를 바탕으로
# 벽돌 던지며, 최종적으로 남는 벽돌 최소값 갱신하는 함수
def game_start():
    global min_answer

    # 이미 최소값이 0이면, return
    if not min_answer:
        return

    # dfs_arr 대로 벽돌 던질 2차원 배열 deepcopy
    copied_arr = [row[:] for row in area]

    # 구슬 던지기 수행
    for col in dfs_arr:

        # 구슬이 맞추는 벽돌 위치 찾기
        sy, sx = 0, col
        while not oob(sy, sx):
            if copied_arr[sy][sx]:
                break
            sy += 1
        else:  # 구슬이 벽돌 안 맞추면 continue
            continue

        # 구슬로 인한 연쇄폭발 (BFS)
        visited = [[0] * w for _ in range(h)]
        visited[sy][sx] = 1

        queue = deque()
        queue.append((sy, sx))

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y, x
                for _ in range(copied_arr[y][x] - 1):
                    ny, nx = ny + dy, nx + dx
                    if oob(ny, nx):
                        break
                    if visited[ny][nx]:
                        continue
                    if not copied_arr[ny][nx]:
                        continue
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

        # 폭발된 곳들 터짐(0) 처리
        for vy in range(h):
            for vx in range(w):
                if visited[vy][vx]:
                    copied_arr[vy][vx] = 0

        # 중력 작용 (시계방향 회전 -> row에 0 다 오른쪽으로 밀기 -> 반시계방향 회전)
        copied_arr = [list(crow)[::-1] for crow in zip(*copied_arr)]
        for c_idx in range(len(copied_arr)):
            new_row = [cr for cr in copied_arr[c_idx] if cr]
            copied_arr[c_idx] = new_row + [0 for _ in range(h - len(new_row))]
        copied_arr = [list(crow) for crow in list(zip(*copied_arr))[::-1]]

    min_answer = min(min_answer, w * h - sum(map(lambda crow: crow.count(0), copied_arr)))


# n개의 column 순열을 생성하는 DFS함수
def dfs(cnt):
    if cnt == n:
        game_start()
        return

    for idx in range(w):
        dfs_arr.append(idx)
        dfs(cnt + 1)
        dfs_arr.pop()


t = int(input())
for test in range(1, t + 1):
    n, w, h = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(h)]

    min_answer = w * h

    dfs_arr = []
    dfs(0)

    print(f"#{test} {min_answer}")
