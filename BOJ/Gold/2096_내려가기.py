# 20241014
# 08:10
# 1 / 2

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

max_area = area[0][:]
min_area = area[0][:]

for i in range(1, n):
    new_max_area, new_min_area = [0] * 3, [0] * 3
    new_max_area[0] = area[i][0] + max(max_area[0], max_area[1])
    new_max_area[1] = area[i][1] + max(max_area)
    new_max_area[2] = area[i][2] + max(max_area[1], max_area[2])

    new_min_area[0] = area[i][0] + min(min_area[0], min_area[1])
    new_min_area[1] = area[i][1] + min(min_area)
    new_min_area[2] = area[i][2] + min(min_area[1], min_area[2])
    max_area, min_area = new_max_area, new_min_area

print(max(max_area), min(min_area))
