N = int(input())
costs = [list(map(int, input().split())) for _ in range(N)]

answer = 1e6 + 1

now = [1e6, costs[0][1], costs[0][2]]
for idx in range(1, N - 1):
    nex = costs[idx][:]
    nex[0] += min(now[1], now[2])
    nex[1] += min(now[0], now[2])
    nex[2] += min(now[0], now[1])
    now = nex
answer = min(answer, costs[-1][0] + now[1], costs[-1][0] + now[2])

now = [costs[0][0], 1e6, costs[0][2]]
for idx in range(1, N - 1):
    nex = costs[idx][:]
    nex[0] += min(now[1], now[2])
    nex[1] += min(now[0], now[2])
    nex[2] += min(now[0], now[1])
    now = nex
answer = min(answer, costs[-1][1] + now[0], costs[-1][1] + now[2])

now = [costs[0][0], costs[0][1], 1e6]
for idx in range(1, N - 1):
    nex = costs[idx][:]
    nex[0] += min(now[1], now[2])
    nex[1] += min(now[0], now[2])
    nex[2] += min(now[0], now[1])
    now = nex
answer = min(answer, costs[-1][2] + now[0], costs[-1][2] + now[1])

print(answer)
