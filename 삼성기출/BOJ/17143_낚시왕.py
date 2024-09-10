# 20240910
# 2:00:00 & 27:00
# 0 / 3   & 1 / 1

"""
풀이 시간: 2시간 & 27분 (09:00 ~ 11:00 & 19:26 ~ 19:53)
풀이 시도: 0 / 3 & 1 / 1


1. 문제 정독 & 풀이 구상 (09:00 - 09:07)
    문제를 읽고는 크게 어려운 점은 없다고 생각했습니다.
    다만, 상어의 이동을 구현할 때, R,C는 100이하인 반면, 초당 이동속도 s는 1000이하였기에,
    시간 초과가 발생하지 않도록, 이동처리를 %를 통해 축약해야겠다고 구상했습니다.


2. 구현 (09:07 - 09:32)



3. 검증 (09:32 - 09:41)


4. 틀렸습니다 (09:41 - 11:00)
    제일 치명적인 실수/오답 이라고 생각하는 'IndexError'이 떴습니다.
    10시 15분까지


    풀이 시간이 다 지나고 나서, 회고한 점은 아래와 같습니다.
    1) 왜 문제를 다시 (차분한 마음으로) 읽으려 하지 않았는가
    2) 시간이 많이 남은 시점에서도, 왜 코드를 싹 다 지우지 않았는가
    3) 다른 구상을 하려할 때, 온전한 구상이 바로 떠오르지 않음에도 왜 코드부터 쳤는가


5. 저녁에 재시도 (19:26 - 19:53)
    코드를 아예 처음부터 작성하니, 당연하게 적었던 2 * r / 2 * c 에 대해
    자연스레 의문을 가지게 됐고, 해당 부분이 기존 코드에서 틀렸음을 확인할 수 있었습니다.

    실제 시험장에서는, 코드의 정답 유무를 모르니,
    무조건! 1차 답안을 싹 다 지우고, 다시 문제를 읽고, 2차 답안을 천천히 한줄한줄 더 생각하며 작성해야겠습니다.
    그리고 실수를 줄이기 위해서, 시험장에서 그렇게 해야지 생각하는 것만으로는 충분히 체화되지 않을 것 같아,
    매일의 연습에서도 위 과정(1차 답안 완성 후, 싹 다 지우고, 다시 문제 읽고, 2차 답안 재작성)을 적용할 것입니다.
"""


direction = ((-1, 0), (0, 1), (1, 0), (0, -1))  # 북동남서
direction_convert = (None, 0, 2, 1, 3)  # 북/남/동/서 -> 북/동/남/서


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


# 모든 상어를 이동시키고, 먹기 처리하는 함수
def move_sharks():
    global area

    # 이동 처리
    new_area = [[[] for _ in range(c)] for _ in range(r)]  # 이동 후의 상어 정보를 담을 배열
    for i in range(r):
        for j in range(c):
            if area[i][j]:
                speed, d_idx, size = area[i][j][0]

                # 초속이 "남북 -> 2 * (r - 1) / 동서 -> 2 * (c - 1)" 보다 큰 경우를 위해, 나머지 연산자 적용
                revised_speed = speed % (2 * (r - 1) if d_idx in [0, 2] else 2 * (c - 1))

                # forward :  현재방향으로 갈 수 있는 최대 길이
                # backward : 현재방향 반대편으로 갈 수 있는 최대 길이
                # first :    먼저 마주하는 벽
                # second :   2번째로 마주하는 벽
                if d_idx == 0:  # 북
                    forward = i
                    backward = r - 1 - i
                    first, second = 0, r - 1
                elif d_idx == 2:  # 남
                    forward = r - 1 - i
                    backward = i
                    first, second = r - 1, 0
                elif d_idx == 1:  # 동
                    forward = c - 1 - j
                    backward = j
                    first, second = c - 1, 0
                elif d_idx == 3:  # 서
                    forward = j
                    backward = c - 1 - j
                    first, second = 0, c - 1

                # 현재 방향으로 갈 때, 벽 마주하지 않는다면
                if revised_speed <= forward:
                    di, dj = direction[d_idx]
                    ni, nj = i + di * revised_speed, j + dj * revised_speed
                    new_area[ni][nj].append((speed, d_idx, size))
                    continue

                # 첫 번째 벽에 닿옴이 확실하므로, 그에 따른 거리 축약 & 방향 전환
                revised_speed -= forward
                d_idx = (d_idx + 2) % 4

                # 두 번째 벽에 닿지는 않는다면
                if revised_speed <= forward + backward:
                    di, dj = direction[d_idx]
                    if d_idx in [0, 2]:
                        ni, nj = first + di * revised_speed, j
                    else:
                        ni, nj = i, first + dj * revised_speed
                    new_area[ni][nj].append((speed, d_idx, size))
                    continue

                # 두 번째 벽에 닿음이 확실하므로, 그에 따른 거리 축약 & 방향 전환
                revised_speed -= (forward + backward)
                d_idx = (d_idx + 2) % 4

                # 남은 거리 이동
                di, dj = direction[d_idx]
                if d_idx in [0, 2]:
                    ni, nj = second + di * revised_speed, j
                else:
                    ni, nj = i, second + dj * revised_speed
                new_area[ni][nj].append((speed, d_idx, size))

    # 먹기 처리
    for i in range(r):
        for j in range(c):
            if len(new_area[i][j]) > 1:  # 해당 칸에 상어 2마리 이상 있다면
                new_area[i][j] = [max(new_area[i][j], key=lambda shark_info: shark_info[2])]  # 사이즈 제일 큰 상어만 남기기

    area = [a[:] for a in new_area]


r, c, m = map(int, input().split())
sharks = [list(map(int, input().split())) for _ in range(m)]
area = [[[] for _ in range(c)] for _ in range(r)]
for shark_y, shark_x, shark_s, shark_d, shark_z in sharks:
    area[shark_y - 1][shark_x - 1].append((shark_s, direction_convert[shark_d], shark_z))

catched_sharks = 0

for col in range(c):
    # 현재 col에서 가장 가까운 상어 잡아먹기
    for row in range(r):
        if area[row][col]:
            catched_sharks += area[row][col][0][2]
            area[row][col] = []
            break

    # 전체 상어 이동&먹기 처리
    move_sharks()

print(catched_sharks)


# 틀렸던, 처음 제출한 코드
# 2 * r / 2 * c 를, 2 * (r - 1) / 2 * (c - 1) 로 고쳐주기만 하면 됐음.
# 구현하면서 활용하는 수에 대한 검증을 확실히 하고 넘어가자.
"""
direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
direction_convert = [None, 0, 2, 1, 3]

r, c, m = map(int, input().split())
area = [[[] for _ in range(c)] for _ in range(r)]
sharks = []
for _ in range(m):
    sy, sx, ss, sd, sz = map(int, input().split())
    sy, sx = sy - 1, sx - 1
    sd = direction_convert[sd]
    area[sy][sx].append((ss, sd, sz))

catched_sharks_size = 0
for col in range(c):
    for row in range(r):
        if area[row][col]:
            catched_sharks_size += area[row][col][0][2]
            area[row][col] = []
            break
    new_area = [[[] for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if area[i][j]:
                ss, sd, sz = area[i][j][0]
                revised_ss = ss % (2 * r if sd in [0, 2] else 2 * c)  # 이 부분을 2시간 동안 발견하지 못했음. 2*r / 2*c 가 아닌 2*(r-1) / 2*(c-1)

                forward, backward = 0, 0
                first_wall, second_wall = None, None
                if sd == 0:
                    forward = i
                    backward = r - 1 - i
                    first_wall, second_wall = 0, r - 1

                    if i == 0:
                        forward = r - 1
                        backward = 0
                        first_wall, second_wall = r - 1, 0
                        sd = 2
                elif sd == 2:
                    forward = r - 1 - i
                    backward = i
                    first_wall, second_wall = r - 1, 0

                    if i == r - 1:
                        forward = r - 1
                        backward = 0
                        first_wall, second_wall = 0, r - 1
                        sd = 0
                elif sd == 3:
                    forward = j
                    backward = c - 1 - j
                    first_wall, second_wall = 0, c - 1

                    if j == 0:
                        forward = c - 1
                        backward = 0
                        first_wall, second_wall = c - 1, 0
                        sd = 1
                else:
                    forward = c - 1 - j
                    backward = j
                    first_wall, second_wall = c - 1, 0

                    if i == c - 1:
                        forward = c - 1
                        backward = 0
                        first_wall, second_wall = 0, c - 1
                        sd = 3

                if revised_ss <= forward:
                    di, dj = direction[sd]
                    ni, nj = i + di * revised_ss, j + dj * revised_ss
                elif revised_ss <= forward * 2 + backward:
                    sd += 2
                    sd %= 4
                    di, dj = direction[sd]

                    revised_ss -= forward
                    if sd in [0, 2]:
                        ni, nj = first_wall + di * revised_ss, j
                    else:
                        ni, nj = i, first_wall + dj * revised_ss
                else:
                    di, dj = direction[sd]
                    revised_ss -= forward * 2 + backward
                    if sd in [0, 2]:
                        ni, nj = second_wall + di * revised_ss, j
                    else:
                        ni, nj = i, second_wall + dj * revised_ss

                new_area[ni][nj].append((ss, sd, sz))

    for i in range(r):
        for j in range(c):
            if len(new_area[i][j]) > 1:
                new_area[i][j] = [max(new_area[i][j], key=lambda x: x[2])]
    area = new_area

print(catched_sharks_size)
"""