# 20240719

score = 0

for _ in range(10):
    now = int(input())
    if 100 - score - now >= 0:
        score += now
        continue
    elif 100 - score < abs(100 - score - now):
        break
    else:
        score += now
        break

print(score)
