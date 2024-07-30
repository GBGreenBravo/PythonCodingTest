# 20240730
# 10:50

# 앞에서부터 내림차순 스택 구현하는 게 더 단순함.
# 내 풀이는 아래와 같다.
# 뒤에서부터 스택을 쌓는다.
# 스택에는 (빌딩 높이, 뒤에 있는 빌딩중 나보다 작은 빌딩 수)가 들어간다.
# 현재 스택에 나보다 작은 빌딩이 있다면, pop하고 그 스택[1]+1을 누적시킨다. -> 같은 높이의 스택은 그대로 놔둠.
# 누적된 값을 ans에 += 하고, stk에 현재의 스택을 추가한다.

n = int(input())
buildings = [int(input()) for _ in range(n)]
buildings.reverse()

stk = [(buildings.pop(0), 0)]

ans = 0
for building in buildings:
    tmp = 0
    while stk and stk[-1][0] < building:
        height, cnt = stk.pop()
        tmp += cnt + 1
    stk.append((building, tmp))
    ans += tmp

print(ans)
