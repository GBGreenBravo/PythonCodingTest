# 20240725
# 08:42

def rotate(array):
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = array[i][j]
    return rotated


T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr_0 = [list(map(int, input().split())) for _ in range(n)]
    arr_90 = rotate(arr_0)
    arr_180 = rotate(arr_90)

    arr_270 = rotate(arr_180)

    print(f"#{test_case}")
    for i in range(n):
        for ar in [arr_90, arr_180, arr_270]:
            print(*ar[i], sep="", end=" ")
        print()

# 인덱스 변환 말고 zip()활용해서 회전시킬 수도 있음.
"""
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr_0 = [list(map(int, input().split())) for _ in range(n)]
    arr_90 = list(list(r[::-1]) for r in zip(*arr_0))
    arr_180 = list(list(r[::-1]) for r in zip(*arr_90))
    arr_270 = list(list(r[::-1]) for r in zip(*arr_180))

    print(f"#{test_case}")
    for i in range(n):
        for ar in [arr_90, arr_180, arr_270]:
            print(*ar[i], sep="", end=" ")
        print()
"""