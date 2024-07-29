# 20240729
# 15:07

n = int(input())
skyline = []
for i in range(n):
    idx, height = map(int, input().split())
    skyline.append(height)
skyline.insert(0, 0)
skyline.append(0)

stk = [0]
answer = 0
for h in skyline:
    if stk[-1] < h:
        stk.append(h)
    elif h < stk[-1]:
        while stk and stk[-1] > h:
            stk.pop()
            answer += 1
        else:
            if h not in stk:
                stk.append(h)
print(answer)