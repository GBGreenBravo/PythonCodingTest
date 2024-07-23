# 20240723
# 35:30

# 지그재그의 각 라인의 최대값을 구하면 [1, 3, 6, 10, 15, 21, ...] 처럼 계차수열임을 확인
# 이 리스트의 인덱스는 각 지그재그의 합과 동일함.
# 그렇기 때문에 리스트의 각 값은 지그재그의 최대값이 되므로, x의 값이 해당 지그재그에 포함돼 있다면 멈추고
# 해당 인덱스의 합의 조합이 되는 것을 (0, 합) 으로 시작하여 순서를 찾아감.
# 지그재그 방향 거꾸로인 건 수 바꿔주면 됨.

x = int(input())

target_num = []
now = 1
plus_value = 1
while now <= 20_000_000:
    target_num.append(now)
    plus_value += 1
    now += plus_value

for i in range(len(target_num)):
    if x == 1:
        print("1/1")
        break
    elif x <= target_num[i]:
        a, b = 0, i
        start = target_num[i - 1] + 1
        while start != x:
            a += 1
            b -= 1
            start += 1
        if i % 2 == 0:
            a, b = b, a
        print(f"{a + 1}/{b + 1}")
        break
