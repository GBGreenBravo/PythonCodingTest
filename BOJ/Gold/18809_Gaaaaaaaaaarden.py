# 20240813
# 43:09
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 상하좌우


def oob(y, x):
    return (y < 0) or (n <= y) or (x < 0) or (m <= x)


def spread(red_arr):  # 유효한 위치와 개수의 red_arr, green_arr에 대해, spread를 진행하고 피운 꽃의 최대값을 갱신하는 BFS 함수
    green_arr = [i for i in now_spread_arr if i not in red_arr]  # red_arr로 인해 정해지는, green_arr

    queue = deque()
    visited = [[[False] * m for _ in range(n)] for _ in range(2)]  # 0: green / 1: red

    for gy, gx in green_arr:
        queue.append((gy, gx, 0))  # 0: green / 1: red
        visited[0][gy][gx] = 1  # 배양액 시작 좌표의 거리 (False 피하기 위해 1부터 시작)
    for ry, rx in red_arr:
        queue.append((ry, rx, 1))
        visited[1][ry][rx] = 1

    flowers = set()  # 꽃이 핀다면, 그 꽃이 핀 좌표를 저장하는 set (중복 저장되어 카운트에 오류 피하고자, list 말고 set 활용)

    while queue:  # BFS기에, distance 오름차순에 위배되지 않음. -> 꽃 피우는 경우 한 queue 내에서
        y, x, color = queue.popleft()  # 현재 좌표 y, x, 색(0: green, 1: red)
        different_color = (color + 1) % 2  # 다른 색 (0 -> 1, 1 -> 0)
        distance = visited[color][y][x] + 1  # 시작된 배양액 좌표로부터의 거리 + 1

        if (y, x) in flowers:  # 현재 좌표에 꽃이 피었다면, 배양액 못 퍼지므로 continue
            continue

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or garden[ny][nx] == 0:  # 영역 밖이거나 호수라면, continue
                continue
            if visited[different_color][ny][nx] and visited[different_color][ny][nx] == distance:  # 다른 색으로 방문했고, 그 거리가 distance와 같다면
                flowers.add((ny, nx))  # 같은 distance에 도착했다는 뜻이므로, 꽃 피우기 (다른 방향에서도 여러 색 동시에 도달할 수 있으므로 set 활용)
                visited[color][ny][nx] = distance
                continue
            if not visited[0][ny][nx] and not visited[1][ny][nx]:  # 어떠한 색의 배양액으로도 아직 닿지 않았다면, 방문 처리 및 queue 삽입
                visited[color][ny][nx] = distance
                queue.append((ny, nx, color))

    global answer_mx
    answer_mx = max(answer_mx, len(flowers))  # 피운 꽃 최대값 갱신


def how_to_spread(red_arr, start):  # (green + red)개의 조합에 대해 red_arr을 red개 만큼 선택하여, spread()를 호출하는 DFS 함수
    if len(red_arr) == red:  # red_arr이 red개 만큼 조합되면, spread() 호출
        spread(red_arr)
        return

    if start == len(now_spread_arr):  # 영역 밖이면 종료
        return

    if red - len(red_arr) > len(now_spread_arr) - start:  # 남은 땅이 필요한 red보다 더 적다면, 조기 종료
        return

    for i in range(start, len(now_spread_arr)):
        how_to_spread(red_arr + [now_spread_arr[i]], i + 1)


def where_to_spread(cnt, start):  # 배양액을 뿌릴 수 있는 곳에서 (green + red)개 만큼의 조합을 구하여, how_to_spread()를 호출하는 DFS 함수
    if cnt == green + red:  # 개수 충족되면 how_to_spread() 호출
        how_to_spread([], 0)
        return

    if start == len(can_spread_grounds):  # 영역 밖이면 종료
        return

    if red + green - cnt > len(can_spread_grounds) - start:  # 남은 땅이 더 필요한 땅 개수보다 더 적다면, 조기 종료
        return

    for i in range(start, len(can_spread_grounds)):
        now_spread_arr.append(can_spread_grounds[i])
        where_to_spread(cnt + 1, i + 1)
        now_spread_arr.pop()


n, m, green, red = map(int, input().split())
garden = [list(map(int, input().split())) for _ in range(n)]

can_spread_grounds = []
for i in range(n):
    for j in range(m):
        if garden[i][j] == 2:  # 배양액 뿌릴 수 있는 곳이라면
            can_spread_grounds.append((i, j))  # 배양액 가능 좌표 따로 배열에 저장
            garden[i][j] = 1

now_spread_arr = []
answer_mx = 0
where_to_spread(0, 0)  # 배양액 가능 좌표 중 어디에 배양액 뿌릴지 호출

print(answer_mx)  # 피운 꽃 최대값 출력
