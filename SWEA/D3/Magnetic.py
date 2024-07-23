# 20240722
# 27:24

T = 10
for test_case in range(1, T + 1):
    length = int(input())
    table = []
    for i in range(length):
        table.append(list(map(int, input().split())))

    for i in range(length):
        for j in range(length):
            if table[j][i] == 1:
                break
            elif table[j][i] == 2:
                table[j][i] = 0

    for i in range(length):
        for j in range(1, length + 1):
            if table[-j][i] == 2:
                break
            elif table[-j][i] == 1:
                table[-j][i] = 0

    count = 0
    for i in range(length):
        now = 2
        for j in range(length):
            if table[j][i] in [1, 2] and table[j][i] != now:
                now = table[j][i]
                count += 1
    count //= 2

    print(f"#{test_case} {count}")
