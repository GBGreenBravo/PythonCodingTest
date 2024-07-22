# 20240722
# 19:51

# a * days + b * days + a >= v 를 만족시키는 days의 최소값 + 1 을 구해야 한다.
# days만을 좌변에 남기면, days >= (v - a) / (a - b) 가 된다.
# 우변의 값을 올림하고난 후 + 1을 해주면 답이 도출됨.

from math import ceil

a, b, v = map(int, input().split())
value = ceil((v - a) / (a - b))
print(value + 1)
