# 20241011
# 09:58
# 1 / 1

convert = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
           "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

t = int(input())
for test in range(1, t + 1):
    n, k = map(int, input().split())
    numbers = list(str(input()))

    numbers_set = set()

    for _ in range(n // 4):
        for i in range(0, n, n // 4):
            split = numbers[i:i + n // 4]
            new_number = 0
            for j in range(len(split) - 1, -1, -1):
                new_number += 16**j * convert[split[len(split) - 1 - j]]
            numbers_set.add(new_number)

        numbers = [numbers[-1]] + numbers[:-1]

    print(f"#{test} {sorted(list(numbers_set), reverse=True)[k - 1]}")
