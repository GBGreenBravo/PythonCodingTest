# 20241003
# 25:55
# 1 / 1

# 19238_스타트택시

"""
풀이 시간: 26분 (15:02 ~ 15:28)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:02 - 15:07)
    이전에 풀 때는, 다른 분들이 간과했던 "도착지 겹치는 경우"를 저도 간과했었지만 운 좋게 넘어갔다고 생각해서,
    입력 조건도 꼼꼼히 확인하고 입력값의 저장 형식을 결정했습니다.


2. 구현 (15:07 - 15:27)
    이전 풀이와 구조는 살짝 다르나, step기반 BFS를 활용한 것과 전체적인 구상은 동일합니다.


3. 디버깅 (15:27 - 15:28)
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def find_next_startpoint():
    global battery, car_y, car_x

    if passenger_startpoints[car_y][car_x]:
        passenger_idx = passenger_startpoints[car_y][car_x]
        passenger_startpoints[car_y][car_x] = 0
        return passenger_idx

    visited = [[0] * n for _ in range(n)]
    visited[car_y][car_x] = 1

    queue = deque()
    queue.append((car_y, car_x))

    distance = 0
    while queue:
        distance += 1
        next_queue = deque()
        found_passengers = []

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:
                    continue
                if passenger_startpoints[ny][nx]:
                    found_passengers.append((ny, nx))
                    continue
                visited[ny][nx] = 1
                next_queue.append((ny, nx))

        if found_passengers:
            nsy, nsx = min(found_passengers)
            passenger_idx = passenger_startpoints[nsy][nsx]
            passenger_startpoints[nsy][nsx] = 0
            battery -= distance
            if battery <= 0:
                return False
            car_y, car_x = nsy, nsx
            return passenger_idx

        queue = next_queue

    return False


def move_passenger_to_endpoint(p_idx):
    global battery, car_y, car_x

    ey, ex = passenger_endpoints[p_idx]

    visited = [[0] * n for _ in range(n)]
    visited[car_y][car_x] = 1

    queue = deque()
    queue.append((car_y, car_x))

    distance = 0
    while queue:
        distance += 1
        next_queue = deque()

        while queue:
            y, x = queue.popleft()
            for dy, dx in direction:
                ny, nx = y + dy, x + dx
                if oob(ny, nx) or visited[ny][nx] or area[ny][nx]:
                    continue
                if ny == ey and nx == ex:
                    battery -= distance
                    if battery < 0:
                        return False
                    battery += distance * 2
                    car_y, car_x = ny, nx
                    return True
                visited[ny][nx] = 1
                next_queue.append((ny, nx))

        queue = next_queue

    return False


n, m, battery = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

car_y, car_x = map(lambda inp: int(inp) - 1, input().split())

passenger_startpoints = [[0] * n for _ in range(n)]
passenger_endpoints = [None]
for i in range(1, m + 1):
    aa, bb, cc, dd = map(lambda inp: int(inp) - 1, input().split())
    passenger_startpoints[aa][bb] = i
    passenger_endpoints.append((cc, dd))

for _ in range(m):
    onboarding_passenger_idx = find_next_startpoint()
    if not onboarding_passenger_idx:
        print(-1)
        break

    if not move_passenger_to_endpoint(onboarding_passenger_idx):
        print(-1)
        break
else:
    print(battery)
