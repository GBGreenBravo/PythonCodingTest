# 20240807
# 06:13
# 1 / 1


def dfs(cnt, making):  # 사용된 카드 수, 만들어지고 있는 string
    if cnt == k:  # 카드 개수가 k개면 results에 making 문자열 저장.
        results.append(making)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, making + cards[i])
            visited[i] = False


n = int(input())
k = int(input())
cards = [str(input()) for _ in range(n)]
visited = [False] * n  # 중복 방문을 피하기 위한 방문 배열
results = []  # k개의 카드로 조합된 모든 결과를 저장하는 리스트
dfs(0, '')
print(len(set(results)))  # 중복되는 값은 set()으로 제거하고, 조합의 개수 출력
