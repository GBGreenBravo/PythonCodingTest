# 20240729
# 07:28

for t in range(1, 11):
    n, password = input().split()
    password = [int(i) for i in str(password)]

    i = 0
    while i < len(password) - 1:
        if password[i] == password[i + 1]:
            del password[i]
            del password[i]
            i = max(i - 2, -1)
        i += 1

    print(f"#{t}", end=" ")
    print(*password, sep='')
