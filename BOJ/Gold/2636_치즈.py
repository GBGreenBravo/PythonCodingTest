# 20240920
# 14:28
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# (BFS) 새로운 N*M 배열 만들어서, 공기인 칸은 1로 바꾸고 반환
# (비효율적이지만 코드가 간단해짐)
def fill_air():
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0, 0))

    while queue:
        y, x = queue.popleft()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or cheese[ny][nx]:
                continue
            visited[ny][nx] = 1
            queue.append((ny, nx))

    return visited


# 공기와 맞닿는 치즈 녹이는 함수
def melt_cheese():
    # 녹이기의 동시성 보존을 위한 배열
    melting_indexes = []

    for y in range(n):
        for x in range(m):
            # 치즈가 있다면
            if cheese[y][x]:
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or not air[ny][nx]:
                        continue
                    # 인접칸에 공기가 있다면
                    melting_indexes.append((y, x))
                    break

    # 녹일 치즈 동시에 녹이기
    for my, mx in melting_indexes:
        cheese[my][mx] = 0

    # 녹인 치즈 수 반환
    return len(melting_indexes)


n, m = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(n)]

air = fill_air()  # 공기 표시

time = 0
while cheese_cnt := sum(map(sum, cheese)):  # 현재 치즈 개수 (이 조건으로 끝나는 경우 없음) (그냥 := 연산자 써보고 싶어서)
    time += 1
    if melt_cheese() == cheese_cnt:  # 녹인 치즈 수 == 기존 치즈 개수 -> break
        break
    air = fill_air()  # 공기 표시

print(time)        # 다 녹는 데 걸린 시간 출력
print(cheese_cnt)  # 다 녹기 1시간 전 치즈 개수 출력
