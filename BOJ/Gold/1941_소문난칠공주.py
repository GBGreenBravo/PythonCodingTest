# 20240808
# 41:38
# 1 / 1

# print(25 * 23 * 11 * 19 * 4)  # 25 C 7

from collections import deque

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return (y < 0) or (5 <= y) or (x < 0) or (5 <= x)


def bfs(arr):  # 7개의 좌표 배열에 대해 칠공주 구성 가능성 유무 파악하는 BFS 함수
    queue = deque()
    queue.append(arr[0])
    visited = [[False] * 5 for _ in range(5)]
    visited[arr[0][0]][arr[0][1]] = True

    while queue:
        y, x = queue.pop()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            if (ny, nx) in arr and not visited[ny][nx]:  # arr에 있는 좌표고, 가본적 없는 좌표면
                visited[ny][nx] = True
                queue.append((ny, nx))

    for y, x in arr:
        if not visited[y][x]:  # 하나라도 상하좌우로 연결 안 돼있으면 return False
            return False

    S_cnt, Y_cnt = 0, 0
    for y, x in arr:
        if area[y][x] == 'S':
            S_cnt += 1
        else:
            Y_cnt += 1
    return True if S_cnt > Y_cnt else False  # 이다솜파가 더 많으면 return True


def check(arr):
    arr = [divmod(i, 5) for i in arr]  # 0부터 24로 좌표 나타냈으므로, 이를 (y, x)로 변환
    if not bfs(arr):  # 칠공주 불가능하면 return
        return False
    else:  # 가능하면 cnt+=1
        global answer_cnt
        answer_cnt += 1


def make_7_combination_from_25(start):  # 25개의 좌표에서 7개를 중복없이 뽑는 DFS
    if len(combination_arr) == 7:  # 종료조건: 7개의 좌표가 뽑히면
        check(combination_arr)  # 칠공주 구성되는지 살펴보기
        return

    if start == 25:  # 조기 종료 조건: 현재 함수에서 시작하는 index가 범위 밖이면 return
        return

    for i in range(start, 25):
        combination_arr.append(i)
        make_7_combination_from_25(i + 1)
        combination_arr.pop()


area = [list(str(input())) for _ in range(5)]
combination_arr = []  # DFS에서 활용할 배열
answer_cnt = 0
make_7_combination_from_25(0)  # DFS 시작
print(answer_cnt)
