# 20241003
# 30:14
# 1 / 1

# 19237_어른상어

"""
풀이 시간: 30분 (14:03 ~ 14:33)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (14:03 - 14:10)


2. 구현 (14:10 - 14:28)
    이전 풀이와 풀이방식이 상당히 달랐습니다.

    이전 풀이는 특정 상태의 특정 기간 동안의 유지를, 플레이어별로 관리했지만,
    이번 풀이는 칸별로 관리했습니다.

    그리고 area에는 플레이어 번호만을 남겨두고 구현한 점, 현재 방향을 위한 배열도 따로 둔 점 등 차이가 많았습니다.

    다른 풀이방식에서도 큰 어려움 없이 단번에 구현해냈다는 것에 의의가 있었습니다.


3. 디버깅 (14:28 - 14:33)
    주석 처리된 부분처럼, 동시 이동이 아닌 행/열 오름차순 순차적 이동으로 구현됐기에, 2번째 테케에서 출력이 달랐습니다.

    그림 설명과 다르게 이동하는 플레이어가 있음을 print디버깅을 통해 확인하고,
    위의 원인을 파악할 수 있었습니다.
"""

direction = (None, (-1, 0), (1, 0), (0, -1), (0, 1))


def oob(y, x):
    return y < 0 or n <= y or x < 0 or n <= x


def move_all():
    global area, death_cnt

    new_area = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if area[y][x]:
                p_idx = area[y][x]
                now_d = people_direction[p_idx]

                now_priorities = direction_priorities[p_idx][now_d]

                for d_idx in now_priorities:
                    dy, dx = direction[d_idx]
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or arbitrary_area[ny][nx]:
                        continue

                    if new_area[ny][nx]:
                        death_cnt += 1
                        if p_idx < new_area[ny][nx]:
                            people_direction[p_idx] = d_idx
                            # arbitrary_area[ny][nx] = [k + 1, p_idx]
                            new_area[ny][nx] = p_idx
                    else:
                        people_direction[p_idx] = d_idx
                        # arbitrary_area[ny][nx] = [k + 1, p_idx]
                        new_area[ny][nx] = p_idx
                    break
                else:
                    for d_idx in now_priorities:
                        dy, dx = direction[d_idx]
                        ny, nx = y + dy, x + dx
                        if oob(ny, nx) or not arbitrary_area[ny][nx] or arbitrary_area[ny][nx][1] != p_idx:
                            continue

                        if new_area[ny][nx]:
                            death_cnt += 1
                            if p_idx < new_area[ny][nx]:
                                new_area[ny][nx] = p_idx
                                people_direction[p_idx] = d_idx
                                # arbitrary_area[ny][nx] = [k + 1, p_idx]
                        else:
                            new_area[ny][nx] = p_idx
                            people_direction[p_idx] = d_idx
                            # arbitrary_area[ny][nx] = [k + 1, p_idx]
                        break

    area = new_area

    for y in range(n):
        for x in range(n):
            if arbitrary_area[y][x]:
                arbitrary_area[y][x][0] -= 1
                if not arbitrary_area[y][x][0]:
                    arbitrary_area[y][x] = 0
            if area[y][x]:
                arbitrary_area[y][x] = [k, area[y][x]]


n, m, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

people_direction = [None] + list(map(int, input().split()))

direction_priorities = [None]
for _ in range(m):
    direction_priorities.append([None] + list(tuple(map(int, input().split())) for _ in range(4)))

arbitrary_area = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if area[i][j]:
            arbitrary_area[i][j] = [k, area[i][j]]

death_cnt = 0
turn = 0
while turn <= 1000:
    turn += 1

    move_all()

    if death_cnt == m - 1:
        print(turn)
        break
else:
    print(-1)
