def cal(num):
    return int(((y + num) / (x + num)) * 100)


x, y = map(int, input().split())

if x == y or cal(0) >= 99:
    print(-1)
else:
    now = cal(0)

    start = 0
    # end = 1_000_000_000 ** 2
    end = int(x ** 2 / (99 * x - 100 * y)) + 1
    while end - start > 0:
        middle = (start + end) // 2

        cal_middle = cal(middle)

        if cal_middle == now:
            start = middle + 1
        elif cal_middle > now:
            end = middle

    print(start)

# 1:54:09

