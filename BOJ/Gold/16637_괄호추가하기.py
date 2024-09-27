# 20240927
# 23:28
# 1 / 2

# eval() 함수를 쓰고 싶었음. (근데 괄호 우선순위가 아니라서, 무의미해짐...)
# n이 1일 때, 고려 안 해서 틀렸음.


# 괄호 씌워서 계산할 연산자 index가 담긴 gwalho_arr 배열을 바탕으로
# 그대로 괄호 씌우고 계산해서, 최대값 갱신하는 함수
def cal_max():

    # 1. new_sick(괄호 씌운 새 식) 만들기
    new_sick = ''
    idx = 1  # 연산자 index 체크
    before_used = False  # 바로 이전 연산자에서 괄호 씌웠는지 체크

    while idx < n:
        # 괄호 씌울 연산자라면
        if idx in gwalho_arr:  # (예시) "(8+7)" 추가하기
            new_sick += '(' + sick[idx - 1:idx + 2] + ')'
            before_used = True
        # 괄호 안 씌울 연산자라면
        else:
            if before_used:  # 이전에 괄호 씌웠다면, (예시) "+7" 추가하기
                new_sick += sick[idx:idx + 1]
            else:            # 이전에 괄호 안 씌웠다면, (예시) "8+7" 추가하기
                new_sick += sick[idx - 1:idx + 1]
            before_used = False

            # 마지막 연산자라면 마지막 숫자 추가하고 종료
            if idx == n - 2:
                new_sick += sick[-1]
                break

        idx += 2  # 다음 연산자 index로 이동

    # 2. 괄호 씌운 새 식, 차례로 계산
    if new_sick[0] == '(':  # 시작부터 괄호 연산인 경우
        result = eval(new_sick[:5])
        new_sick = new_sick[5:]
    else:                   # 시작이 괄호 연산이 아닌 경우
        result = eval(new_sick[:1])
        new_sick = new_sick[1:]

    while new_sick:  # 나머지 식도 마저 계산
        if new_sick[1] == '(':
            result = eval(str(result) + new_sick[0] + str(eval(new_sick[2:5])))
            new_sick = new_sick[6:]
        else:
            result = eval(str(result) + new_sick[:2])
            new_sick = new_sick[2:]

    # 최대값 갱신
    global max_answer
    max_answer = max(max_answer, result)


def dfs(idx):
    # 괄호처리할 연산자index 다 골랐다면, 식 계산하기
    if idx == n:
        cal_max()
        return

    dfs(idx + 2)

    # 바로 이전의 연산자에서 괄호 씌웠다면, 연달아서 괄호 못 씌움
    if not gwalho_arr or gwalho_arr[-1] + 2 != idx:
        gwalho_arr.append(idx)
        dfs(idx + 2)
        gwalho_arr.pop()


n = int(input())
sick = str(input())

if n == 1:  # 연산자 안 들어오는 경우
    print(int(sick))
else:       # 연산자 들어오는 경우
    max_answer = -(2**31)  # 무조건 갱신되는 최대값

    # DFS 함수 호출
    gwalho_arr = []  # 괄호로 씌워서 연산할 연산자의 index 배열
    dfs(1)

    print(max_answer)  # 최대값 출력
