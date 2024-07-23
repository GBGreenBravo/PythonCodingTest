# 20240723
# 07:26

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))

    profit = 0

    while prices:
        mx_price = max(prices)
        mx_price_index = prices.index(max(prices))
        for i in prices[:mx_price_index]:
            profit += mx_price - i
        prices = prices[mx_price_index + 1:]

    print(f"#{test_case} {profit}")


# 위 코드는 max(), index() 너무 자주 활용하여 루프를 많이 돌게 됨.
# 아래 코드는 O(N)만에 답변 도출 가능.
"""
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    prices = list(map(int, input().split()))

    profit = 0
    mx_price = prices[-1]
    for i in range(n - 2, -1, -1):
        if prices[i] > mx_price:
            mx_price = prices[i]
        else:
            profit += mx_price - prices[i]

    print(f"#{test_case} {profit}")
"""
