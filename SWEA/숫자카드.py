# 20240722

T = int(input())

for test_case in range(1, T + 1):
    arr = [0] * 10
    n = int(input())
    numbers = str(input())
    for i in numbers:
        arr[int(i)] += 1

    max_number = abs(arr[::-1].index(max(arr)) - 9)

    print(f"#{test_case} {max_number} {max(arr)}")