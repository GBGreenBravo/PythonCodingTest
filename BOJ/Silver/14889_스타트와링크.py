# 20240808
# 18:54
# 1 / 1


def check(arr1):  # 0을 포함하는 arr1 팀을 받아, arr2 팀을 생성하고, 두 팀의 능력치 차와 mn을 비교하여 갱신하는 함수
    sm1 = 0  # arr1 팀의 능력치 합
    for i in range(half_n - 1):
        for j in range(i + 1, half_n):
            ability_i, ability_j = arr1[i], arr1[j]
            sm1 += abilities[ability_i][ability_j]
            sm1 += abilities[ability_j][ability_i]

    arr2 = list(set(range(n)) - set(arr1))  # 전체 멤버에서 arr1 팀의 멤버를 빼주면 arr2가 정해짐.
    sm2 = 0  # arr2 팀의 능력치 합
    for i in range(half_n - 1):
        for j in range(i + 1, half_n):
            ability_i, ability_j = arr2[i], arr2[j]
            sm2 += abilities[ability_i][ability_j]
            sm2 += abilities[ability_j][ability_i]

    global mn
    mn = min(mn, abs(sm1 - sm2))  # mn 갱신


def dfs(arr, cnt, start):  # 팀 구성원 배열, 팀 구성원 수, 현재 함수에서 순회 시작할 index
    if cnt == half_n:  # 팀이 구성되면 능력치 계산해보기
        check(arr)
        return

    for i in range(start, n):
        dfs(arr + [i], cnt + 1, i + 1)


n = int(input())
half_n = n // 2  # 한 팀의 멤버 수
abilities = [list(map(int, input().split())) for _ in range(n)]
mn = sum(map(sum, abilities))  # 임의의 최소값 설정
dfs([0], 1, 1)  # 0을 포함하는 half_n개의 원소로 이뤄진 조합만 체크해주면, 0 미포함은 중복이므로 계산할 필요 없음.
print(mn)
