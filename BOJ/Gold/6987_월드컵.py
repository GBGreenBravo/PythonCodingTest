# 20240818
# 2:00:32
# 1 / 2


def dfs(cnt):
    if cnt == 15:
        combinations.add(tuple(sorted([tuple(i) for i in logs])))  # 조합 완성됐다면 나라별 승무패 combinations에 추가
        return

    if logs[0][0] > logs[0][2] or logs[-1][0] < logs[-1][2]:  # 승무패 순이므로, 첫 나라는 승이 패보다 많아서는 안되고, 마지막 나라는 패가 승보다 많아서는 안된다.
        return

    if sum(logs[0]) == sum(logs[1]) == 5:  # ㅋㅋㅋ.. 첫 번째, 두 번째 나라 완성됐고
        if logs[0] > logs[1]:  # 정렬 깨지면 return
            return
        if sum(logs[2]) == 5:  # 마찬가지로 이를 i, i + 1 나라에 대해 가지치기
            if logs[1] > logs[2]:
                return
            if sum(logs[3]) == 5:
                if logs[2] > logs[3]:
                    return
                if sum(logs[4]) == 5:
                    if logs[3] > logs[4]:
                        return
                    if sum(logs[5]) == 5:
                        if logs[4] > logs[5]:
                            return

    for i in range(3):
        match_result = ["W", "D", "L"][i]

        team_a, team_b = matches[cnt]
        if match_result == "W":
            logs[team_a][0] += 1
            logs[team_b][2] += 1
        elif match_result == "D":
            logs[team_a][1] += 1
            logs[team_b][1] += 1
        else:
            logs[team_a][2] += 1
            logs[team_b][0] += 1

        dfs(cnt + 1)

        if match_result == "W":
            logs[team_a][0] -= 1
            logs[team_b][2] -= 1
        elif match_result == "D":
            logs[team_a][1] -= 1
            logs[team_b][1] -= 1
        else:
            logs[team_a][2] -= 1
            logs[team_b][0] -= 1


matches = ((0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5))  # 6 C 2 조합
combinations = set()  # 가능한 모든 조합이 정렬되어 담기는 set
logs = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]  # 각 나라의 W, D, L이 담길 배열
dfs(0)

countries = [tuple(map(int, input().split())) for _ in range(4)]
results = []
for i in range(4):
    a1, a2, a3, b1, b2, b3, c1, c2, c3, d1, d2, d3, e1, e2, e3, f1, f2, f3 = countries[i]
    if tuple(sorted([(a1, a2, a3), (b1, b2, b3), (c1, c2, c3), (d1, d2, d3), (e1, e2, e3), (f1, f2, f3)])) in combinations:  # 입력으로 들어온 값을 정렬했을 때, 그 조합이 combinations에 존재하면
        results.append(1)
    else:
        results.append(0)
print(*results)
# print(len(combinations))
# print(sorted(combinations)[0])
# print(sorted(combinations)[-2])
# print(sorted(combinations)[-1])
# print([i for i in sorted(list(combinations)) if i[1][0] > i[1][2]])
