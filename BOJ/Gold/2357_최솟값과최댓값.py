# 20241102
# 1 / 1

# 세그먼트트리 첫 문제

N, M = map(int, input().split())
inputNs = [int(input()) for _ in range(N)]
inputMs = [tuple(map(int, input().split())) for _ in range(M)]
length = 1
while length < N:
    length *= 2
length *= 2

max_tree = [0] * length
min_tree = [0] * length

leaf_start = length // 2
for i in range(N):
    max_tree[i + leaf_start] = inputNs[i]
    min_tree[i + leaf_start] = inputNs[i]

while length != 2:
    for i in range(length // 2, length, 2):
        if not min_tree[i]:
            break
        elif not min_tree[i + 1]:
            max_tree[i // 2] = max_tree[i]
            min_tree[i // 2] = min_tree[i]
            break
        else:
            max_tree[i // 2] = max(max_tree[i], max_tree[i + 1])
            min_tree[i // 2] = min(min_tree[i], min_tree[i + 1])
    length //= 2

for left, right in inputMs:
    left = left - 1 + leaf_start
    right = right - 1 + leaf_start
    max_left, max_right, min_left, min_right = max_tree[left], max_tree[right], min_tree[left], min_tree[right]

    while True:
        next_left, next_right = (left + 1) // 2, (right - 1) // 2
        if next_left > next_right:
            break
        left, right = next_left, next_right

        max_left = max(max_left, max_tree[left])
        max_right = max(max_right, max_tree[right])

        min_left = min(min_left, min_tree[left])
        min_right = min(min_right, min_tree[right])

    print(min(min_left, min_right), max(max_left, max_right))
