# 20240726
# 1시간 넘게 못 풂.

# 초기에 result값을 word로 설정해놔서 틀림.
# 'abcde'의 경우, 정답이 'abedc'지만 'abcde'보다 순위가 밀려있음.

word = str(input())
result = word

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        now = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        if now < result:
            result = now

print(result)

# 위는 오답.
# 아래와 같이, result 초기값을 제대로 설정해주면 됨.

word = str(input())
result = 'z' * len(word)

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        now = word[:i][::-1] + word[i:j][::-1] + word[j:][::-1]
        if now < result:
            result = now

print(result)
