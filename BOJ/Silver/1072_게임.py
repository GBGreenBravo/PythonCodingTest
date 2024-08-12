# 20240812
# 1:54:09
# 25:48
# 1 / 14


# y = 29, x = 50 면
# int(y / x * 100) 에서는 57 반환하고
# 100 * y // x 에서는 58 반환한다.
# 부동소수점으로 인한 알려진 에러. 따라서 이러한 경우에는 정수끼리 계산한 아래의 방식을 활용하는 게 정확하다.

def cal(num):
    return 100 * (y + num) // (x + num)  # 이 부분을 return int((y + num) / (x + num) * 100)으로 작성했어서 틀림.


x, y = map(int, input().split())
now = cal(0)

if now >= 99:
    print(-1)
else:
    left = 0
    right = x ** 2
    while left < right:
        middle = int((left + right) // 2)
        cal_middle = cal(middle)

        if cal_middle <= now:
            left = middle + 1
        elif cal_middle > now:
            right = middle

    print(left)
