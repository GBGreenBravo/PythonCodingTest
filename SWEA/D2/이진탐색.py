# 20240805
# 08:21
# 1 / 1

def in_order(index):  # 중위 순회
    global value

    if index > n:  # 종료조건: n 이상의 인덱스; 존재하지 않는 노드
        return

    in_order(index * 2)
    value += 1
    complete_binary_tree[index] = value  # 0부터 시작하는 value 값을 증위순회하며 저장한다.
    in_order(index * 2 + 1)


t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    complete_binary_tree = [None for _ in range(n + 1)]

    value = 0
    in_order(1)  # 루트노드부터 시작.

    print(f"#{test_case} {complete_binary_tree[1]} {complete_binary_tree[n // 2]}")
