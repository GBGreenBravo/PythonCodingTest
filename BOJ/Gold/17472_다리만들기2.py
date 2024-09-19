# 20240919
# 42:42
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# 현재 좌표를 기준으로, 오른쪽과 아래쪽에 설치할 수 있는 다리 있으면 bridges에 저장하는 함수
def check_possible_bridges(sy, sx):
    # 오른쪽에 가능한 다리 있는지 체크
    if not oob(sy, sx + 1) and not area[sy][sx + 1]:
        right = [(sy, sx + 1)]
        for _ in range(m):
            y, x = right[-1]
            if oob(y, x + 1):
                break
            if area[y][x + 1]:
                if len(right) > 1 and area[y][x + 1] != area[sy][sx]:  # 다리길이 2 이상 and 같은 섬 연결 X
                    bridges.append(right)
                break
            right.append((y, x + 1))

    # 아래쪽에 가능한 다리 있는지 체크
    if not oob(sy + 1, sx) and not area[sy + 1][sx]:
        below = [(sy + 1, sx)]
        for _ in range(n):
            y, x = below[-1]
            if oob(y + 1, x):
                break
            if area[y + 1][x]:
                if len(below) > 1 and area[y + 1][x] != area[sy][sx]:  # 다리길이 2 이상 and 같은 섬 연결 X
                    bridges.append(below)
                break
            below.append((y + 1, x))


# 현재 조합된 bridge_arr로 섬 모두 연결할 수 있다면, 최소값 갱신하는 함수
def check_bridge_arr():
    # 다리로 연결되는 섬들 (간선 배열)
    connected = [[] for _ in range(total_island_cnt + 1)]

    # bridge 양 끝점보다 한칸씩 더 가면 섬 번호 나오므로, 두 섬 연결하는 간선 저장
    for bridge in bridge_arr:
        y0, x0 = bridge[0]
        y1, x1 = bridge[1]
        dy, dx = y0 - y1, x0 - x1
        connected[area[y0 + dy][x0 + dx]].append(area[bridge[-1][0] - dy][bridge[-1][1] - dx])
        connected[area[bridge[-1][0] - dy][bridge[-1][1] - dx]].append(area[y0 + dy][x0 + dx])

    # 1번 섬부터 연결되는 섬 연쇄적으로 연결
    connected_visited = [0] * (total_island_cnt + 1)
    connected_visited[1] = 1
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for next_node in connected[node]:
            if connected_visited[next_node]:
                continue
            connected_visited[next_node] = 1
            queue.append(next_node)

    # 모든 섬이 연결된 게 아니라면, return
    if sum(connected_visited[1:]) != total_island_cnt:
        return

    # 모든 섬 연결 됐다면, 최소값 갱신
    global min_answer
    min_answer = min(min_answer, sum(map(len, bridge_arr)))


# 가능한 다리 조합을 찾는 DFS 조합 함수
def bridge_combination(cnt, start_idx):
    # 종료 조건
    if cnt == bridge_limit:
        check_bridge_arr()
        return

    # 조기 종료 조건1: 현재 start_idx에서 bridge_limit만큼 다리 못 만들면
    if bridge_limit - cnt > len_bridges - start_idx:
        return

    # 조기 종료 조건2: 현재 구성된 bridge_arr이 이미 min_answer보다 크면
    if sum(map(len, bridge_arr)) >= min_answer:
        return

    # DFS 재귀 호출
    for idx in range(start_idx, len_bridges):
        bridge_arr.append(bridges[idx])
        bridge_combination(cnt + 1, idx + 1)
        bridge_arr.pop()


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

# (BFS) 섬의 구분을 위해 섬 번호(1번~)로 섬 표시
island_flag = 1
island_visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if area[i][j] and not island_visited[i][j]:
            island_visited[i][j] = 1

            queue = deque()
            queue.append((i, j))

            area[i][j] = island_flag

            while queue:
                ii, jj = queue.popleft()
                for di, dj in direction:
                    ni, nj = ii + di, jj + dj
                    if oob(ni, nj) or island_visited[ni][nj] or not area[ni][nj]:
                        continue
                    island_visited[ni][nj] = 1
                    queue.append((ni, nj))
                    area[ni][nj] = island_flag

            island_flag += 1
total_island_cnt = island_flag - 1  # 전체 섬 수

# 모든 좌표 탐색하며, 오른쪽과 아래쪽으로 설치할 수 있는 다리 저장
bridges = []
for i in range(n):
    for j in range(m):
        if area[i][j]:
            check_possible_bridges(i, j)
len_bridges = len(bridges)

# (DFS) 가능한 다리 조합 모두 살펴보고, 최소값 찾기
min_answer = n * m * 2
for bridge_limit in range(1, len_bridges + 1):
    bridge_arr = []
    bridge_combination(0, 0)
print(-1 if min_answer == n * m * 2 else min_answer)
