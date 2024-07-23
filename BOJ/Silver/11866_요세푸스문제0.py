# 20240723
# 11:28

n, k = map(int, input().split())
people = list(range(1, n + 1))
now_index = -1
len_people = len(people)
result = []
while people:
    now_index = (now_index + k) % len_people
    result.append(people.pop(now_index))
    now_index -= 1
    len_people -= 1

print("<", end="")
print(*result, sep=", ", end="")
print(">")
