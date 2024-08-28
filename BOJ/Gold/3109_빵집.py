# 20240828
# 34:29
# 1 / 3

"""
00:00 - 18:00 : 그리디 구현 및 제출 (틀렸습니다)
18:00 - 31:00 : DFS&그리디 구현 및 제출 (시간초과)
31:00 - 34:29 : impossible 코드 추가 (정답)

처음에 틀린 이유는 greedy하게 위로 갈 수 있으면 가다가, 막히면 break라,
dfs개념을 적용시키지 않아서 틀림.

두 번째는 로직은 합리적이었으나, 시간초과 났음.
그래서 시간 어떻게 줄일 수 있나, 생각해보니,
이미 실패해서 되돌아와서 route.pop()하는 경우는 나중에도 갈 필요 없음.
그래서 바로 impossible 로직 추가해 주고 정답.
"""

direction_y = (-1, 0, 1)  # 맨 위의 행부터 출발하므로, 위->아래의 행 탐색 순서


def oob(y):
    return y < 0 or r <= y


def dfs(y, x):
    global find_proper_pipeline

    if x == c - 1:
        find_proper_pipeline = True
        return

    for dy in direction_y:
        ny, nx = y + dy, x + 1
        if not oob(ny) and not area[ny][nx] and not impossible[ny][nx]:
            route.append((ny, nx))
            dfs(ny, nx)
            if find_proper_pipeline:  # 위의 재귀에서 적절한 파이프라인 찾았다면 return (현재의 (ny, nx)가 route에 포함돼야 하기 때문)
                return
            impossible[ny][nx] = 1  # 위의 재귀에서 적절한 파이프라인 못 찾았다면, 해당 좌표 (route에 포함될 수 없는) 불가능 처리
            route.pop()


def align_pipe_line(start_row):  # 현재 행에서 출발하는 파이프라인을 구상해보고, 유효한 게 있다면 방문처리하는 함수
    global route

    sy, sx = start_row, 0
    route = [(sy, sx)]
    dfs(sy, sx)

    if find_proper_pipeline:  # 유효한 파이프라인에 대해 방문 처리
        for ry, rx in route:
            area[ry][rx] = 1


r, c = map(int, input().split())
area = [[1 if i == 'x' else 0 for i in str(input())] for _ in range(r)]  # 갈 수 없는 곳은 1로, 갈 수 있는 곳은 0으로

impossible = [[0] * c for _ in range(r)]  # 해당 좌표에서 DFS한다 해도 마지막 열에 도착할 수 없으면 1

answer = 0
for i in range(r):  # 1열의 모든 행에서 출발시켜봄
    find_proper_pipeline = False
    align_pipe_line(i)  # 파이프라인 맞춰보기
    if find_proper_pipeline:  # 적절한 파이프라인 찾았다면 +=1
        answer += 1
print(answer)
