# 20240806
# 04:46
# 1 / 1

from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
queue.append((0, 0))

visited = [[0] * n for _ in range(n)]

while queue:  # BFS로 탐색
    y, x = queue.popleft()  # 현재 좌표
    distance = area[y][x]  # 현재 좌표에서 이동해야 하는 거리
    for dy, dx in ((0, 1), (1, 0)):  # 우, 하에 대해서만
        ny, nx = y + dy * distance, x + dx * distance  # 다음 좌표 지정
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            visited[ny][nx] = 1
            queue.append((ny, nx))

print("HaruHaru" if visited[-1][-1] else "Hing")  # 최하단 최우측의 좌표 1 여부에 따른 출력
