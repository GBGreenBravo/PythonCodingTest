def bfs(sy, sx):
    from collections import deque
    visited = [[0] * N for _ in range(M)]
    visited[sy][sx] = 1
    queue = deque([(sy, sx)])

    while queue:
        y, x = queue.popleft()
        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx
            if ny < 0 or M <= ny or nx < 0 or N <= nx:
                continue
            if visited[ny][nx] or area[ny][nx] == 1:
                continue
            if area[ny][nx] == 2:
                return
            visited[ny][nx] = 1
            queue.append((ny, nx))

    print((sy + 1, sx + 1), "부터 보물(2)까지의 초기 경로는 막혀있으면 안됩니다!")


T = int(input())
for test in range(1, T + 1):
    print(f"{test}번 테케")

    M, N = map(int, input().split())
    if not (5 <= M <= 20):
        print("M(행) 범위 틀림!")
    if not (5 <= N <= 20):
        print("N(열) 범위 틀림!")

    K, B, D, R = map(int, input().split())
    if not (1 <= K <= 10):
        print("K(플레이어 수) 범위 틀림!")
    if not (1 <= B <= 10):
        print("B(폭탄 사거리) 범위 틀림!")
    if not (1 <= D <= 20):
        print("D(임시 벽 수명) 범위 틀림!")
    if not (3 <= R <= min(M, N)):
        print("R(회전 정사각형 길이) 범위 틀림!")
    if R % 2 == 0:
        print("R(회전 정사각형 길이)은 홀수여야 합니다!")

    area = [list(map(int, input().split())) for _ in range(M)]

    for i in range(M):
        for j in range(N):
            if area[i][j] == 2:
                if i - R//2 < 0 or M <= i + R//2 or j - R//2 < 0 or N <= j + R//2:
                    print("범위 내의 R로 설정해 주세요.")

    for _ in range(K):
        py, px, p_bomb = map(int, input().split())
        py, px = py - 1, px - 1
        if area[py][px]:
            print((py + 1, px + 1), "에는 빈칸(0)이어야 합니다!")
        bfs(py, px)

print("테케 검증 완료")
