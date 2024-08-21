# 20240821
# 31:30
# 1 / 1

"""
문제의 예시 타일을 아래와 같은 2차원 리스트로 저장
[[1, 4, 4, 5, 3, 4, 5, 4, 5, 2],
 [0, 4, 2, 5, 6, 4, 4, 6, 5, 0],
 [2, 4, 5, 1, 6, 1, 1, 6, 2, 3],
 [0, 4, 2, 5, 3, 1, 2, 5, 5, 0],
 [4, 1, 2, 2, 4, 3, 2, 3, 3, 4]]

0이 아닌 값이 있는 좌표는, 무조건 짝꿍 좌표를 가지고, 짝꿍 좌표와 같은 칸 번호를 갖게 된다.
"""

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or 2 * n <= xx


def cal_pair_yx(yy, xx):  # 좌표값을 받아, "짝꿍 좌표"와 "해당 좌표들이 적힌 칸의 번호"를 반환하는 함수
    if yy % 2 == 0:  # 짝수 행이라면, (yy // 2) * (2 * n - 1) 만큼 이전 행들에서 번호 소모됨.
        if xx % 2 == 0:
            return yy, xx + 1, (yy // 2) * (2 * n - 1) + (xx // 2) + 1  # (왼쪽 좌표의 x값 // 2) + 1 추가로 더해주기
        else:
            return yy, xx - 1, (yy // 2) * (2 * n - 1) + ((xx - 1) // 2) + 1
    else:  # 홀수 행이라면, n + ((yy - 1) // 2) * (2 * n - 1) 만큼 이전 행들에서 번호 소모됨.
        if xx % 2 == 1:
            return yy, xx + 1, n + ((yy - 1) // 2) * (2 * n - 1) + ((xx - 1) // 2) + 1
        else:
            return yy, xx - 1, n + ((yy - 1) // 2) * (2 * n - 1) + ((xx - 2) // 2) + 1


def bfs():
    queue = deque()
    queue.append((0, 0, [1]))  # 첫 번째 타일 왼쪽 좌표 시작
    queue.append((0, 1, [1]))  # 첫 번째 타일 오른쪽 좌표 시작

    mx_num = 0
    mx_arr = [1]  # n이 1인 경우 아래 while문 바로 빠져나오기에 1 반환해야 함.

    while queue:
        y, x, route = queue.popleft()  # 현재 좌표 y x, 현재 좌표가 있는 칸의 번호

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx) or visited[ny][nx] or area[ny][nx] == 0 or area[y][x] != area[ny][nx]:  # 영역 밖 / 이미 방문 / 홀수 행 맨앞이나 맨뒤 / 숫자가 달라 이동 불가능
                continue
            py, px, p_num = cal_pair_yx(ny, nx)  # 도달할 수 있는 좌표에는 무조건 짝꿍인 좌표가 있으므로, 그 좌표와 타일 번호를 가져옴

            if p_num == target_num:  # 마지막 번호의 타일에 도달했다면, 해당 루트 반환
                return route + [p_num]

            visited[ny][nx] = 1  # 도달한 좌표 방문처리
            queue.append((ny, nx, route + [p_num]))

            visited[py][px] = 1  # 도달한 짝꿍 좌표 방문처리
            queue.append((py, px, route + [p_num]))

            if p_num > mx_num:  # 현재 방문한 타일 번호가 최대값보다 크다면
                mx_num = p_num
                mx_arr = route + [p_num]  # 최대값으로 가는 루트 갱신

    return mx_arr  # 마지막 타일에 도착하지 않았다면, 가장 큰 번호에 도달한 루트 반환


n = int(input())
area = [[0] * (2 * n) for _ in range(n)]  # row는 n이고 column은 2 * n인 배열 세팅

for i in range(n):  # i행에 대해
    j = 0 if i % 2 == 0 else 1  # i가 짝수면 0부터 시작, i가 홀수면 1부터 시작
    while j + 1 < 2 * n:  # j + 1이 2 * n 미만일 동안
        a, b = map(int, input().split())  # 타일 저장
        area[i][j] = a
        area[i][j + 1] = b
        j += 2

visited = [[0] * (2 * n) for _ in range(n)]  # BFS를 위한 방문 배열
visited[0][0] = 1  # 첫 번째 타일 방문처리
visited[0][1] = 1  # 첫 번째 타일 방문처리

target_num = cal_pair_yx(n, 2 * n - 2)[2]  # 마지막 타일의 번호

answer_arr = bfs()

print(len(answer_arr))
print(*answer_arr)
