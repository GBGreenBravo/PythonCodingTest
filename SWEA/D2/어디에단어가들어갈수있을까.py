# 20240724
# 11:39

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    contis = []
    for i in range(n):
        conti = 0
        for j in range(n):
            if puzzle[i][j] == 1:
                conti += 1
            else:
                contis.append(conti)
                conti = 0
        contis.append(conti)
    for i in range(n):
        conti = 0
        for j in range(n):
            if puzzle[j][i] == 1:
                conti += 1
            else:
                contis.append(conti)
                conti = 0
        contis.append(conti)

    print(f"#{test_case} {contis.count(k)}")
