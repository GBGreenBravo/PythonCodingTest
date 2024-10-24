# 20241024
# 1 / 1


def clockwise(idx):
    cube[idx] = [list(row)[::-1] for row in zip(*cube[idx])]


def counterclockwise(idx):
    cube[idx] = [list(row) for row in list(zip(*cube[idx]))[::-1]]


def rotate_cube():
    if rotating_side == 4 and rotating_direction == 1:
        clockwise(1)
        cube[5][0], cube[2][0], cube[4][0], cube[3][0] = cube[2][0], cube[4][0], cube[3][0], cube[5][0]

    elif rotating_side == 4 and rotating_direction == -1:
        counterclockwise(1)
        cube[5][0], cube[2][0], cube[4][0], cube[3][0] \
            = cube[3][0], cube[5][0], cube[2][0], cube[4][0]

    elif rotating_side == 5 and rotating_direction == 1:
        clockwise(0)
        cube[5][2], cube[2][2], cube[4][2], cube[3][2] \
            = cube[3][2], cube[5][2], cube[2][2], cube[4][2]

    elif rotating_side == 5 and rotating_direction == -1:
        counterclockwise(0)
        cube[5][2], cube[2][2], cube[4][2], cube[3][2] \
            = cube[2][2], cube[4][2], cube[3][2], cube[5][2]

    elif rotating_side == 1 and rotating_direction == 1:
        clockwise(5)
        cube[1][2][0], cube[1][2][1], cube[1][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][2][2], cube[3][1][2], cube[3][0][2] \
        = cube[3][2][2], cube[3][1][2], cube[3][0][2], \
            cube[1][2][0], cube[1][2][1], cube[1][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0]

    elif rotating_side == 1 and rotating_direction == -1:
        counterclockwise(5)
        cube[1][2][0], cube[1][2][1], cube[1][2][2], \
            cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][2][2], cube[3][1][2], cube[3][0][2] \
        = cube[2][0][0], cube[2][1][0], cube[2][2][0], \
            cube[0][0][2], cube[0][0][1], cube[0][0][0], \
            cube[3][2][2], cube[3][1][2], cube[3][0][2], \
            cube[1][2][0], cube[1][2][1], cube[1][2][2]

    elif rotating_side == 3 and rotating_direction == 1:
        clockwise(4)
        cube[1][0][2], cube[1][0][1], cube[1][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][2][2], cube[2][1][2], cube[2][0][2] \
        = cube[2][2][2], cube[2][1][2], cube[2][0][2], \
            cube[1][0][2], cube[1][0][1], cube[1][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2]

    elif rotating_side == 3 and rotating_direction == -1:
        counterclockwise(4)
        cube[1][0][2], cube[1][0][1], cube[1][0][0], \
            cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][2][2], cube[2][1][2], cube[2][0][2] \
        = cube[3][0][0], cube[3][1][0], cube[3][2][0], \
            cube[0][2][0], cube[0][2][1], cube[0][2][2], \
            cube[2][2][2], cube[2][1][2], cube[2][0][2], \
            cube[1][0][2], cube[1][0][1], cube[1][0][0]

    elif rotating_side == 0 and rotating_direction == 1:
        clockwise(3)
        cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[4][2][2], cube[4][1][2], cube[4][0][2] \
        = cube[4][2][2], cube[4][1][2], cube[4][0][2], \
            cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0]

    elif rotating_side == 0 and rotating_direction == -1:
        counterclockwise(3)
        cube[1][0][0], cube[1][1][0], cube[1][2][0], \
            cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[4][2][2], cube[4][1][2], cube[4][0][2] \
        = cube[5][0][0], cube[5][1][0], cube[5][2][0], \
            cube[0][0][0], cube[0][1][0], cube[0][2][0], \
            cube[4][2][2], cube[4][1][2], cube[4][0][2], \
            cube[1][0][0], cube[1][1][0], cube[1][2][0]

    elif rotating_side == 2 and rotating_direction == 1:
        clockwise(2)
        cube[1][2][2], cube[1][1][2], cube[1][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[5][2][2], cube[5][1][2], cube[5][0][2] \
        = cube[5][2][2], cube[5][1][2], cube[5][0][2], \
            cube[1][2][2], cube[1][1][2], cube[1][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2]

    elif rotating_side == 2 and rotating_direction == -1:
        counterclockwise(2)
        cube[1][2][2], cube[1][1][2], cube[1][0][2], \
            cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[5][2][2], cube[5][1][2], cube[5][0][2] \
        = cube[4][0][0], cube[4][1][0], cube[4][2][0], \
            cube[0][2][2], cube[0][1][2], cube[0][0][2], \
            cube[5][2][2], cube[5][1][2], cube[5][0][2], \
            cube[1][2][2], cube[1][1][2], cube[1][0][2]


S = int(input())
for scenario in range(1, S + 1):
    cube = [[[0] * 3 for _ in range(3)] for _ in range(6)]
    for i in range(3):
        cube[1][i] = list(map(str, input().split()))
    for i in range(3):
        input_list = list(map(str, input().split()))
        cube[3][i] = input_list[:3]
        cube[5][i] = input_list[3:6]
        cube[2][i] = input_list[6:9]
        cube[4][i] = input_list[9:]
    for i in range(3):
        cube[0][i] = list(map(str, input().split()))

    R = int(input())
    for _ in range(R):
        rotating_side, rotating_direction = map(int, input().split())
        rotate_cube()

    print(f"Scenario #{scenario}:")
    for i in range(3):
        print("      ", end="")
        print(*cube[1][i])
    for i in range(3):
        print(*cube[3][i] + cube[5][i] + cube[2][i] + cube[4][i])
    for i in range(3):
        print("      ", end="")
        print(*cube[0][i])
    print()
