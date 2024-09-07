# 20240907
# 57:29
# 1 / 9

direction = (0, 1), (0, -1), (1, 0), (-1, 0)


def oob(y, x):
    return y < 0 or n <= y or x < 0 or m <= x


def dfs(y, x, cnt):
    dd = int(area[y][x])  # 현재 칸에 적힌 숫자

    next_cnts = []  # 다음 재귀에서의 반환값(갈 수 있는 최대 칸 수)들을 담을 배열
    for dy, dx in direction:
        ny, nx = y + dy * dd, x + dx * dd
        if oob(ny, nx) or area[ny][nx] == 'H':  # 영역 밖 / 구멍
            continue
        if visited[ny][nx]:  # 현재 DFS에서 방문된 적 있으면 무한으로 가능 => -1 출력 and exit()
            print(-1)
            exit()
        if done[ny][nx]:  # 이미 갈 수 있는 칸 수가 체크된 곳이라면(= 끝까지 가본 DFS로 체크됐다면)
            next_cnts.append(done[ny][nx])  # 재귀호출하지 않고 done에서 꺼내 씀
            continue
        # 체크되지 않은 칸은 DFS 재귀호출로
        visited[ny][nx] = 1
        next_cnts.append(dfs(ny, nx, cnt + 1))
        visited[ny][nx] = 0

    if not next_cnts:  # 더 이상 갈 곳 없다면, return 1
        done[y][x] = 1
        return 1
    else:  # 한 군데라도 갈 곳 있다면, done에 최대값 + 1 저장&return
        done[y][x] = max(next_cnts) + 1
        return max(next_cnts) + 1


n, m = map(int, input().split())
area = [list(str(input())) for _ in range(n)]

# DFS에서 방문체크를 위한 배열
visited = [[0] * m for _ in range(n)]
visited[0][0] = 1

# DFS로 탐색된 곳에 대해,  갈 수 있는 최대 칸 수를 저장할 배열
done = [[0] * m for _ in range(n)]

print(dfs(0, 0, 1))
