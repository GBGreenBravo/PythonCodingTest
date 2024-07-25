# 20240725
# 15:45

for _ in range(10):
    test_case = int(input())
    mp = [list(map(int, input().split())) for _ in range(100)]

    before = (-1, -1)
    now = (99, mp[99].index(2))
    while now[0] != 0:
        left = (now[0], now[1] - 1)
        right = (now[0], now[1] + 1)
        up = (now[0] - 1, now[1])

        if now[1] != 0 and mp[left[0]][left[1]] == 1 and left != before:
            before, now = now, left
            continue
        if now[1] != 99 and mp[right[0]][right[1]] == 1 and right != before:
            before, now = now, right
            continue
        before, now = now, up

    print(f"#{test_case} {now[1]}")




