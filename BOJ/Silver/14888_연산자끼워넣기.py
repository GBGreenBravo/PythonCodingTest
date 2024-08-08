# 20240808
# 17:40
# 1 / 1


def dfs(operand_lst, opcode_lst):
    if len(operand_lst) == 1:  # 종료 조건: 연산자 모두 사용되어서 operand가 1개만 남았다면
        value = operand_lst[0]

        global mx, mn  # 최대값, 최소값 갱신
        mx = max(mx, value)
        mn = min(mn, value)

    for i in range(4):  # 0 1 2 3 에 대해서
        if opcode_lst[i]:  # + - * / 에 대해서
            opcode_lst[i] -= 1  # 해당 연산자가 아직 남아있다면
            dfs(opcode_dict[i](*operand_lst[:2]) + operand_lst[2:], opcode_lst)
            opcode_lst[i] += 1


# dictionary key는 "0 1 2 3" -> value는 "+ - * /" 에 따른 연산 결과값을 리스트에 담아 반환하는 함수
opcode_dict = {0: lambda a, b: [a + b], 1: lambda a, b: [a - b], 2: lambda a, b: [a * b], 3: lambda a, b: [int(a / b)]}

n = int(input())
operands = list(map(int, input().split()))
opcodes = list(map(int, input().split()))

mx, mn = -1_000_000_000, 1_000_000_000  # 최대값, 최소값 임의의 값으로 선언
dfs(operands, opcodes)
print(mx, mn, sep="\n")


# dfs()의 인자로 리스트가 아닌, 연산자 인덱스와 계산값을 가진다면 아래와 같은 풀이. (시간/메모리 차이는 거의 없음)
"""
def dfs(back_operand_index, cal_result):
    if back_operand_index == n:  # 종료 조건: 뒤 연산자의 인덱스가 n이라면 (범위 밖)
        global mx, mn  # 최대값, 최소값 갱신
        mx = max(mx, cal_result)
        mn = min(mn, cal_result)

    for i in range(4):  # 0 1 2 3 에 대해서
        if opcodes[i]:  # + - * / 에 대해서 해당 연산자가 아직 남아있다면
            opcodes[i] -= 1
            dfs(back_operand_index + 1, opcode_dict[i](cal_result, operands[back_operand_index]))
            opcodes[i] += 1


# dictionary key는 "0 1 2 3" -> value는 "+ - * /" 에 따른 연산 결과값 반환하는 함수
opcode_dict = {0: lambda a, b: a + b, 1: lambda a, b: a - b, 2: lambda a, b: a * b, 3: lambda a, b: int(a / b)}

n = int(input())
operands = list(map(int, input().split()))
opcodes = list(map(int, input().split()))

mx, mn = -1_000_000_000, 1_000_000_000  # 최대값, 최소값 임의의 값으로 선언
dfs(1, operands[0])
print(mx, mn, sep="\n")
"""