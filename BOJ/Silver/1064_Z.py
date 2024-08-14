# 20240814
# 48:09
# 1 / 1

twos = [2 ** i for i in range(16)]


def recur(y, x):
    if not y and not x:
        return

    global answer

    if y >= x:
        mx_y = max([i for i in twos if y - i >= 0])
        answer += mx_y ** 2 * 2
        return recur(y - mx_y, x)

    elif y < x:
        mx_x = max([i for i in twos if x - i >= 0])
        answer += mx_x ** 2
        return recur(y, x - mx_x)


n, r, c = map(int, input().split())
answer = 0
recur(r, c)
print(answer)
