# 20240818
# 13:40
# 1 / 1

"""
0
1 2
3 4 5
6 7 8 9
10 11 12 13
"""
# 위의 인덱스로 triangle에 넣어놓고 아래서 2번째 줄부터 밑의 최대값을 추가해가며 누적시킴
# 위 계산을 해주면 맨 위에 최대값이 저장되게 됨.

triangle = []
n = int(input())
for _ in range(n):
    triangle.extend(list(map(int, input().split())))

first_indexes = [0]
idx = 0
d = 1
for i in range(n - 1):
    idx += d
    first_indexes.append(idx)
    d += 1

for i in range(n - 2, -1, -1):
    start_idx = first_indexes[i]
    end_idx = first_indexes[i + 1]
    for j in range(start_idx, end_idx):
        triangle[j] += max(triangle[j + i + 1], triangle[j + i + 2])

print(triangle[0])
