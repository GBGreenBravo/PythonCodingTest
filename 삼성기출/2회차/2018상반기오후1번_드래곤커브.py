# 20240930
# 13:54
# 1 / 1

# 15685_드래곤커브

"""
풀이 시간: 14분 (15:58 - 16:12)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:58 - 16:02)
    코드 리셋에 대한 첫 고찰을 했던 문제였기에, 실수 포인트와 풀이가 기억에 많이 남은 편이었습니다.


2. 구현 (16:02 - 16:10)
    이전 풀이와 동일하게, 좌표기준 회전으로 문제를 풀었습니다.


3. 디버깅 (16:10 - 16:11)
"""

direction = ((0, 1), (-1, 0), (0, -1), (1, 0))


def rotate(cy, cx, remain_cnt, indexes_arr):
    if not remain_cnt:
        for iy, ix in indexes_arr:
            area[iy][ix] = 1
        return

    new_indexes_arr = []
    for iy, ix in indexes_arr:
        dy, dx = iy - cy, ix - cx
        ny, nx = cy + dx, cx - dy
        new_indexes_arr.append((iy, ix))
        new_indexes_arr.append((ny, nx))

    dsy, dsx = sy - cy, sx - cx
    ncy, ncx = cy + dsx, cx - dsy
    rotate(ncy, ncx, remain_cnt - 1, new_indexes_arr)


area = [[0] * 101 for _ in range(101)]
n = int(input())
for _ in range(n):
    sy, sx, sd, gen = map(int, input().split())
    ey, ex = sy + direction[sd][0],  sx + direction[sd][1]
    rotate(ey, ex, gen, [(sy, sx), (ey, ex)])

answer = 0
for i in range(100):
    for j in range(100):
        if area[i][j] and area[i][j + 1] and area[i + 1][j] and area[i + 1][j + 1]:
            answer += 1
print(answer)
