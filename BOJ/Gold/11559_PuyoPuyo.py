# 20240806
# 29:21
# 1 / 1

from collections import deque

field = [list(str(input())) for _ in range(12)]

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return not(0 <= y < 12) or not(0 <= x < 6)


in_a_row = 0  # 정답으로 출력할 연쇄 횟수
while True:
    explosion_happened = False  # 뿌요 터지는지 확인할 flag

    for i in range(12):
        for j in range(6):
            if field[i][j] != '.':  # 뿌요를 만난다면 BFS
                queue = deque()
                queue.append((i, j))
                visited = [[0] * 6 for _ in range(12)]
                visited[i][j] = 1
                color = field[i][j]  # 기준 색

                while queue:
                    cy, cx = queue.popleft()
                    for dy, dx in direction:
                        ny, nx = cy + dy, cx + dx
                        if oob(ny, nx) or visited[ny][nx] or field[ny][nx] != color:
                            continue
                        visited[ny][nx] = 1
                        queue.append((ny, nx))

                if sum(map(sum, visited)) >= 4:  # visited의 총합, 즉 현재 좌표에서 연결돼 있는 같은 색의 뿌요 수가 4 넘으면
                    explosion_happened = True  # 연쇄 flag -> True
                    for ey in range(12):
                        for ex in range(6):
                            if visited[ey][ex] == 1:  # 폭발하는 좌표에서 뿌요 제거
                                field[ey][ex] = '.'

    if not explosion_happened:  # 연쇄 일어나지 않는다면 break
        break
    else:  # 연쇄가 일어난다면
        in_a_row += 1  # 연쇄 횟수 += 1

        field = [list(col) for col in zip(*field)]  # 행 <-> 열
        for i in range(6):
            while '.' in field[i]:  # 빈공간'.' 모두
                field[i].remove('.')
            field[i] = ['.'] * (12 - len(field[i])) + field[i]  # 상단에 빈공간'.' 채우기
        field = [list(row) for row in zip(*field)]  # 열 <-> 행

print(in_a_row)
