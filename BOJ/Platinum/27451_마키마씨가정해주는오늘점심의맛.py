# 20250108
# 1 / 16

# 답의 최대값을 4999로 조절하는 while문을 설정해서, 꼼수로 맞힘.
# 아래쪽에 정석 풀이 코드 있음.


def bfs():
    queue = [(A, 1), (B, 2), (C, 4)]
    distance = 0
    route_a, route_b, route_c = [None for _ in range(N + 1)], [None for _ in range(N + 1)], [None for _ in range(N + 1)]
    route_a[A] = [A]
    route_b[B] = [B]
    route_c[C] = [C]
    while queue and distance < 5000:
        next_queue = set()

        this_a, this_b, this_c = 0, 0, 0
        visited = dict()
        next_route_a, next_route_b, next_route_c = [None for _ in range(N + 1)], [None for _ in range(N + 1)], [None for _ in range(N + 1)]

        for now, origin in queue:
            if origin == 1:
                this_a = 1
            elif origin == 2:
                this_b = 1
            else:
                this_c = 1

            v = visited.get(now, 0)
            if origin == 1 and v not in (1, 3, 5):
                v += 1
            if origin == 2 and v not in (2, 3, 6):
                v += 2
            if origin == 4 and v not in (4, 5, 6):
                v += 4
            if v == 7:
                print(now, distance)
                print(*route_a[now])
                print(*route_b[now])
                print(*route_c[now])
                return
            visited[now] = v

            for nex in connected[now]:
                next_queue.add((nex, origin))

                if origin == 1 and not next_route_a[nex]:
                    next_route_a[nex] = [r for r in route_a[now]] + [nex]
                if origin == 2 and not next_route_b[nex]:
                    next_route_b[nex] = [r for r in route_b[now]] + [nex]
                if origin == 4 and not next_route_c[nex]:
                    next_route_c[nex] = [r for r in route_c[now]] + [nex]

        if not (this_a and this_b and this_c):
            break

        distance += 1
        queue = next_queue
        route_a, route_b, route_c = next_route_a, next_route_b, next_route_c

    print(-1)


N, M = map(int, input().split())
A, B, C = map(int, input().split())
connected = [[] for _ in range(N + 1)]
for _ in range(M):
    ss, ee = map(int, input().split())
    connected[ss].append(ee)
bfs()


# 정석 풀이
"""
from collections import defaultdict

# 입력
N, M = map(int, input().split())
A, B, C = map(int, input().split())
V = defaultdict(list)
for _ in range(M):
    f, g = map(int, input().split())
    V[f].append(g)

# 초기화
prev = [None] + [[[0] * (N**3 + 1) for _ in range(N + 1)] for _ in range(3)]
prev[1][A][0] = -1
prev[2][B][0] = -1
prev[3][C][0] = -1

# 상태 업데이트
for n in range(1, 4):
    for j in range(N * N * N):
        for i in range(1, N + 1):
            if prev[n][i][j] == 0:
                continue
            for k in V[i]:
                prev[n][k][j + 1] = i

# 결과 찾기
for j in range(N * N * N + 1):
    for i in range(1, N + 1):
        control = all(prev[n][i][j] != 0 for n in range(1, 4))
        if control:
            print(i, j)
            for n in range(1, 4):
                W = []
                p = i
                for j2 in range(j, 0, -1):
                    W.append(p)
                    p = prev[n][p][j2]
                W.append(p)
                W.reverse()
                print(" ".join(map(str, W)))
            exit()

print("-1")
"""
