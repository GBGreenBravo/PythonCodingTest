# 20240722

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    m = str(input())
    max = 0
    now = 0
    for i in m:
        if i == "0":
            now = 0
        else:
            now += 1
            if max < now:
                max = now
    print(f"#{test_case} {max}")