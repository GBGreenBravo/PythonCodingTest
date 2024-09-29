# 20240929
# 11:18
# 1 / 1

from collections import deque

t = int(input())
for _ in range(t):
    start, end = map(int, input().split())

    visited = [0] * 10000
    visited[start] = '_'

    queue = deque()
    queue.append(start)
    while queue and not visited[end]:
        now = queue.popleft()
        history = visited[now]

        d = (now * 2) % 10000
        if not visited[d]:
            visited[d] = history + 'D'
            queue.append(d)

        s = now - 1 if now else 9999
        if not visited[s]:
            visited[s] = history + 'S'
            queue.append(s)

        four = '0' * (4 - len(str(now))) + str(now)

        l = int(four[1:] + four[0])
        if not visited[l]:
            visited[l] = history + 'L'
            queue.append(l)

        r = int(four[-1] + four[:3])
        if not visited[r]:
            visited[r] = history + 'R'
            queue.append(r)

    print(visited[end][1:])


# 20240815
# 14:37
# 1 / 1

# L, R에서 각각 (x % 1000 * 10) + (x // 1000), (x % 10) * 1000 + (x // 10)를 활용했다    면 더 좋았을 듯함.

from collections import deque


def make_nexts(number, command_str):  # 숫자와 커맨드문자열을 받아, (다음 숫자, 다음 커맨드문자열) 리스트를 반환하는 함수
    d = (number * 2) % 10000
    s = number - 1 if number > 0 else 9999
    full_number = str(number) if number // 1000 else '0' * (4 - len(str(number))) + str(number)  # 1000보다 작으면 앞에 0으로 채워주기 위함.
    l = int(full_number[1:] + full_number[0])
    r = int(full_number[3] + full_number[:3])
    return [(d, command_str + 'D'), (s, command_str + 'S'), (l, command_str + 'L'), (r, command_str + 'R')]


t = int(input())
for _ in range(t):
    start, end = map(int, input().split())
    visited = [False] * 10_000
    visited[start] = True

    queue = deque()
    queue.append((start, ''))

    while queue:
        now, commands = queue.popleft()  # 현재 숫자, 현재까지의 커맨드목록

        if now == end:
            answer = commands
            break

        for next_num, new_commands in make_nexts(now, commands):
            if not visited[next_num]:  # 이미 방문했던 곳은, 이미 최단or같은 거리로 방문했다는 뜻이므로 continue
                visited[next_num] = True
                queue.append((next_num, new_commands))

    print(answer)
