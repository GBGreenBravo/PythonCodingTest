# 20240820
# 1:32:50
# 1 / 5

# 이분탐색 심화버전으로 풂. 탐색의 대상이 되는 target이 내림차순이었기에,
# right는 이전의 값으로 시작해도 되지만,
# left는 그 인덱스의 값이 target보다 작아질 때까지 2의 d제곱만큼 빼면서 다음 순서에서 별도로 처리해줬다. (항상 0으로 설정했을 때는 시간초과 났기에)

# 위의 풀이를 명료하게 구현하는 것이, 투 포인터..!

# ab, cd로 병합해서 16_000_000끼리 비교하는 건 쉽게 생각했으나, ab의 값 카운트를 (n + 1) * 2 길이의 리스트로 하려 해서, 메모리 초과가 났었다.
# 이럴 때는 별도로 카운트되는 수의 개수가 최대 16_000_000이므로, list가 아닌 dictionary로 다루는 것이 메모리 효율적임.
# 해당 풀이는 본 풀이 밑 주석에.

n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
    aa, bb, cc, dd = map(int, input().split())
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)

ab = []  # a와 b 배열의 각 원소 합의 조합을 저장한 배열 (최대 4000**2)
cd = []
for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])
        cd.append(c[i] + d[j])

answer_cnt = 0

ab.sort()  # 오름차순 정렬
cd.sort()  # 오름차순 정렬
min_cd, max_cd = min(cd), max(cd)
before_left = 0  # 이전 숫자의 왼쪽 index
before_right = len(cd) - 1  # 이전 숫자의 오른쪽 index
for ab_num in ab:  # ab배열에서 하나 꺼내고
    target = -ab_num  # 합이 0이 되는 목표치 설정
    if target < min_cd or target > max_cd:  # 목표치가 최소/최대 범위에 포함 안되면 continue
        continue

    d = 0
    while before_left - 2 ** d >= 0:  # before_left가 현재 target의 index보다 클 것이므로
        if cd[before_left - 2 ** d] < target:  #cd[index]의 값이 target보다 더 작아질 때까지 2의 d제곱 만큼 빼는 작업
            break
        d += 1

    left, right = max(0, before_left - 2**d), before_right  # 이전에서 빼준 값이 0보다 작으면 0 선택 / before_right는 그대로
    while left <= right:  # 이분탐색
        middle = (left + right) // 2
        middle_value = cd[middle]

        if middle_value == target:
            cd_left, cd_right = cd[left], cd[right]
            if cd_left == target and cd_right == target:
                break
            elif cd_left == target:
                right -= 1
            elif cd_right == target:
                left += 1
            else:
                left += 1
                right -= 1
        elif middle_value < target:
            left = middle + 1
        else:  # elif middle_value > target:
            right = middle - 1
    else:
        continue
    answer_cnt += right - left + 1

    before_left = left  # 현재 left를 저장하고, 다음 순서에서 2의 d제곱씩 빼면서 값 더 작아지도록 작업해주는 게, 0부터 탐색하는 것보다 효율 좋음.
    before_right = right  # 다음 순서인 ab_number은 지금의 ab_number보다 무조건 크므로, 지금의 right보다 큰 인덱스를 살펴볼 필요 없음.

print(answer_cnt)

"""
n = int(input())
a, b, c, d = [], [], [], []
for _ in range(n):
    aa, bb, cc, dd = map(int, input().split())
    a.append(aa)
    b.append(bb)
    c.append(cc)
    d.append(dd)

ab = []
cd = dict()
for i in range(n):
    for j in range(n):
        ab.append(a[i] + b[j])
        if cd.get(c[i] + d[j]):
            cd[c[i] + d[j]] += 1
        else:
            cd[c[i] + d[j]] = 1

answer_cnt = 0
for ab_number in ab:
    answer_cnt += cd.get(-ab_number, 0)
print(answer_cnt)
"""