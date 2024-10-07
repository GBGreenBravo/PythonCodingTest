# 20241007
# 11:32
# 1 / 1

h, w = map(int, input().split())
area = [[0] * w for _ in range(h)] + [[2] * w]
heights = list(map(int, input().split()))
for idx, height in enumerate(heights):
    for hh in range(h - 1, h - height - 1, -1):
        area[hh][idx] = 2

for row in range(h - 1, -1, -1):
    in_a_row = 0

    one_indexes = [idx for idx, value in enumerate(area[row]) if value == 2]
    for i in range(len(one_indexes) - 1):
        start = one_indexes[i]
        end = one_indexes[i + 1]

        for j in range(start + 1, end):
            if not area[row + 1][j]:
                break
        else:
            for j in range(start + 1, end):
                area[row][j] = 1

print(sum(map(lambda roww: roww.count(1), area)))
