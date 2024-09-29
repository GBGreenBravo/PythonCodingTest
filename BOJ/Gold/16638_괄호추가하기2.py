# 20240929
# 16:30
# 1 / 2

# n이 1일 때, 고려 안 해서 틀렸음.


def check():
    new_expression = ''
    before_used = False

    idx = 1
    while idx < n:
        if idx in dfs_arr:
            new_expression += '(' + expression[idx - 1:idx + 2] + ')'
            before_used = True
        else:
            if before_used:
                new_expression += expression[idx]
            else:
                new_expression += expression[idx - 1:idx + 1]
            before_used = False

            if idx == n - 2:
                new_expression += expression[-1]
        idx += 2

    global max_answer
    max_answer = max(max_answer, eval(new_expression))


def dfs(start_idx):
    if start_idx == n:
        check()
        return

    dfs(start_idx + 2)
    if not dfs_arr or dfs_arr[-1] + 2 != start_idx:
        dfs_arr.append(start_idx)
        dfs(start_idx + 2)
        dfs_arr.pop()


n = int(input())
expression = str(input())

if n == 1:
    print(expression)
else:
    max_answer = -(2**31)
    dfs_arr = []
    dfs(1)
    print(max_answer)
