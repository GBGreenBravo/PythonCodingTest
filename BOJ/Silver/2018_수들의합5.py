# 20240722
# 02:19

n = int(input())

answer = 1

for i in range(1, n + 1):
    now = i
    for j in range(i + 1, n):
        now += j
        if now > n:
            break
        elif now == n:
            answer += 1
            break

print(answer)


# 투포인터를 활용한다면 아래와 같이.
'''
n = int(input())
count = 0

start, end = 1, 1
now = 1

while end <= n:
    if now == n:
        count += 1
        now -= start
        start += 1
    elif now < n:
        end += 1
        now += end
    elif now > n:
        now -= start
        start += 1

print(count)
'''
