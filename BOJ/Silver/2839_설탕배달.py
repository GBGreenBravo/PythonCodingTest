# 20240721
# 08:50

n = int(input())

five = [i * 5 for i in range(0, 1001)]
three = [i * 3 for i in range(0, 1700) if i * 3 <= 5000]

five = five[::-1]


def calculate(n):
    for i in five:
        for j in three:
            if i + j > n:
                break
            if i + j == n:
                return i // 5 + j // 3
    return -1


print(calculate(n))
