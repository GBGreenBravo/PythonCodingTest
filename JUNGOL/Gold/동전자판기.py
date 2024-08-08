# 20240808
# 33:00
# 1 / 1

w = int(input())
first_coins = list(map(int, input().split()))  # 사용가능한 최대 동전 배열

used_coins = [0] * 6  # 사용되는 동전을 저장할 배열
index_to_money = {0: 500, 1: 100, 2: 50, 3: 10, 4: 5, 5: 1}  # 인덱스를 돈으로 바꾸는 딕셔너리

now_money = 0  # 반복문에서 만들 돈
while now_money != w:  # 만들어진 돈이 목표치와 같으면 종료
    if now_money < w:  # 현재 돈이 목표치보다 작으면 (작은돈부터 쓰는 게 좋음)
        for i in range(5, -1, -1):  # 1원부터
            if first_coins[i] - used_coins[i] > 0:  # 사용가능한 동전 수가 남아있다면 사용
                now_money += index_to_money[i]
                used_coins[i] += 1
                break

    else:  # 현재 돈이 목표치보다 많으면 (큰돈부터 빼는 게 좋음)
        will_be_used = None
        for i in range(5, -1, -1):  # 1원부터
            if used_coins[i] > 0 and now_money - index_to_money[i] >= w:  # 사용된 동전이고, 이 동전을 빼도 목표치보다 크거나 같으면
                will_be_used = i

        now_money -= index_to_money[will_be_used]  # 빼도 되는 동전 중에 가장 큰 돈을 쓴다.
        used_coins[will_be_used] -= 1

print(sum(used_coins))
print(*used_coins)
