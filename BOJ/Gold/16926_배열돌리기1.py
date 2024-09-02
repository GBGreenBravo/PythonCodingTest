# 20240903
# 17:38
# 1 / 1

n, m, r = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

indexes = []  # 겉에서부터 돌릴 라인 좌표들을 저장할 배열
for i in range(min(n // 2, m // 2)):  # 한 라인을 좌측상단부터 시계방향으로 저장
    tmp = []
    for j in range(i, m - i):
        tmp.append((i, j))
    for j in range(i + 1, n - 1 - i):
        tmp.append((j, m - i - 1))
    for j in range(m - 1 - i, i - 1, -1):
        tmp.append((n - 1 - i, j))
    for j in range(n - 2 - i, i, -1):
        tmp.append((j, i))
    indexes.append(tmp)

new_arr = [[0] * m for _ in range(n)]  # 돌린 결과가 저장될 배열
for index_arr in indexes:
    d = r % len(index_arr)  # 현재 라인 길이를 넘어서 돌리는 경우, % 연산으로 줄이기
    for i in range(len(index_arr)):
        y, x = index_arr[i]
        dy, dx = index_arr[(i + d) % len(index_arr)]  # d 만큼 돌렸을 때의 좌표
        new_arr[y][x] = area[dy][dx]

for row in new_arr:
    print(*row)
