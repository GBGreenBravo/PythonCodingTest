# 20240927
# 13:37
# 1 / 1

# 14503_로봇청소기

"""
풀이 시간: 15분 (17:07 - 17:22)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (17:07 - 17:11)
    (09/27 한정) 정독&메모 하지 않았습니다..
    문제 정독&메모 루틴의 소중함을 깨달은 하루였습니다.

    문제의 조건에 따른 수행을 (매우) 간단하게 메모했습니다.

2. 구현 (17:11 - 17:18)
    이전의 코드와 비교하면, 로직은 동일하나 코드가 좀 더 간결해졌습니다.


3. 디버깅 (17:18 - 17:20)
    문제를 정확히 읽지 않아, 후진 시 방문했던 칸이어도 후진 못 하도록 구현했던 것을,
    문제를 다시 읽고 바로잡았습니다.
"""

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서

n, m = map(int, input().split())
y, x, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[y][x] = 1

while True:
    for _ in range(4):
        d = (d - 1) % 4
        dy, dx = direction[d]
        ny, nx = y + dy, x + dx
        if area[ny][nx] or visited[ny][nx]:
            continue
        visited[ny][nx] = 1
        y, x = ny, nx
        break
    else:
        bdy, bdx = direction[d - 2]
        bny, bnx = y + bdy, x + bdx
        if area[bny][bnx]:
            break
        visited[bny][bnx] = 1
        y, x = bny, bnx

print(sum(map(sum, visited)))
