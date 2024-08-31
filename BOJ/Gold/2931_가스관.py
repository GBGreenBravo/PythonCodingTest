# 20240831
# 27:50
# 1 / 1

from collections import deque

# 가스관 블록에 따른 가스 전파 방향 (추후 값 비교를 위해, value는 미리 오름차순 정렬)
direction_dict = {'|': [(-1, 0), (1, 0)],
                  '-': [(0, -1), (0, 1)],
                  '+': [(-1, 0), (0, -1), (0, 1), (1, 0)],
                  '1': [(0, 1), (1, 0)],
                  '2': [(-1, 0), (0, 1)],
                  '3': [(-1, 0), (0, -1)],
                  '4': [(0, -1), (1, 0)]}


# 현재 가스관 좌표로부터 연결되는 모든 가스관에 방문 처리 & 지워진 블록으로 연결되면 따로 저장
def bfs(sy, sx):
    visited[sy][sx] = 1  # 시작 좌표 방문처리

    queue = deque()
    queue.append((sy, sx))

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction_dict[area[y][x]]:  # 현재 가스관에서 갈 수 있는 방향으로
            ny, nx = y + dy, x + dx
            if visited[ny][nx]:  # 이미 방문한 가스관이라면 continue
                continue
            if area[ny][nx] == '.':  # 지워진 블록이라면, 따로 저장
                targets.append((ny, nx, dy, dx))
            elif area[ny][nx] in direction_dict.keys():  # '.', 'M', 'Z'가 아닌, 가스관 블록이라면
                visited[ny][nx] = 1
                queue.append((ny, nx))


r, c = map(int, input().split())
area = [list(str(input())) for _ in range(r)]

visited = [[0] * c for _ in range(r)]  # BFS 중복방지 체크를 위한 배열
targets = []  # 지워진 블록의 (행/열/들어온방향)이 들어갈 배열
for i in range(r):
    for j in range(c):
        if area[i][j] in ['.', 'M', 'Z']:  # 가스 전파가 필요없는 곳들은 continue (M,Z도 인접한 가스관이 있으므로 필요 없음.)
            continue
        if not visited[i][j]:  # 나머지에서는 모두 가스 전파 필요하므로 bfs() 호출
            bfs(i, j)

print(*[i + 1 for i in targets[0][:2]], end=" ")  # 지워진 블록의 행/열 출력
target_directions = sorted((-target[2], -target[3]) for target in targets)  # 지워진 블록으로 들어온 방향을 역으로 표시(지워진 블록에서 가스 나가는 방향)하여 정렬
for key, value in direction_dict.items():  # 이미 정렬돼 있는 dict.values()의 각 요소들
    if value == target_directions:  # 해당 블록이라면 출력
        print(key)
