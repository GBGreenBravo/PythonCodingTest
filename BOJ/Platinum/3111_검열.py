# 20241203
# 1 / 21

import sys
from collections import deque

word = str(input())
N = len(word)
text = deque(str(sys.stdin.readline()))
left, right = deque(), deque()

while len(text) >= N:
    while text and len(text) >= N:
        for i in range(N):
            if text[i] != word[i]:
                break
        else:
            for _ in range(N):
                text.popleft()
            for _ in range(min(2 * N - 2, len(left))):
                text.appendleft(left.pop())
            break
        left.append(text.popleft())
    while text and len(text) >= N:
        for i in range(N):
            if text[-1 - i] != word[-1 - i]:
                break
        else:
            for _ in range(N):
                text.pop()
            for _ in range(min(2 * N - 2, len(right))):
                text.append(right.popleft())
            break
        right.appendleft(text.pop())

print("".join(left + text + right))
