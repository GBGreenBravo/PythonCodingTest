# 20240915
# 43:43
# 1 / 3

# 이 문제의 경우에는, range(2**n) 이진수 활용하면 시간초과 나는 문제임! (백트래킹을 반영 못 했기에)
# union() 함수 쓸 때, {} 씌우는 거 까먹지 말자!!

# 육각형 한변을 루트5로 생각하고, dy/dx 설정
direction = ((-2, 1), (0, 2), (2, 1), (2, -1), (0, -2), (-2, -1))


def dfs(cnt, y, x, d, visited):
    global answer

    # (종료 조건) 이제 1번만 더 방향회전하면 n번 방향회전하는 경우
    if cnt == n - 1:
        # 왼쪽으로 방향회전
        left = (d - 1) % 6
        dy, dx = direction[left]
        ny, nx = y + dy, x + dx
        if (ny, nx) in visited:  # 방문한 좌표인 경우에만, answer += 1
            answer += 1

        # 오른쪽으로 방향회전
        right = (d + 1) % 6
        dy, dx = direction[right]
        ny, nx = y + dy, x + dx
        if (ny, nx) in visited:  # 방문한 좌표인 경우에만, answer += 1
            answer += 1
        return

    else:
        # 왼쪽으로 방향회전
        left = (d - 1) % 6
        dy, dx = direction[left]
        ny, nx = y + dy, x + dx
        if (ny, nx) not in visited:  # 방문하지 않은 좌표인 경우에만, 다음 재귀호출
            dfs(cnt + 1, ny, nx, left, visited.union({(ny, nx)}))

        # 오른쪽으로 방향회전
        right = (d + 1) % 6
        dy, dx = direction[right]
        ny, nx = y + dy, x + dx
        if (ny, nx) not in visited:  # 방문하지 않은 좌표인 경우에만, 다음 재귀호출
            dfs(cnt + 1, ny, nx, right, visited.union({(ny, nx)}))


n = int(input())

answer = 0
dfs(0, -2, 1, 0, {(0, 0), (-2, 1)})  # 0idx 방향으로 직진 1번 한 상태를, 초기값으로 설정.
print(answer)
