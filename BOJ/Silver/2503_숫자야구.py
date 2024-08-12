# 20240812
# 17:54
# 1 / 1

"""
1. 문제 분석
- DFS, BruteForce
- DFS로 만들어진 숫자의 조합에 대해, Q&A의 스트라이크/볼 기준을 모두 만족하는 경우의 수를 출력

2. 설계
- dfs()로 arr에 중복없이 숫자를 저장하며, 3개의 숫자가 조합되면, 해당 조합을 기준으로 Q&A 부합 여부를 체크한다.
- Q&A에서 질의한 숫자조합과 비교하며 스트라이크/볼 기준을 검토한다.

3. 구현
- check()함수에서 1,2,3번째 수에 대한 검증을 해줬는데, 해당 코드를 하드코딩으로 3개 각각을 비교해줬다.
- 3개의 수로 제한돼있기에, 별도의 루프로 만들거나 함수화할 필요는 없다고 생각했다.

4. 검증
- DFS를 활용하는 것도 좋지만, 더 간편하게는 range(123, 988)에서 중복만 continue해줘도 괜찮을 듯함.
"""


def check():  # 현재 조합이 Q&A의 스트라이크/볼 기준에 부합하는지 체크하는 함수
    one, two, three = num_arr[0], num_arr[1], num_arr[2]  # 생성된 조합의 3개의 수

    for qna in qnas:
        strike, ball = 0, 0
        c1, c2, c3 = map(int, str(qna[0]))  # qna에서 질문한 3개의 수

        if one == c1:  # 첫번째 수가 동일하면, strike += 1
            strike += 1
        elif one in [c2, c3]:  # 첫번째 수가 2,3번째에 있으면 ball += 1
            ball += 1
        if two == c2:
            strike += 1
        elif two in [c1, c3]:
            ball += 1
        if three == c3:
            strike += 1
        elif three in [c1, c2]:
            ball += 1

        if strike != qna[1] or ball != qna[2]:  # strike, ball 응답에 부합하지 않으면 return False
            return False

    return True  # Q&A에 모두 부합하면 return True


def dfs(cnt):
    if cnt == 3:  # 3개의 수가 조합되면, chec()해보고 True를 반환하면 answer_cnt += 1
        if check():
            global answer_cnt
            answer_cnt += 1
        return

    for i in range(1, 10):  # 1부터 9에 대해 중복 제외하고 DFS
        if i in num_arr:
            continue
        num_arr.append(i)
        dfs(cnt + 1)
        num_arr.pop()


n = int(input())
qnas = [list(map(int, input().split())) for _ in range(n)]
num_arr = []  # DFS에서 생성되는 3개의 숫자
answer_cnt = 0  # 가능한 경우의 수
dfs(0)

print(answer_cnt)
