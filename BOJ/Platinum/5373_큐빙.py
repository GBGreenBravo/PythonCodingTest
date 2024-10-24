# 20241024
# 40:21
# 1 / 1

convert_to_color = ['y', 'w', 'b', 'g', 'o', 'r']


def clockwise(idx):
    cube[idx] = [list(row)[::-1] for row in zip(*cube[idx])]


def counterclockwise(idx):
    cube[idx] = [list(row) for row in list(zip(*cube[idx]))[::-1]]


def rotate_cube():
    if info == 'U+':
        clockwise(1)
        cube[5][0], cube[2][0], cube[4][0], cube[3][0] = cube[2][0], cube[4][0], cube[3][0], cube[5][0]

    elif info == 'U-':
        counterclockwise(1)
        cube[5][0], cube[2][0], cube[4][0], cube[3][0] \
            = cube[3][0], cube[5][0], cube[2][0], cube[4][0]

    elif info == 'D+':
        clockwise(0)
        cube[5][2], cube[2][2], cube[4][2], cube[3][2] \
            = cube[3][2], cube[5][2], cube[2][2], cube[4][2]

    elif info == 'D-':
        counterclockwise(0)
        cube[5][2], cube[2][2], cube[4][2], cube[3][2] \
            = cube[2][2], cube[4][2], cube[3][2], cube[5][2]

    elif info == 'F+':
        clockwise(5)
        cube[1][2][0], cube[1][2][1], cube[1][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][2][2], cube[3][1][2], cube[3][0][2] \
        = cube[3][2][2], cube[3][1][2], cube[3][0][2], \
            cube[1][2][0], cube[1][2][1], cube[1][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0]

    elif info == 'F-':
        counterclockwise(5)
        cube[1][2][0], cube[1][2][1], cube[1][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][2][2], cube[3][1][2], cube[3][0][2] \
        = cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][2][2], cube[3][1][2], cube[3][0][2], \
            cube[1][2][0], cube[1][2][1], cube[1][2][2]

    elif info == 'B+':
        clockwise(4)
        cube[1][0][2], cube[1][0][1], cube[1][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][2][2], cube[2][1][2], cube[2][0][2] \
        = cube[2][2][2], cube[2][1][2], cube[2][0][2], \
            cube[1][0][2], cube[1][0][1], cube[1][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2]

    elif info == 'B-':
        counterclockwise(4)
        cube[1][0][2], cube[1][0][1], cube[1][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][2][2], cube[2][1][2], cube[2][0][2] \
        = cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][2][2], cube[2][1][2], cube[2][0][2], \
            cube[1][0][2], cube[1][0][1], cube[1][0][0]

    elif info == 'L+':
        clockwise(3)
        cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[4][2][2], cube[4][1][2], cube[4][0][2] \
        = cube[4][2][2], cube[4][1][2], cube[4][0][2], \
            cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0]

    elif info == 'L-':
        counterclockwise(3)
        cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[4][2][2], cube[4][1][2], cube[4][0][2] \
        = cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[4][2][2], cube[4][1][2], cube[4][0][2], \
            cube[1][0][0], cube[1][1][0], cube[1][2][0]

    elif info == 'R+':
        clockwise(2)
        cube[1][2][2], cube[1][1][2], cube[1][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[5][2][2], cube[5][1][2], cube[5][0][2] \
        = cube[5][2][2], cube[5][1][2], cube[5][0][2], \
            cube[1][2][2], cube[1][1][2], cube[1][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2]

    elif info == 'R-':
        counterclockwise(2)
        cube[1][2][2], cube[1][1][2], cube[1][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[5][2][2], cube[5][1][2], cube[5][0][2] \
        = cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[5][2][2], cube[5][1][2], cube[5][0][2], \
            cube[1][2][2], cube[1][1][2], cube[1][0][2]


T = int(input())
for _ in range(T):

    N = int(input())
    information = list(map(str, input().split(" ")))

    cube = []  # 0/1/2/3/4/5 -> bottom/top/right/left/top/bottom
    for i in range(6):
        cube.append([[i] * 3 for _ in range(3)])

    for info in information:
        rotate_cube()

    for row in cube[1]:
        print(*[convert_to_color[num] for num in row], sep="")
