# 20240913
# 26:35
# 1 / 1

shapes = (None,
          ((4, ), (1, 1, 1, 1)),
          ((2, 2),),
          ((2, 2, 1), (2, 3)),
          ((1, 2, 2), (3, 2)),
          ((2, 2, 2), (1, 2, 1), (2, 3), (3, 2)),
          ((2, 2, 2), (3, 3), (2, 1, 1), (1, 3)),
          ((2, 2, 2), (3, 3), (1, 1, 2), (3, 1))
          )

c, p = map(int, input().split())
input_bottoms = list(map(int, input().split()))
height = max(input_bottoms) + 4
area = [[0] * c for _ in range(height)]
for col in range(c):
    for r in range(input_bottoms[col]):
        area[-1 - r][col] = 1

case_cnt = 0

falling_shapes = shapes[p]
for falling in falling_shapes:
    for col in range(0, c - len(falling) + 1):
        now_row = 0
        while now_row < height:
            touch = 0
            for d in range(len(falling)):
                depth = falling[d]
                if now_row + depth >= height:
                    touch += 1
                elif area[now_row + depth][col + d]:
                    touch += 1
            if not touch:
                now_row += 1
                continue
            if touch == len(falling):
                case_cnt += 1
            break

print(case_cnt)
