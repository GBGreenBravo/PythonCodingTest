# 20240826
# 40:41
# 1 / 2


def oob(y, x):
    return y <= 0 or n - 1 <= y or x <= 0 or n - 1 <= x  # 처음부터 열려있는 칸들에 대해서도 영역 밖 처리.


def check_mines(sy, sx, my, mx, direction):  # (sy, sx)부터 시작해서 (my, mx) 방향으로 direction에 있는 좌표들을 살펴보며 보드를 밝혀가는 함수
    global answer_mines

    for i in range(n):
        y, x = sy + my * i, sx + mx * i  # 지정된 (my, mx) 방향으로 한칸씩 늘려감

        possibles = []  # #(아직 모름)만 넣음
        mine_decided = []  # 4(지뢰 확정)만 넣음

        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if oob(ny, nx):
                continue
            if area[ny][nx] == '#':
                possibles.append((ny, nx))
            elif area[ny][nx] == 4:
                mine_decided.append((ny, nx))

        if int(area[y][x]) == len(mine_decided):  # 주변의 #(아직 모름)에 지뢰 넣을 수 없다면
            for py, px in possibles:
                area[py][px] = 0
        elif int(area[y][x]) == len(mine_decided) + len(possibles):  # 주변의 #(아직 모름)에 지뢰 넣을 수 있다면
            for py, px in possibles:
                area[py][px] = 4
                answer_mines += 1


n = int(input())
area = [list(str(input())) for _ in range(n)]

answer_mines = (n - 4) ** 2 if n > 4 else 0  # 가려진 칸들 중 테두리 아닌 것들은 다 지뢰가 될 수 있음.

check_mines(0, 0, 0, 1, ((1, -1), (1, 0), (1, 1)))                  # (0, 0)에서 오른쪽으로
check_mines(0, n - 1, 1, 0, ((-1, -1), (0, -1), (1, -1)))           # (0, n-1)에서 아래쪽으로
check_mines(n - 1, n - 1, 0, -1, ((-1, -1), (-1, 0), (-1, 1)))      # (n-1, n-1)에서 왼쪽으로
check_mines(n - 1, 0, -1, 0, ((-1, 1), (0, 1), (1, 1)))             # (n-1, 0)에서 위쪽으로

print(answer_mines)
