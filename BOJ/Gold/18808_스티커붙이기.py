# 20240806
# 34:00
# 1 / 1

n, m, k = map(int, input().split())
area = [[0] * m for _ in range(n)]
stickers = []
for _ in range(k):  # 스티커를 0 1 로 이루어진 2차원리스트; 입력 그대로 저장함.
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < m)


def check_and_attach(sticker_shape, y, x):  # 현재 스티커의 모양과 우측상단에 맞댈 좌표를 받아, 스티커를 대보고 붙일 수 있다면 붙이는 함수
    height, width = len(sticker_shape), len(sticker_shape[0])  # 스티커의 높이와 너비
    sticker_locations = [[None] * width for _ in range(height)]  # 스티커를 붙일 좌표를 저장하는 리스트
    for h in range(height):
        for w in range(width):
            if sticker_shape[h][w] == 0:  # 스티커 붙이는 곳이 아니라면 False 저장
                sticker_locations[h][w] = False
            else:  # 스티커 붙이는 곳이라면, 적절한 좌표 저장
                sticker_locations[h][w] = (y + h, x + w)

    sticker_attach_lst = []
    for row in sticker_locations:  # 스티커 붙일 곳에 대해
        for nex in row:
            if not nex:  # 스티커 붙이는 곳이 아니라면 continue
                continue
            ny, nx = nex
            if oob(ny, nx) or area[ny][nx] == 1:  # 스티커가 영역 밖이거나, 이미 스티커 붙여져 있다면, return False
                return False
            sticker_attach_lst.append((ny, nx))

    for ny, nx in sticker_attach_lst:  # 스티커 붙일 수 있는 곳에 스티커 붙이기
        area[ny][nx] = 1
    return True


def rotate(sticker_shape):  # 스티커를 시계방향 90도로 돌려서 반환하는 함수
    return [list(col)[::-1] for col in zip(*sticker_shape)]


for sticker in stickers:  # 스티커 1개씩 탐색
    rotate_cnt = 0
    while rotate_cnt < 4:  # 돌린 횟수가 4번이 되면 종료; 스티커 버려야 함.
        attachable = False  # 스티커 붙이기가 가능한지 체크하는 flag

        for i in range(n):
            for j in range(m):
                check = check_and_attach(sticker, i, j)  # 현재 좌표가 상단우측인 경우에, 스티커 갖다 대보기
                if check:
                    attachable = True  # 붙여졌다면 flag -> True
                    break
            if attachable:
                break

        if attachable:  # 스티커 붙였다면 다음 스티커로
            break
        else:  # 스티커 못 붙였으면, 스티커 회전시키고 다음 while문
            sticker = rotate(sticker)
            rotate_cnt += 1

print(sum(map(sum, area)))
