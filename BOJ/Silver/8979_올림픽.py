# 20240806
# 1 / 1

n, k = map(int, input().split())
countries = [(0, -1, -1, -1)] * (n + 1)
# (country, gold, silver, bronze) 나라는 1부터 시작하므로 0으로 초기화, 메달 개수가 -1은 불가능하므로 -1로 초기화
for _ in range(n):
    country, gold, silver, bronze = map(int, input().split())
    countries[country] = (country, gold, silver, bronze)
countries.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)  # 금->은->동 메달 개수 내림차순으로 정렬

rankings = [None] * (n + 1)  # country에 따른 랭킹을 저장할 리스트
rankings[countries[0][0]] = 1  # 1위 나라에 대한 랭킹 저장

for i in range(1, len(countries)):
    c_now = countries[i]
    if c_now[1:] == countries[i - 1][1:]:  # 앞의 나라와 동일한 금은동을 가진 경우
        rankings[c_now[0]] = rankings[countries[i - 1][0]]  # 같은 순위로 저장
        continue
    else:
        rankings[c_now[0]] = i + 1  # 앞의 나라보다 낮은 순위인 경우 i+1 저장.

print(rankings[k])
