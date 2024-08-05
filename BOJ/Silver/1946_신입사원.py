# 20240805
# 17:46
# 1 / 2

t = int(input())
for _ in range(t):
    n = int(input())
    scores = [tuple(map(int, input().split())) for _ in range(n)]

    scores.sort(key=lambda x: (x[0], x[1]))  # 0번 인덱스 성적 기준으로 정렬.

    best_1 = scores[0][1]
    answer = n
    for i in range(1, n):  # 0번 인덱스는 성적 높은 순대로 정렬 돼있기 때문에, 1번 인덱스 성적만 봐주면 됨.
        if scores[i][1] > best_1:  # 현재의 1번 인덱스 성적이 이전의 1번 인덱스 최고 성적보다 낮으면, 탈락
            answer -= 1
        else:
            best_1 = scores[i][1]  # 현재의 1번 인덱스 성적이 이전의 1번 인덱스 최고 성적보다 높으면, 갱신

    print(answer)



