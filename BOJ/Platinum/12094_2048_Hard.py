# 20241021
# 46:54
# 1 / 3

# 남쪽으로 밀 때, r의 range설정을 range(N - 1, -1, -1)로 했어야 하는데, range(N)으로 설정해서 2번 틀림.

direction = ((0, 1), (0, -1), (1, 0), (-1, 0))  # 0/1/2/3 -> 동/서/남/북


def push(arr, d_idx):
    new_arr = [[0] * N for _ in range(N)]
    if d_idx == 0:
        for r in range(N):
            idx = N - 1
            done = [0] * N
            for c in range(N - 1, -1, -1):
                if arr[r][c]:
                    if idx != N - 1 and not done[idx + 1] and arr[r][c] == new_arr[r][idx + 1]:
                        new_arr[r][idx + 1] *= 2
                        done[idx + 1] = 1
                    else:
                        new_arr[r][idx] = arr[r][c]
                        idx -= 1
    elif d_idx == 1:
        for r in range(N):
            idx = 0
            done = [0] * N
            for c in range(N):
                if arr[r][c]:
                    if idx != 0 and not done[idx - 1] and arr[r][c] == new_arr[r][idx - 1]:
                        new_arr[r][idx - 1] *= 2
                        done[idx - 1] = 1
                    else:
                        new_arr[r][idx] = arr[r][c]
                        idx += 1
    elif d_idx == 2:
        for c in range(N):
            idx = N - 1
            done = [0] * N
            for r in range(N - 1, -1, -1):
                if arr[r][c]:
                    if idx != N - 1 and not done[idx + 1] and arr[r][c] == new_arr[idx + 1][c]:
                        new_arr[idx + 1][c] *= 2
                        done[idx + 1] = 1
                    else:
                        new_arr[idx][c] = arr[r][c]
                        idx -= 1
    else:  # elif d_idx == 3:
        for c in range(N):
            idx = 0
            done = [0] * N
            for r in range(N):
                if arr[r][c]:
                    if idx != 0 and not done[idx - 1] and arr[r][c] == new_arr[idx - 1][c]:
                        new_arr[idx - 1][c] *= 2
                        done[idx - 1] = 1
                    else:
                        new_arr[idx][c] = arr[r][c]
                        idx += 1

    for r in range(N):
        for c in range(N):
            if arr[r][c] != new_arr[r][c]:
                return new_arr, False

    return new_arr, True


def dfs(arr, cnt):
    global max_answer
    now_max = max(map(max, arr))
    max_answer = max(max_answer, now_max)

    if now_max * 2**(10 - cnt) <= max_answer:  # 현재최대값이 아무리 커져도 최대값 이하면 return
        return

    if cnt == 10:
        return

    for d_idx in range(4):
        new_arr, not_changed = push(arr, d_idx)
        if not_changed:  # 밀어도 변화 없으면 continue
            continue
        dfs(new_arr, cnt + 1)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

max_answer = 0
dfs(area, 0)
print(max_answer)
