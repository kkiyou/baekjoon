N = int(input())
if N < 10:
    N = N * 10
origin_N = N
cycle_n = 0
while True:
    N_10 = N // 10
    N_1 = N % 10
    new_N = N_1 * 10 + (N_10 + N_1) % 10
    cycle_n += 1
    if origin_N == new_N:
        break
    else:
        N = new_N
print(cycle_n)