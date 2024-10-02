# 20241001
# 22:42
# 1 / 1

# 17140_이차원배열과연산

"""
풀이 시간: 23분 (15:37 - 16:00)
풀이 시도: 1 / 1


1. 문제 정독 & 풀이 구상 (15:37 - 15:42)


2. 구현 (15:42 - 15:52)
    이전 풀이에서 입력의 행/열이 IndexError을 일으킬 수도 있음을 모르고 틀렸었기에,
    이번에는 같은 실수를 하지 않도록 주의했습니다.

    풀이방식은 이전 코드와 동일합니다.
    다만, dictionary의 get()메서드에 default값을 설정하거나, map()을 더 적극적으로 활용하여
    코드가 간결해졌다는 차이가 있습니다.


3. 디버깅 (15:52 - 15:59)
    숫자/빈도 순으로 추가해야 할 것을, 빈도/숫자 순으로 추가했던 실수가 있었습니다.

    한 가지 간과했던 것은, 빈도체크 중에 0을 만나면
    break가 아닌 continue를 써야하는데 섣불리 구현했기에, 해당 코드의 디버깅에 시간이 소요됐습니다.
"""


def operate():
    for idx, row in enumerate(area):
        num_dict = dict()
        for value in row:
            if not value:
                continue
            num_dict[value] = num_dict.get(value, 0) + 1

        new_row = []
        for num_cnt in sorted(num_dict.items(), key=lambda nd: (nd[1], nd[0])):
            new_row.extend(num_cnt)

        area[idx] = new_row[:100]

    max_col = max(map(len, area))
    for idx, row in enumerate(area):
        area[idx].extend([0] * (max_col - len(row)))


r, c, k = map(int, input().split())
r, c = r - 1, c - 1

area = [list(map(int, input().split())) for _ in range(3)]

time = 0
len_row, len_col = 3, 3
while not(r < len_row and c < len_col and area[r][c] == k):
    time += 1
    if time == 101:
        break

    if len_row >= len_col:
        operate()
    else:
        area = [list(rr) for rr in list(zip(*area))[::-1]]
        operate()
        area = [list(rr)[::-1] for rr in zip(*area)]

    len_row, len_col = len(area), len(area[0])

print(time if time != 101 else -1)
