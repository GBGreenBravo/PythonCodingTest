# 20241020
# 34:20
# 1 / 1

"""
01
32
위의 네 구역이 각각 흩어지지 않고 단체로 움직이기 때문에,
아래와 같은 규칙 생김.
따라서 R개의 연산들에 대해, 네 구역에 바뀌는 영향만 체크해줬다가, 나중에 일괄반영하면 됨.

1 -> 상하 뒤집어서 바꿈
    전치 & 반시계회전
    0/1/2/3 -> 3/2/1/0
2 -> 좌우 뒤집어서 바꿈
    전치 & 시계회전
    0/1/2/3 -> 1/0/3/2
3 -> 오른쪽 90도 회전
    0/1/2/3 -> 3/0/1/2 % 시계회전
4 -> 왼쪽 90도 회전
    0/1/2/3 -> 1/2/3/0 & 반시계회전
5 -> 영역 나눠서 시계방향
    0/1/2/3 -> 3/0/1/2
6 -> 영역 나눠서 반시계방향
    0/1/2/3 -> 1/2/3/0
"""

N, M, R = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(N)]
operations = list(map(int, input().split()))

transposed = 0
rotated_cnt = 0
rotating = [0, 1, 2, 3]
for operation in operations:
    if operation == 1:
        transposed ^= 1
        rotated_cnt *= -1
        rotated_cnt -= 1
        rotating[0], rotating[1], rotating[2], rotating[3] = rotating[3], rotating[2], rotating[1], rotating[0]
    elif operation == 2:
        transposed ^= 1
        rotated_cnt *= -1
        rotated_cnt += 1
        rotating[0], rotating[1], rotating[2], rotating[3] = rotating[1], rotating[0], rotating[3], rotating[2]
    elif operation == 3:
        rotating[0], rotating[1], rotating[2], rotating[3] = rotating[3], rotating[0], rotating[1], rotating[2]
        rotated_cnt += 1
    elif operation == 4:
        rotating[0], rotating[1], rotating[2], rotating[3] = rotating[1], rotating[2], rotating[3], rotating[0]
        rotated_cnt -= 1
    elif operation == 5:
        rotating[0], rotating[1], rotating[2], rotating[3] = rotating[3], rotating[0], rotating[1], rotating[2]
    else:  # elif operation == 6:
        rotating[0], rotating[1], rotating[2], rotating[3] = rotating[1], rotating[2], rotating[3], rotating[0]

area_0 = [area[row][:M//2] for row in range(N//2)]
area_1 = [area[row][M//2:] for row in range(N//2)]
area_2 = [area[row][M//2:] for row in range(N//2, N)]
area_3 = [area[row][:M//2] for row in range(N//2, N)]

if transposed:
    area_0 = [list(row) for row in zip(*area_0)]
    area_1 = [list(row) for row in zip(*area_1)]
    area_2 = [list(row) for row in zip(*area_2)]
    area_3 = [list(row) for row in zip(*area_3)]

rotated_cnt %= 4
for _ in range(rotated_cnt):
    area_0 = [list(row)[::-1] for row in zip(*area_0)]
    area_1 = [list(row)[::-1] for row in zip(*area_1)]
    area_2 = [list(row)[::-1] for row in zip(*area_2)]
    area_3 = [list(row)[::-1] for row in zip(*area_3)]

final = [area_0, area_1, area_2, area_3]
final[rotating.index(0)], final[rotating.index(1)], final[rotating.index(2)], final[rotating.index(3)] = final[0], final[1], final[2], final[3]
for i in range(len(final[0])):
    print(*final[0][i] + final[1][i], sep=" ")
for i in range(len(final[3])):
    print(*final[3][i] + final[2][i], sep=" ")
