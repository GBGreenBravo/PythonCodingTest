# 20240916
# 1 / 5

r, s = map(int, input().split())
area = [list(str(input())) for _ in range(r)]

meteors = []
grounds = []
for col in range(s):
    meteor = -1
    for row in range(r):
        if area[row][col] == 'X':
            meteor = row
        elif area[row][col] == '#':
            meteors.append(meteor)
            grounds.append(row)
            break

height = min([grounds[i] - 1 - meteors[i] for i in range(s) if meteors[i] != -1])

for col in range(s):
    if meteors[col] == -1:
        continue
    origin = [area[row][col] for row in range(grounds[col])]
    for row in range(height, grounds[col]):
        area[row][col] = origin[row - height]
    for row in range(height):
        area[row][col] = '.'

for row in area:
    print(*row, sep="")
