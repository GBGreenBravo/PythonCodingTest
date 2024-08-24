# 20240824
# 06:38
# 1 / 1

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n = int(input())
area = [[int(i) for i in list(str(input()))] for _ in range(n)]

home_counts = []  # 단지별 집 수들을 저장할 배열

for i in range(n):
    for j in range(n):
        if area[i][j]:  # 집(1)이라면
            home_count = 1

            queue = deque([(i, j)])
            area[i][j] ^= 1  # 중복 방지를 위해 0으로
            while queue:
                y, x = queue.popleft()
                for dy, dx in direction:
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or not area[ny][nx]:  # 영역 밖 or 집 없다면, continue
                        continue
                    area[ny][nx] ^= 1  # 중복 방지를 위해 0으로
                    queue.append((ny, nx))
                    home_count += 1

            home_counts.append(home_count)  # 처음 집과 연결된 모든 집의 수를 저장

home_counts.sort()  # 출력 조건을 위한 오름차순 정렬
print(len(home_counts))
for home_count in home_counts:
    print(home_count)
