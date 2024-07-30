# 20240730
# 54:28

# f1, f2 = 1, 1
# pairs = {(0, 1): 1, (1, 1): 1}
# i = 2
# while True:
#     i += 1
#     f3 = (f1 + f2) % 1000000
#     if pairs.get((f3, f2)) == 1:
#         break
#     pairs[(f3, f2)] = 1
#
#     f1, f2 = f2, f3
#
# print(i)
# print(f1, f2, f3)

# 위 코드로 dictionary에 넣어서 중복시작하는 n번째를 구함.
# 1,500,000번째에서 0이 나오고 그 다음에 1이 나오기 때문에,
# 1,500,000을 %= 해줌.

n = int(input())
if n < 3:
    print(1)
else:
    if n >= 1500000:
        n %= 1500000

    f1, f2 = 1, 1
    i = 2
    while i != n:
        f3 = (f1 + f2) % 1000000
        i += 1
        f1, f2 = f2, f3
    print(f3)






