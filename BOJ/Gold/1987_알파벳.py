# 20240901
# 27:03
# 1 / 5

# 방문 배열을 [0] * 26로 선언하지 않고,
# dfs()의 인자로 전달하거나, set의 not in 으로 검사를 하면, 모두 시간초과 났던 문제

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))


def oob(y, x):
    return y < 0 or r <= y or x < 0 or c <= x


def dfs(y, x, len_arr):
    global answer
    answer = max(answer, len_arr)  # 최대값 갱신
    if answer == answer_limit:  # 가능한 최대값 되면, 그 값 출력하고 종료
        print(answer)
        exit()

    for dy, dx in direction:
        ny, nx = y + dy, x + dx
        if oob(ny, nx):
            continue
        ord_idx = area[ny][nx]
        if visited[ord_idx]:
            continue
        visited[ord_idx] = 1
        dfs(ny, nx, len_arr + 1)
        visited[ord_idx] = 0


r, c = map(int, input().split())
area = [[ord(i) - ord('A') for i in str(input())] for _ in range(r)]  # 입력 받을 때 A->0 Z->25로 변경

answer_limit = len(set.union(*map(lambda x: set(x), area)))  # 입력된 알파벳(중복 제거) 총 수
answer = 1

visited = [0] * 26  # 알파벳 26개의 방문 배열
visited[area[0][0]] = 1
dfs(0, 0, 1)
print(answer)
