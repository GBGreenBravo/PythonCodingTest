# 20240930
# 11:21
# 1 / 2

# 15686_치킨배달

"""
풀이 시간: 11분 (16:14 - 16:25)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (16:14 - 16:18)


2. 구현 (16:18 - 16:23)
    이전 구현과 비교하면, (풀이 방식은 같으나) 더 깔끔한 코드가 완성됐습니다.
    코드가 깔끔한 것보다 정확한 게 중요하지만, 깔끔한 코드가 검증도 더 편하고 쉽다는 것을 알기에,
    본시험에서 시간이 난다면, 차분한 리팩토링을 통해 더욱 깔끔한 코드를 지향할 것입니다.


3. 디버깅 (-)


4. 시간초과 (16:24 - 16:25)
    dfs에서 idx를 써야할 걸, 함수 입력값인 start_idx로 써서 시간초과 났습니다.
    dfs함수에서 변수로 i를 쓰면 전역 변수와 겹치기에, 최근에 idx를 쓰기로 바꿨는데,
    이러한 사소한 변경에서 비롯된 실수였습니다.
    이번 주 내로 코드 스타일과 템플릿을 더욱 확고히 해야겠습니다.
"""


def dfs(cnt, start_idx):
    global min_answer

    if cnt == m:
        now_answer = 0

        for py, px in people:
            shortest = n**2
            for hy, hx in dfs_arr:
                shortest = min(shortest, abs(py - hy) + abs(px - hx))
            now_answer += shortest

        min_answer = min(min_answer, now_answer)
        return

    for idx in range(start_idx, len_hospitals):
        dfs_arr.append(hospitals[idx])
        dfs(cnt + 1, idx + 1)
        dfs_arr.pop()


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

people = []
hospitals = []
for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            people.append((i, j))
        elif area[i][j] == 2:
            hospitals.append((i, j))
len_hospitals = len(hospitals)

min_answer = len(people) * n**2
dfs_arr = []
dfs(0, 0)
print(min_answer)
