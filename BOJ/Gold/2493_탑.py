# 20240729
# 08:35

n = int(input())
towers = list(map(int, input().split()))
stk = []
result = []

for i in range(len(towers)):
    tower = towers[i]
    if not stk:
        result.append(0)
    else:
        while stk:
            if tower <= stk[-1][0]:
                result.append(stk[-1][1] + 1)
                break
            elif tower > stk[-1][0]:
                stk.pop()
        else:
            result.append(0)

    stk.append((tower, i))

print(*result, sep=" ")