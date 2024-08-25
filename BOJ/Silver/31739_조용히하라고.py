# 20240825
# 57:35
# 1 / 3


def dfs(cnt, distance, visited):
    global mx_death_cnt

    if mx_death_cnt == k:
        return

    if distance > t:
        return

    mx_death_cnt = max(mx_death_cnt, cnt)

    for i in range(k):
        if i in visited:
            continue
        addtional_distance = abs(mosquitoes[visited[-1]][0] - mosquitoes[i][0]) + abs(mosquitoes[visited[-1]][1] - mosquitoes[i][1])
        dfs(cnt + 1, distance + addtional_distance, visited + [i])


# 상하좌우로 이동하는 dfs로 할 수도 있지만, 우정이의 체력 최대값이 10**9로 너무 큼.
# 반면 모기의 최대값은 10으로 비교적 적기 때문에, 순열로 배치하며 해당 순서로 방문하는 거리를 체크하는 백트래킹을 구현하면 됨.
def first_solution():  # 태극 모기장
    global mx_death_cnt
    mx_death_cnt = 0

    for i in range(k):
        dfs(1, 0, [i])

    return mx_death_cnt


def second_solution():  # 태극 전기장
    mx_death_cnt = 0

    for i in range(n):
        for j in range(m):
            death_cnt = 0
            for my, mx, life in mosquitoes:
                if my == i and mx == j:
                    death_cnt += 1
                    continue
                if p / (abs(my - i) + abs(mx - j)) >= life:
                    death_cnt += 1

            mx_death_cnt = max(mx_death_cnt, death_cnt)
            if mx_death_cnt == k:
                return k

    return mx_death_cnt


n, m, k, t, p = map(int, input().split())
mosquitoes = [tuple(map(int, input().split())) for _ in range(k)]
mosquitoes = [(my - 1, mx - 1, ml) for my, mx, ml in mosquitoes]  # 입력의 좌표를 0번 인덱스부터 시작하도록, 조정

print(first_solution(), second_solution())
