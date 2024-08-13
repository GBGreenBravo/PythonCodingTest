# 20240813
# 21:37
# 1 / 3

# 아래 풀이처럼 n에서 1까지 내림차순으로 찾는 방법도 있지만, 반대로 1,2,3 채워놓고 오름차순으로 찾는 풀이도 있다.

from collections import deque

n = int(input())
visited = [0] * (n + 1)  # 방문여부 체크를 위한 배열
visited[n] = 1  # 첫 시작(n)에 1
queue = deque()
queue.append(n)

answer = 0
while queue:  # BFS로 진행되므로 distance 오름차순이 보장됨
    now = queue.popleft()
    if now == 1:  # 현재 방문이 1이면 종료.
        answer = visited[1] - 1
        break
    distance = visited[now] + 1  # 다음 방문의 distance

    if now % 3 == 0 and (not visited[now // 3] or visited[now // 3] > distance):  # 현재 수가 3으로 나눠 떨어지고, 방문 안했거나, 했다면 기존보다 거리가 짧을 때
        visited[now // 3] = distance
        queue.append(now // 3)
    if now % 2 == 0 and (not visited[now // 2] or visited[now // 2] > distance):  # 현재 수가 2로 나눠 떨어지고, 방문 안했거나, 했다면 기존보다 거리가 짧을 때
        visited[now // 2] = distance
        queue.append(now // 2)
    if not visited[now - 1]:  # 현재 수 - 1에 방문 안 했을 때만 (//2나 //3보다 항상 더 큰 distance를 보장함)
        visited[now - 1] = distance
        queue.append(now - 1)

print(answer)
