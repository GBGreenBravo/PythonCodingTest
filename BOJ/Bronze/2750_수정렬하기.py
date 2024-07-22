# 20240722
# 03:17

n = int(input())
lst = [int(input())]

for i in range(n - 1):
    num = int(input())
    for j in range(len(lst)):
        if num < lst[j]:
            lst.insert(j, num)
            break
    else:
        lst.append(num)

for i in lst:
    print(i)
