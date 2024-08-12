# 20240813
# 12:43
# 1 / 1


def dfs(num_str, odd_cnt):
    for n in num_str:  # 현재 들어온 num_str의 자리수에서 홀수 카운트
        if n in '13579':
            odd_cnt += 1

    if len(num_str) == 1:  # 길이가 1이면 끝이므로, 결과값 results에 저장
        results.append(odd_cnt)
        return
    if len(num_str) == 2:  # 길이가 2면, 2개로 나눠서 재귀
        dfs(str(int(num_str[0]) + int(num_str[1])), odd_cnt)
    if len(num_str) >= 3:  # 길이가 3이면, 가능한 모든 3개의 분리로 재귀
        for first_cut in range(1, len(num_str) - 1):
            for second_cut in range(first_cut + 1, len(num_str)):
                dfs(str(int(num_str[:first_cut]) + int(num_str[first_cut:second_cut]) + int(num_str[second_cut:])), odd_cnt)


num = str(input())
results = []
dfs(num, 0)
print(min(results), max(results))
