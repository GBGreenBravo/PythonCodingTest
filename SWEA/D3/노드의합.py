# 20240805
# 15:21
# 1 / 1

def post_order(index):  # 후위 순회
    if index > n:  # 인덱스 범위 넘어서면 return None
        return

    left = post_order(index * 2)
    right = post_order(index * 2 + 1)

    if left and right:  # 자식노드 둘다 있으면
        sm = left + right
    elif left and not right:  # 왼쪽 자식노드만 있다면 (완전이진트리이므로, 오른쪽 자식노드만 있는 경우는 없음.)
        sm = left
    elif not left and not right:  # 현재가 리프노드라면
        sm = complete_binary_tree[index]

    complete_binary_tree[index] = sm
    return sm


T = int(input())
for test_case in range(1, T + 1):
    n, m, l = map(int, input().split())
    complete_binary_tree = [None for _ in range(n + 1)]
    for _ in range(m):
        idx, value = map(int, input().split())
        complete_binary_tree[idx] = value

    post_order(1)

    print(f"#{test_case} {complete_binary_tree[l]}")
