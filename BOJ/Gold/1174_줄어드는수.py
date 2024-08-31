# 20240815
# 1:11:29
# 1 / 3

n = int(input())

downs = [-1] * 1_000_001
for i in range(1, 12):
    downs[i] = i - 1
for i in range(12, 1_000_001):
    before = [int(j) for j in str(downs[i - 1])]

    if downs[i - 1] == 9876543210:
        break

    len_before = len(before)
    for j in range(len_before - 1):
        idx = len_before - 1 - j
        new = (before[idx] + 1) % 10

        if idx == len_before - 1:
            if before[-2] > new:
                before[-1] += 1
                break
        else:
            if before[idx - 1] > new > before[idx + 1]:
                before[idx] += 1
                before[-1] = 0
                for nidx in range(len_before - 2, idx, -1):
                    before[nidx] = before[nidx + 1] + 1
                break
    else:
        before_first = before[0]
        if before_first == 9:
            before = list(range(len_before, -1, -1))
        else:
            before = [len_before - 1 - i for i in range(len_before)]
            before[0] = before_first + 1

    downs[i] = int(''.join([str(j) for j in before]))

print(downs[n])
