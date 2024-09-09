# 20240909
# 17:53
# 1 / 2

# break 수행 시, break로 탈출하는 반복문 꼭 체크해주자..!

from collections import deque

direction = ((0, -1), (-1, 0), (0, 1))  # 좌 상 우


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


# 궁수 위치 3개(archer_arr)로 게임 수행하고, 죽인 적 수 반환하는 함수
def play_game():
    dead_enemy_cnt = 0  # 반환할 죽인 적 수

    game_area = [row[:] for row in area]  # deepcopy

    for _ in range(n):  # n번 동안 적 죽이고 적 내려오기 수행
        dead_enemies = set()  # 현재 궁수턴에서 죽는 적 좌표 담길 set

        # 각 궁수위치마다 죽일 적 찾는 BFS
        for archer in archer_arr:
            visited = [[0] * m for _ in range(n)]  # 방문체크 배열

            queue = deque()
            queue.append((n, archer, 0))  # 궁수 위지 좌표, 거리

            while queue:
                y, x, distance = queue.popleft()

                if distance == d:  # 궁수로부터의 거리가 d라면, 더이상 못 가므로 break
                    break

                for dy, dx in direction:  # 좌 상 우 순서
                    ny, nx = y + dy, x + dx
                    if oob(ny, nx) or visited[ny][nx]:
                        continue
                    if game_area[ny][nx]:  # 적 있다면
                        dead_enemies.add((ny, nx))  # 죽일 적 set에 넣어놓고 break
                        break
                    visited[ny][nx] = 1
                    queue.append((ny, nx, distance + 1))
                else:  # 죽일 적 못 찾았다면 계속
                    continue
                break  # 죽일 적 찾았다면 break

        dead_enemy_cnt += len(dead_enemies)  # += 죽이게 되는 적의 수
        for ey, ex in dead_enemies:
            game_area[ey][ex] = 0  # 죽임 처리 (1 -> 0)

        # 적 한칸씩 내려옴 처리
        game_area.pop()
        game_area.insert(0, [0] * m)

    return dead_enemy_cnt  # 현재 궁수 조합에서, 죽인 적 수 반환


# m 중에서 궁수 3명의 위치를 조합하는 함수
def pick_archers(cnt, start_idx):
    global max_answer

    if cnt == 3:  # 조합 완성되면
        max_answer = max(max_answer, play_game())  # 최대값 갱신
        return

    for i in range(start_idx, m):
        archer_arr.append(i)
        pick_archers(cnt + 1, i + 1)
        archer_arr.pop()


n, m, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

max_answer = 0
archer_arr = []
pick_archers(0, 0)  # 궁수 3명 조합
print(max_answer)


"""
# 20240806
# 35:33
# 1 / 1

from collections import deque

n, m, d = map(int, input().split())
area = [list(map(int,input().split())) for _ in range(n)]


def oob(y, x):
    return not(0 <= y < n) or not(0 <= x < m)


def play_game(archer_lst):  # archer_lst로 고정된 궁수 위치로, 게임의 규칙대로 게임을 수행하는 함수
    global answer

    delete_cnt = 0  # 제거된 적을 세는 변수
    game_area = [row[:] for row in area]  # area를 play_game() 호출마다 써야하기에, copy

    for _ in range(n):  # enemy 전진의 최대 횟수는 n - 1번. 맨 처음의 상태도 포함해야 하기에 range(n)
        delete_set = set()  # 이번 턴에 제거될 적의 좌표 담는 set (다른 궁수가 같은 적 좌표 가리킬 수도 있어서 set으로 중복 제거)

        for archer in archer_lst:  # 한 궁수에 대해
            front_y, front_x = n - 1, archer  # 궁수 바로 앞의 좌표 (distance = 1)

            # 아래부터 탐색
            visited = [[0] * m for _ in range(n)]
            queue = deque()
            queue.append((front_y, front_x, 1))

            enemy = None
            while queue:
                cy, cx, distance = queue.popleft()  # 현재좌표와, 궁수로부터의 거리

                if distance > d:  # 궁수로부터의 거리가 d를 넘어서면, 유효한 거리 d 안에 적 없다는 뜻이므로 break
                    break

                if game_area[cy][cx] == 1:  # 현재 탐색한 좌표에 적이 있다면, enemy에 저장하고 break
                    enemy = (cy, cx)
                    break

                for dy, dx in ((0, -1), (-1, 0), (0, 1)):  # (좌, 상, 우) 우선순위 대로 탐색
                    ny, nx = cy + dy, cx + dx
                    if oob(ny, nx) or visited[ny][nx]:
                        continue
                    visited[ny][nx] = 1
                    queue.append((ny, nx, distance + 1))

            if enemy:
                delete_set.add(enemy)  # 이 궁수의 유효한 거리 내의 최우선순위의 적 좌표 저장.

        for delete_y, delete_x in delete_set:  # 제거할 적 제거하고 delete_cnt += 1
            game_area[delete_y][delete_x] = 0
            delete_cnt += 1

        game_area = [[0] * m] + game_area[:-1]  # 맨 윗칸에 0배열 추가하고 아래로 한칸씩 이동 (마지막 행은 삭제됨)

    answer = max(answer, delete_cnt)  # answer 갱신


def dfs_archer(archer_cnt, archer_lst, before):  # 선발된 궁수 수, 선발된 궁수 index 배열, 이전에 뽑은 궁수 index
    if archer_cnt == 3:  # 궁수 3명이면 play_game()
        play_game(archer_lst)
        return

    for i in range(before + 1, m):  # 중복을 피하기 위해 before+1부터 탐색
        if not archer_visited[i]:
            archer_visited[i] = 1
            dfs_archer(archer_cnt + 1, archer_lst + [i], i)
            archer_visited[i] = 0


answer = 0
archer_visited = [0] * m  # 궁수 위치 중복을 피하기 위한 방문배열
dfs_archer(0, [], -1)
print(answer)
"""