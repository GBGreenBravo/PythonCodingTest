# 20240729
# 08:24

T = int(input())
for test_case in range(1, T + 1):
    code = str(input())
    stk = []
    result = 1
    for s in code:
        if s == '(':
            stk.append(s)
        elif s == '{':
            stk.append(s)
        elif s == ')':
            if not stk or stk[-1] == '{':
                result = 0
                break
            elif stk[-1] == '(':
                del stk[-1]
        elif s == '}':
            if not stk or stk[-1] == '(':
                result = 0
                break
            elif stk[-1] == '{':
                del stk[-1]
    if stk:
        result = 0
    print(f"#{test_case} {result}")


# openB, closeB = ('(', '{'), (')', '}') 활용하여 중복 코드 아래와 같이 줄임.
"""
T = int(input())
for test_case in range(1, T + 1):
    code = str(input())
    stk = []
    openB, closeB = ('(', '{'), (')', '}')
    result = 1
    for s in code:
        if s in openB:
            stk.append(s)
        elif s in closeB:
            if not stk or stk[-1] == openB[closeB.index(s) - 1]:
                result = 0
                break
            elif stk[-1] == openB[closeB.index(s)]:
                del stk[-1]
    else:
        if stk:
            result = 0
    print(f"#{test_case} {result}")
"""