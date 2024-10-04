# 202401003
# 15:12
# 1 / 1

# 21610_마법사상어와비바라기

"""
풀이 시간: 15분 (21:32 ~ 21:47)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (21:32 - 21:37)
    이 문제를 처음 접했을 때, %연산자를 활용하지 않고 행/열 이어짐을 구현했었습니다.
    그것보다 %연산자를 활용하는 것이 훨씬 간단하고 좋음을 알기에, 어려움 없이 풀이 방식을 떠올렸습니다.


2. 구현 (21:37 - 21:46)
    시간복잡도 이슈가 없음을 확인하고 그대로 구현했습니다.


3. 디버깅 (-)
"""

direction_8 = (None, (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1))
direction_4 = ((-1, 1), (-1, -1), (1, -1), (1, 1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
moves = [tuple(map(int, input().split())) for _ in range(m)]

specials = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]
for move_d_idx, move_distance in moves:
    di, dj = direction_8[move_d_idx]
    specials = [((sp[0] + di * move_distance) % n, (sp[1] + dj * move_distance) % n) for sp in specials]

    for si, sj in specials:
        area[si][sj] += 1
    for si, sj in specials:
        for ddi, ddj in direction_4:
            ni, nj = si + ddi, sj + ddj
            if oob(ni, nj) or not area[ni][nj]:
                continue
            area[si][sj] += 1

    specials = set(specials)
    next_specials = []
    for i in range(n):
        for j in range(n):
            if area[i][j] >= 2 and (i, j) not in specials:
                area[i][j] -= 2
                next_specials.append((i, j))
    specials = next_specials

print(sum(map(sum, area)))
