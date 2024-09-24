# 20240924
# 07:55
# 1 / 1

from collections import deque


def bfs(start):
    visited = [0] * (members + 1)
    visited[start] = 1

    queue = deque()
    queue.append((start, 0))

    while queue:
        now_member, distance = queue.popleft()
        for next_member in connected[now_member]:
            if visited[next_member]:
                continue
            visited[next_member] = 1
            queue.append((next_member, distance + 1))

    return distance


# 멤버 수
members = int(input())

# 인접리스트
connected = [[] for _ in range(members + 1)]
while True:
    a, b = map(int, input().split())
    if not a - b:  # -1, -1 이 들어오면 종료
        break
    connected[a].append(b)
    connected[b].append(a)

# 리더 점수, 리더 후보 배열
leader_score = members + 1
leader_candidates = []

for member in range(1, members + 1):
    # 현재 멤버 점수 계산
    member_score = bfs(member)

    # 리더 점수보다 작으면, 점수&배열 갱신
    if member_score < leader_score:
        leader_score = member_score
        leader_candidates = [member]
    # 리더 점수와 같으면, 후보배열에 추가
    elif member_score == leader_score:
        leader_candidates.append(member)

print(leader_score, len(leader_candidates))
print(*leader_candidates)
