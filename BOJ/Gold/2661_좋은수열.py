# 20240809
# 17:18
# 1 / 1

# if arr[-1:] == arr[-2:-1]:
# if arr[-2:] == arr[-4:-2]:
# if arr[-3:] == arr[-6:-3]:
# if arr[-4:] == arr[-7:-4]:
# 위와 같이 직접 규칙 체크하면서 뒤에셔 비교하는 슬라이싱의 전자 인덱스가 범위 안일 때까지를 확인했음.


def dfs(cnt):
    global find_answer
    if find_answer:  # 정답 찾았으면 다른 좋은수열 출력하지 않게, return
        return

    # 중복 검사
    i = 1
    while len(arr) > 1 and -1-(i*2) >= -n-1:
        if arr[-i:] == arr[-(i*2):-i]:
            return
        i += 1

    if cnt == n:  # 가장 작은 좋은수열 찾았으면 출력하고 return
        print(*arr, sep="")
        find_answer = True
        return

    for i in range(1, 4):  # DFS
        arr.append(i)
        dfs(cnt + 1)
        arr.pop()


n = int(input())
arr = []
find_answer = False
dfs(0)


# flag 사용하지 않고, 아래와 같이 exit() 사용해도 됨.
"""
def dfs(cnt):
    i = 1
    while len(arr) > 1 and -1-(i*2) >= -n-1:
        if arr[-i:] == arr[-(i*2):-i]:
            return
        i += 1

    if cnt == n:
        print(*arr, sep="")
        exit()

    for i in range(1, 4):
        arr.append(i)
        dfs(cnt + 1)
        arr.pop()


n = int(input())
arr = []
dfs(0)
"""