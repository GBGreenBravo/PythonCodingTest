# 20250715
# 27:28
# 1 / 1


def solve():
    global arr

    N, M = map(int, input().split())
    start_idx = 1
    while start_idx < N + M:
        start_idx *= 2
    arr = [0 for _ in range(start_idx * 2)]
    for i in range(start_idx, start_idx + N):
        arr[i] = 1
    for i in range(start_idx - 1, 0, -1):
        arr[i] = arr[i * 2] + arr[i * 2 + 1]

    # index: 영화 번호 / value: 세그먼트트리 마지막 depth의 index (1 ~ start_idx)
    where = [N + 1 - i for i in range(N + 1)]

    order = list(map(int, input().split()))
    answer = []
    added = N + 1  # 세그먼트트리에 다음에 추가될 index 기록용
    for o in order:
        arr[1] -= 1
        answer.append(cal_and_remove(start_idx - 1 + where[o], 1, start_idx, start_idx * 2 - 1))
        where[o] = added
        add(start_idx - 1 + added)
        added += 1

    print(*answer, sep=" ")


def cal_and_remove(target_idx, now_idx, left, right):
    if left == right:
        return 0

    mid = (left + right) // 2
    if target_idx <= mid:
        arr[now_idx * 2] -= 1
        return cal_and_remove(target_idx, now_idx * 2, left, mid) + arr[now_idx * 2 + 1]
    else:
        arr[now_idx * 2 + 1] -= 1
        return cal_and_remove(target_idx, now_idx * 2 + 1, mid + 1, right)


def add(target_idx):
    arr[target_idx] = 1
    while target_idx != 1:
        target_idx //= 2
        arr[target_idx] = arr[target_idx * 2] + arr[target_idx * 2 + 1]


T = int(input())
for _ in range(T):
    solve()
