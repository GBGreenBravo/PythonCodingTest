for test_case in range(1, 11):
    width = int(input())
    buildings = list(map(int, input().split()))

    result = 0

    for i in range(2, len(buildings) - 2):

        diff = buildings[i] - max(buildings[i - 2: i] + buildings[i + 1: i + 3])
        if diff > 0:
            result += diff

    print(f"#{test_case} {result}")
