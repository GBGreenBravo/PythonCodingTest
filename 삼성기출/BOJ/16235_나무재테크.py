# 20240904
# 23:00
# 1 / 1

"""
풀이 시간: 23분 (16:00 ~ 16:23)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (16:00 - 16:08)
    문제를 읽으며, 거의 모든 요구사항을 메모했습니다.
    읽음과 동시에, 구상을 하는 편이기에,
    코드로 표현할 수 있는 건 코드 스타일로 적었습니다
    (ex. 여름에서 "죽은나무나이//2 만큼", 가을에서 "oob -> 나무 안 생김")

    문제의 초기 세팅을 먼저 마련해주고,
    사계절 각각의 작업에 대한 수행을 반복문으로 구현해주면 되겠다고 생각했습니다.

    그리고 한 가지 조심했어야 하는 건,
    저는 행을 y, 열을 x의 변수로 선언하는 것을 선호하는데,
    문제에서는 r,x를 행 c,y를 열로 표현했기에,
    해당 부분에 대해 헷갈리지 않도록 조심해야 했습니다.


2. 구현 (16:08 - 16:19)
    답변을 출력할 때, 새로운 시도를 해봤습니다.
    print(sum(map(len, trees)))
    (추후 검증 단계에서 틀린 코드로 판명나, 수정됐습니다.)

    초기 구상처럼,
    초기 세팅, 사계절 반복문 구현, 답변 출력에 대한 코드를 구현했습니다.
    봄/여름 - 가을/겨울을 구분해서 작성해줬기에,
    특별한 엣지 케이스는 생각나지 않았습니다.


3. 검증 (16:19 - 16:23)
    테스트케이스를 돌린 결과, 새롭게 도전했던 출력 코드가 이상했습니다. print(sum(map(len, trees)))
    자세히 보니, 그냥 2차원 배열의 n*n만을 출력하는 코드였습니다.
    따라서 적절한 출력을 위해 답변 출력을 위한 코드를 재작성했습니다.

    위 코드를 수정하니, 모든 테스트케이스에서 정상적인 답변이 출력됐습니다.
    그리고 메모를 다시 보고, 하나하나 대조해본 결과, 모든 요구사항이 반영돼 있었습니다.
    BFS/DFS/백트래킹을 쓰지 않은, 반복문을 이용한 구현이었기에,
    구상/구현에 대해서 다른 문제들보다 확신이 더 컸습니다.

    실행시간 제한이 0.3초였기에, 시간초과만 나지 않는다면 정답일 것이라는 확신이 들었습니다.
    그래서 코드를 보며, 시간 복잡도를 계산했습니다.
    (k * n**2 * 나무 수) 였습니다.
    나무 수는 알 수 없지만, k * n**2가 10**5였기도 하고,
    모든 칸의 나무 수가 10**2 * 3가 될 케이스는 없다고 판단한 후, 제출했습니다.
"""


directions = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))


def oob(yy, xx):
    return yy < 0 or n <= yy or xx < 0 or n <= xx


n, m, k = map(int, input().split())
feed = [list(map(int, input().split())) for _ in range(n)]  # 반복적으로 추가되는 양분의 배열

area = [[5] * n for _ in range(n)]  # 현재 각 칸의 양분의 배열
trees = [[[] for _ in range(n)] for _ in range(n)]  # 현재 각 칸의 나무들의 나이들이 담기는 배열
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    trees[a][b].append(c)  # 입력으로 주어진 나무 반영

# k년 동안의 반복문 수행
for _ in range(k):
    # 봄/여름의 작업 코드
    for i in range(n):
        for j in range(n):
            if not trees:  # (양분 먹을 / 죽어서 양분 추가할) 나무 없으면 continue
                continue

            food = area[i][j]  # 현재 칸의 초기 양분

            added_food_from_dead_trees = 0  # 여름에 죽는 나무로 인해 추가되는 양분

            now_trees = sorted(trees[i][j])  # 나이 어린 순부터 양분 먹기에, sorted()
            next_trees = []  # 봄/여름이 지나고, 현재 칸에 저장될 나무들의 나이 배열

            for age in now_trees:
                if age <= food:  # 양분이 충분하면
                    food -= age  # 나무 나이만큼 -=
                    next_trees.append(age + 1)  # 1살 증가시켜서 저장
                else:            # 양분이 충분하지 않으면
                    added_food_from_dead_trees += age // 2  # 죽고 여름에 현재 칸에 나이//2 만큼 양분 추가함

            area[i][j] = food + added_food_from_dead_trees  # 봄/여름이 지난 후의, 현재 칸의 양분
            trees[i][j] = next_trees  # 봄/여름이 지난 후의, 현재 칸의 나무들의 나이 배열

    # 가을/겨울의 작업 코드
    added_trees = [[[] for _ in range(n)] for _ in range(n)]  # 번식되는 나이 1의 나무들이 담기는 배열
    for i in range(n):
        for j in range(n):
            area[i][j] += feed[i][j]  # 겨울의 양분 추가 (가을의 작업과 독립적이므로, 먼저 해줘도 됨.)

            # 아래는 가을의 작업 코드
            if not trees[i][j]:  # 나무 없다면 번식할 나무도 없으므로, continue
                continue

            for tree_age in trees[i][j]:
                if not tree_age % 5:  # 나무의 나이가 5의 배수인 경우
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if not oob(ni, nj):
                            added_trees[ni][nj].append(1)  # 영역 밖이 아니라면, 나이 1의 나무 추가
    for i in range(n):
        for j in range(n):
            trees[i][j].extend(added_trees[i][j])  # 번식으로 추가되는 나무 반영

# 답변(k년이 지난 후 살아남은 나무 수) 출력을 위한 코드
answer = 0
for i in range(n):
    for j in range(n):
        answer += len(trees[i][j])
print(answer)
