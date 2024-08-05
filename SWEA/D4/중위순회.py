# 20240805
# 1 / 1


def in_order_print(index):  # 중위순회하며 print
    if index > n:
        return
    in_order_print(index * 2)
    print(complete_binary_tree[index], end="")
    in_order_print(index * 2 + 1)


for test_case in range(10):
    n = int(input())
    complete_binary_tree = [None for _ in range(n + 1)]
    for _ in range(n):
        info = list(map(str, input().split()))
        complete_binary_tree[int(info[0])] = info[1]  # 입력값의 인덱스의 완전이진트리 리스트에 문자열 저장.

    print(f"#{test_case + 1}", end=" ")
    in_order_print(1)
    print()
