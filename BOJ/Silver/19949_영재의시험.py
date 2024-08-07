# 20240807
# 10:22
# 1 / 1


def dfs(len, answer_cnt, before1, before2):  # 현재까지 찍은 답안 개수, 정답 맞힌 개수, 이전에 찍었던 번호, 2번 전에 찍었던 번호
    global cnt

    if 10 - len < 5 - answer_cnt:  # 조기 종료 조건: 앞으로 찍을 번호보다 맞춰야하는 정답이 더 큰 경우
        return

    if len == 10:  # 10문제 모두 찍은 경우
        if answer_cnt >= 5:  # 5점 이상이라면 cnt += 1
            cnt += 1
        return

    for i in range(1, 6):
        if before1 and before2 and before1 == before2 and before2 == i:  # 이전에 찍은 2개의 번호가 존재하고 i와 같으면 continue
            continue
        new_answer_cnt = answer_cnt + 1 if answers[len] == i else answer_cnt  # 현재 i가 len번째 문제의 정답이라면 정답 카운트 += 1
        dfs(len + 1, new_answer_cnt, i, before1)


answers = list(map(int, input().split()))
cnt = 0
dfs(0, 0, None, None)
print(cnt)
