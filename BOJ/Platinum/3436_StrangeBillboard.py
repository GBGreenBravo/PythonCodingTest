# 20241230
# 17:40
# 1 / 1


def check(first_row):
    global answer

    now_answer = 0

    if R == 1:
        now_row = [c for c in area[0]]
        c = 0
        while first_row:
            if first_row & 1:
                now_answer += 1
                if c:
                    now_row[c - 1] ^= 1
                now_row[c] ^= 1
                if c != C - 1:
                    now_row[c + 1] ^= 1
            first_row >>= 1
            c += 1
        if not sum(now_row):
            answer = min(answer, now_answer)

        return

    before_row = [c for c in area[0]]
    now_row = [c for c in area[1]]

    c = 0
    while first_row:
        if first_row & 1:
            now_answer += 1
            if c:
                before_row[c - 1] ^= 1
            before_row[c] ^= 1
            if c != C - 1:
                before_row[c + 1] ^= 1
            now_row[c] ^= 1
        first_row >>= 1
        c += 1

    for r in range(1, R - 1):
        next_row = [c for c in area[r + 1]]
        for c in range(C):
            if before_row[c]:
                now_answer += 1
                if c:
                    now_row[c - 1] ^= 1
                now_row[c] ^= 1
                if c != C - 1:
                    now_row[c + 1] ^= 1
                next_row[c] ^= 1

        before_row, now_row = now_row, next_row

    for c in range(C):
        if before_row[c]:
            now_answer += 1
            if c:
                now_row[c - 1] ^= 1
            now_row[c] ^= 1
            if c != C - 1:
                now_row[c + 1] ^= 1

    if not sum(now_row):
        answer = min(answer, now_answer)

    return


while True:
    R, C = map(int, input().split())
    if not R:
        break

    area = [[int(i == 'X') for i in str(input())] for _ in range(R)]

    answer = R * C + 1
    for i in range(2 ** C):
        check(i)

    if answer == R * C + 1:
        print("Damaged billboard.")
    else:
        print(f"You have to tap {answer} tiles.")

    input()
