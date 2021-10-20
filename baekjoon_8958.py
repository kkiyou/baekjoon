N = int(input())
for _ in range(N):
    ox_result = input()
    ox_res_list = list(ox_result)
    score = 0
    i = 1
    for ox in ox_res_list:
        if ox == 'O':
            score = score + i
            i += 1
        else:
            i = 1
    print(score)