# 20240805
# 33:52
# 1 / 1

def in_order(index):  # 중위순환
    if index > n:
        return

    if not connected[index]:  # 자식노드라면 정수 그대로 반환
        return int(binary_tree[index])

    # 자식노드가 있는 노드라면, 연산자로 계산한 결과 반환
    left = in_order(connected[index][0])
    right = in_order(connected[index][1])

    if binary_tree[index] == '+':
        return left + right
    elif binary_tree[index] == '-':
        return left - right
    elif binary_tree[index] == '*':
        return left * right
    elif binary_tree[index] == '/':
        return left / right


for test_case in range(1, 11):
    n = int(input())
    binary_tree = [None for _ in range(n + 1)]
    connected = [[] for _ in range(n + 1)]  # 완전이진트리가 아니므로, 자식노드 정보 저장할 리스트
    for _ in range(n):
        info = list(map(str, input().split()))
        binary_tree[int(info[0])] = info[1]  # 이진트리에 정보 저장
        if len(info) > 2:  # 자식노드 있다면, 자식노드 정보를 connected에 저장
            connected[int(info[0])].append(int(info[2]))
            connected[int(info[0])].append(int(info[3]))

    answer = int(in_order(1))

    print(f"#{test_case} {answer}")


# 아래는 exec() 함수 이용하여 풀었지만, 해당 함수 제한돼서 위 코드로 바꿈.
"""
def in_order(index):
    global expression

    if index > n:
        return

    if connected[index]:
        expression += '('
        in_order(connected[index][0])
        expression += complete_binary_tree[index]
        in_order(connected[index][1])
        expression += ')'
    else:
        expression += complete_binary_tree[index]


for test_case in range(1, 11):
    n = int(input())
    complete_binary_tree = [None for _ in range(n + 1)]
    connected = [[] for _ in range(n + 1)]
    for _ in range(n):
        info = list(map(str, input().split()))
        complete_binary_tree[int(info[0])] = info[1]
        if len(info) > 2:
            connected[int(info[0])].append(int(info[2]))
            connected[int(info[0])].append(int(info[3]))

    expression = ""
    in_order(1)
    expression = 'print(int' + expression + ')'

    print(f"#{test_case}", end=" ")
    exec(expression)
"""