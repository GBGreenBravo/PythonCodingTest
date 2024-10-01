# 20240930
# 17:02
# 1 / 1

# 16235_나무재테크

"""
풀이 시간: 17분 (17:06 - 17:23)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (17:06 - 17:11)


2. 구현 (17:11 - 17:21)


3. 디버깅 (-)
"""

direction = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


n, m, k = map(int, input().split())
area = [[5] * n for _ in range(n)]
regular_added = [list(map(int, input().split())) for _ in range(n)]
viruses = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    rr, cc, oo = map(int, input().split())
    viruses[rr - 1][cc - 1].append(oo)

for _ in range(k):
    for i in range(n):
        for j in range(n):
            now_viruses = viruses[i][j]
            if not now_viruses:
                continue

            now_viruses.sort()
            area_value = area[i][j]
            alive = []
            added_from_death = 0
            for virus in now_viruses:
                if area_value < virus:
                    added_from_death += virus // 2
                else:
                    area_value -= virus
                    alive.append(virus + 1)
            viruses[i][j] = alive
            area[i][j] = area_value + added_from_death

    for i in range(n):
        for j in range(n):
            for virus in viruses[i][j]:
                if virus == 1:
                    break
                if not virus % 5:
                    for di, dj in direction:
                        ni, nj = i + di, j + dj
                        if not oob(ni, nj):
                            viruses[ni][nj].append(1)

    for i in range(n):
        for j in range(n):
            area[i][j] += regular_added[i][j]

print(sum([len(viruses[row][col]) for row in range(n) for col in range(n)]))
