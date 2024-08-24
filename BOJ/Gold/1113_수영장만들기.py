# 20240824
# 29:34
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def check_and_fill_water(sy, sx, h):  # 현재 높이와 같은 좌표들을 탐색하며, 물을 더 채울 수 있다면 채우는 함수
    same_heights = [(sy, sx)]  # (물 보충을 위해) 현재 높이와 같은 좌표들을 저장할 배열

    queue = deque([(sy, sx)])
    visited_at_this_height[sy][sx] = 1

    border_mn_value = 9  # 수영장 테두리의 가장 낮은 높이까지 물 채울 수 있기에, 9로 초기화
    can_fill_water = True  # 현재 좌표의 수영장에 물 채울 수 있는지 체크하는 flag

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or area[ny][nx] < h:  # 영역 밖이거나 or 주변이 더 낮다면, 물을 채울 수 없음
                can_fill_water = False
                continue  # 그래도 (현재 높이와 같은) 인접한 영역의 좌표가, 이 함수를 중복 호출하지 않도록, visited 처리는 끝까지 해줘야 함.
            if area[ny][nx] > h:  # 현재 높이보다 높다면, 수영장 테두리 이므로
                border_mn_value = min(border_mn_value, area[ny][nx])  # 수영장 테두리 최소값 갱신
                continue
            if visited_at_this_height[ny][nx]:
                continue
            same_heights.append((ny, nx))
            visited_at_this_height[ny][nx] = 1
            queue.append((ny, nx))

    if not can_fill_water:  # 영역 밖이거나 or 주변이 더 낮아서, 물을 채울 수 없다면 return
        return

    for y, x in same_heights:  # 수영장 물 높이 상승
        area[y][x] = border_mn_value

    global answer
    answer += (border_mn_value - h) * len(same_heights)  # 물 추가량 => (물 높이 상승치 * 수영장 내 좌표 수)


n, m = map(int, input().split())
area = [[int(i) for i in list(str(input()))] for _ in range(n)]

answer = 0

for height in range(1, 9):  # 1부터 8까지의 높이에 대해 (9가 상한선이므로)
    visited_at_this_height = [[0] * m for _ in range(n)]  # 현재 높이와 같은 높이를 가진 좌표들 중복 탐색 방지를 위한, 방문 배열

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if area[i][j] == height and not visited_at_this_height[i][j]:
                check_and_fill_water(i, j, height)

print(answer)
