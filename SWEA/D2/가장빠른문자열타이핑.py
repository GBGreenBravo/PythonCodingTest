# 20240725
# 04:27

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(str, input().split())
    print(f"#{test_case} {len(a) - (len(b) - 1) * a.count(b)}")
