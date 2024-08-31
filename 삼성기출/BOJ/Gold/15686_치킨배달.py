# 20240826
# 23:00
# 1 / 2

"""
풀이 시간: 23분 (16:18 ~ 16:41)
풀이 시도: 1 / 2


1. 문제 정독 & 풀이 구상 (16:18 - 16:23)
    치킨집의 최대 개수 m이 13이 상한값이므로,

    정해진 m개의 배열에 대해 각각의 치킨집으로부터 시작하는 bfs를 구현할까 하고 처음에 생각이 들었지만,
    치킨집의 최대값이 13개이므로, 치킨집 좌표를 반복문(최대 13)을 통해 최소 치킨거리를 찾는 것이 훨씬 시간적으로 유리하겠다는 생각이 들었습니다.



2. 구현 (16:23 - 16:31)
    이전에 풀었던 주사위 굴리기에서 너무나 많은 생각을 하고, 이 문제를 풀어서인지
    중간중간에 멈춰서 풀이의 논리를 확인하지 않고 구현했던 것 같습니다.
    구현을 하며, 중간중간에 print()를 통해 원하는 인자와 반환이 함수에서 이뤄짐을 확인했습니다.


3. 검증 (16:31 - 16:34)
    모든 테스트케이스를 돌려본 결과, 이상 없이 답변을 출력했기에, 큰 의심 없이 제출했습니다.


4. 시간초과 및 재구현(16:34 ~ 16:41)
    시간초과가 발생했기에, 이전의 검증에서 하지 않았던 최대 범위에서의 테스트케이스를 만들었습니다.
    n = 50, m = 6
    이 경우에 예상한 시간복잡도는, comb(13, 7) * 50 * 7로,
    13개 치킨집 중 6개를 골라, 100개의 집들에 대해, 7개의 치킨집과 거리를 비교하는 것이었습니다.
    그러나 파이참에서 제한시간보다 훨씬 더 오래 걸렸고, 뭔가 잘못 구현되었음을 알아챘습니다.

    도시치킨거리를 구하는 함수를 봤을 때는, 이상이 없다고 판단했고,
    조합을 구하는 함수를 다시 살펴본 결과,
    치킨 집을 선택함에 있어서, 순열이 아닌 조합을 해줘야 하는데,
    초기 구현에서 순열로 구현됐기에, 시간초과가 발생한 것이었습니다.

    따라서 해당 부분을 수정하여, 시간을 줄일 수 있었고, 정답을 제출했습니다.
    처음에 생각은 조합으로 했으면서 왜 순열로 구현했는지에 대해 영상을 시청해본 결과,
    순열과 조합에 대한 템플릿이 제대로 정비되어 있지 않다는 문제점을 발견했습니다.
    따라서, 앞으로 순열/조합에 대한 구현 실수를 하지 않도록, 두 개념 간의 명확한 구분을 할 것입니다.
"""


def cal_city_chicken_distance(chicken_indexes):  # 치킨집 배열들에 대해, 도시치킨거리를 구하고, 최소값을 갱신하는 함수
    now_chickens_distance = 0  # 치킨거리를 누적할 변수

    for hy, hx in homes:  # 모든 집들에 대해
        mn_distance = n**2
        for cy, cx in chicken_indexes:
            mn_distance = min(mn_distance, abs(hy - cy) + abs(hx - cx))  # 이 집의 최소 치킨거리를 계산
        now_chickens_distance += mn_distance

    global mn_chickens_distance
    mn_chickens_distance = min(mn_chickens_distance, now_chickens_distance)  # 최소 도시치킨거리 갱신


def choose_m_chickens(cnt, start_idx):  # m개의 치킨집 조합을 구하는 백트래킹 함수
    if cnt == m:  # m개의 치킨집을 골랐다면,
        chicken_indexes = [chickens[i] for i in range(len(chickens)) if chicken_visited[i]]
        cal_city_chicken_distance(chicken_indexes)  # 치킨집 좌표 배열로, 도시치킨거리 계산 & 최소값 갱신
        return

    if len(chickens) - start_idx < m - cnt:  # 조기 종료; 앞으로 남은 치킨집 수가, 필요한 치킨집 수보다 더 작다면
        return

    for i in range(start_idx, len(chickens)):
        chicken_visited[i] = 1
        choose_m_chickens(cnt + 1, i + 1)
        chicken_visited[i] = 0


n, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
homes = []
chickens = []
for i in range(n):
    for j in range(n):
        if area[i][j] == 1:
            homes.append((i, j))  # 집들 좌표 저장
        elif area[i][j] == 2:
            chickens.append((i, j))  # 치킨집들 좌표 저장

chicken_visited = [0] * len(chickens)  # m개의 치킨집을 구성할 배열
mn_chickens_distance = len(homes) * n**2  # 임의의 최소값
choose_m_chickens(0, 0)
print(mn_chickens_distance)
