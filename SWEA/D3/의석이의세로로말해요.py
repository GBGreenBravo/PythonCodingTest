# 20240725
# 08:37

T = int(input())
for test_case in range(1, T + 1):
    words = [list(str(input())) for _ in range(5)]
    max_length = max([len(w) for w in words])
    for word in words:
        if len(word) < max_length:
            for i in range(max_length - len(word)):
                word.append(" ")
    spinned = ""
    for i in zip(*words):
        for j in i:
            spinned += str(j)
    print(f"#{test_case} {spinned.replace(' ', '')}")
