# 20241021
# 44:30
# 1 / 1


"""
행이나 열 길이 중 하나라도, 홀수가 있다면, 모두 탐색 가능.
둘 다 짝수라면, 하나는 포기해야 함. (0, 0)과 (R - 1, C - 1)이 아닌 것 중, 최소값 하나만 빼자.

둘다 짝수인 경우(else문) =>
    행idx+열idx 가 홀수면, 그 좌표 하나만 빼고 다 탐색 가능.
    행idx+열idx 가 짝수인 경우...? => 얘네가 최소좌표가 되더라도 다른 (행idx+열idx==홀수) 좌표가 무조건 포함 안되는 루트로만 작성됨.
    => 행idx+열idx 가 홀수인 곳에서만 최소값 찾으면 됨.

    => 행idx가 짝/홀인 경우만, 탐색 경로 법칙 달리 적용해주면 됨.
"""


def find_min_index():
    min_value = 1000
    min_y, min_x = None, None
    for y in range(R):
        for x in range(C):
            if (y + x) % 2 == 0:
                continue
            if area[y][x] < min_value:
                min_value = area[y][x]
                min_y, min_x = y, x
    return min_y, min_x


R, C = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(R)]

if R % 2:
    for _ in range((R - 1) // 2):
        print("R" * (C - 1), end="")
        print("D", end="")
        print("L" * (C - 1), end="")
        print("D", end="")
    print("R" * (C - 1), end="")

elif C % 2:
    for _ in range((C - 1) // 2):
        print("D" * (R - 1), end="")
        print("R", end="")
        print("U" * (R - 1), end="")
        print("R", end="")
    print("D" * (R - 1), end="")

else:
    my, mx = find_min_index()

    if my % 2 == 0:
        for _ in range(my // 2):
            print("R" * (C - 1) + "D" + "L" * (C - 1) + "D", end="")

        print("DR", end="")
        col = 1
        while col != C - 1:
            if col < mx:
                print("URDR", end="")
            elif col >= mx:
                print("RURD", end="")
            col += 2

        for _ in range((R - 1 - (my + 1)) // 2):
            print("D" + "L" * (C - 1) + "D" + "R" * (C - 1), end="")
    else:
        for _ in range(my // 2):
            print("R" * (C - 1) + "D" + "L" * (C - 1) + "D", end="")

        col = 0
        while col != C - 2:
            if col < mx:
                print("DRUR", end="")
            elif col >= mx:
                print("RDRU", end="")
            col += 2
        print("RD", end="")

        for _ in range((R - 1 - my) // 2):
            print("D" + "L" * (C - 1) + "D" + "R" * (C - 1), end="")
