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
