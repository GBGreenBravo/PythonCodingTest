# 20240729
# 12:30

n = int(input())
num_lst = [int(input()) for _ in range(n)]

stk = []
end = 0
result = []
possible = True

for num in num_lst:
    while True:
        if end < num:
            stk.append(end + 1)
            result.append('+')
            end += 1
        elif stk and stk[-1] == num:
            stk.pop()
            result.append("-")
            break
        elif end > num:
            possible = False
            break
    if not possible:
        break
if possible:
    print(*result, sep="\n")
else:
    print("NO")

