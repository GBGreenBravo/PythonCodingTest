# 20240729
# 10:18

T = int(input())
for test_case in range(1, T + 1):
    word = str(input())
    pointer = 0
    while len(word) > 1 and pointer != len(word) - 1:
        if word[pointer] == word[pointer + 1]:
            if pointer != 0:
                word = word[:pointer] + word[pointer + 2:]
            else:
                word = word[2:]
            pointer -= 1 if pointer > 0 else 0
        else:
            pointer += 1

    print(f"#{test_case} {len(word)}")


# 스택 개념 활용
"""
T = int(input())
for test_case in range(1, T + 1):
    word = list(str(input()))
    stk = []
    for w in word:
        if stk and stk[-1] == w:
            del stk[-1]
        else:
            stk.append(w)
    print(f"#{test_case} {len(stk)}")
"""