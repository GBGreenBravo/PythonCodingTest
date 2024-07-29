# 20240729
# 12:42

T = int(input())
for test_case in range(1, T + 1):
    brackets = list(str(input()))
    sm = 0

    lower_height = 0
    now_height = 0
    i = 0
    while i < len(brackets) - 1:
        if brackets[i] + brackets[i + 1] == '()':
            sm += now_height - lower_height
            sm += now_height
            i += 1
            lower_height = now_height
        elif brackets[i] == '(':
            now_height += 1
        elif brackets[i] == ')':
            lower_height -= 1
            now_height -= 1
        i += 1

    print(f"#{test_case} {sm}")