# 20241025
# 27:41
# 1 / 3

"""
주요 로직
    ⇄ 이런 식으로 배열 따로 탐색 후, x 만나면 각각 정사각형 영역 찾기.
    찾은 정사각형 2개로 모두 안 가려지면,
    ⇅ 이런 식으로 배열 따로 탐색 후, x 만나면 각각 정사각형 영역 찾기.

틀렸던 부분
    5 5
    .....
    xxxx.
    xxxxx
    xxxxx
    xxxx.

    위와 같은 코드를 초기에 생각 못해서 1번 틀리고,
    ⇄ 이런 식으로 탐색 후, 안 되면 ⇅ 이렇게 탐색해야 했는데, ⇆ 이렇게 탐색해서 또 1번 틀림.
"""


def oob(yy, xx):
    return yy < 0 or R <= yy or xx < 0 or C <= xx


R, C = map(int, input().split())
area = [[int(inp == 'x') for inp in str(input())] for _ in range(R)]

first = None
for i in range(R):
    for j in range(C):
        if area[i][j]:
            length = 1
            while True:
                if oob(i, j + length) or oob(i + length, j):
                    break
                if not area[i][j + length] or not area[i + length][j]:
                    break
                length += 1
            first = i + 1, j + 1, length
            break
    else:
        continue
    break

second = None
for i in range(R - 1, -1, -1):
    for j in range(C - 1, -1, -1):
        if area[i][j]:
            length = 1
            while True:
                if oob(i, j - length) or oob(i - length, j):
                    break
                if not area[i][j - length] or not area[i - length][j]:
                    break
                length += 1
            second = i - length + 2, j - length + 2, length
            break
    else:
        continue
    break

copied_area = [row[:] for row in area]
for i in range(first[2]):
    for j in range(first[2]):
        copied_area[first[0]-1 + i][first[1]-1 + j] = 0
for i in range(second[2]):
    for j in range(second[2]):
        copied_area[second[0]-1 + i][second[1]-1 + j] = 0
if not sum(map(sum, copied_area)):
    print(*first)
    print(*second)
else:
    first = None
    for j in range(C - 1, -1, -1):
        for i in range(R):
            if area[i][j]:
                length = 1
                while True:
                    if oob(i, j - length) or oob(i + length, j):
                        break
                    if not area[i][j - length] or not area[i + length][j]:
                        break
                    length += 1
                first = i + 1, j - length + 2, length
                break
        else:
            continue
        break

    second = None
    for j in range(C):
        for i in range(R - 1, -1, -1):
            if area[i][j]:
                length = 1
                while True:
                    if oob(i, j + length) or oob(i - length, j):
                        break
                    if not area[i][j + length] or not area[i - length][j]:
                        break
                    length += 1
                second = i - length + 2, j + 1, length
                break
        else:
            continue
        break
    print(*first)
    print(*second)
