# 20240725
# 47:17

from math import sqrt, floor

n = int(input())
numbers = list(map(int, input().split()))
print(*[1 if number == floor(sqrt(number))**2 else 0 for number in numbers], sep=" ")

# sqrt(10**18 - 1)는 왜 10**9 인가,,,,
"""
numbers = [10**18 - 1, 10**18]
print(numbers)
print([sqrt(i) for i in numbers])  
"""
# => 부동소수점의 한계라고 함.
# 따라서, sqrt(num)과 floor(sqrt(num))를 비교하면 안되고,
# num과 floor(sqrt(num))**2를 비교해야 한다.
