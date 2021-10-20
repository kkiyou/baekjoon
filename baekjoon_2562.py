max_N = 0
max_N_i = 0
for i in range(1, 10):
    globals()[f"N_{i}"] = int(input())
    if max_N < globals()[f"N_{i}"]:
        max_N = globals()[f"N_{i}"]
        max_N_i = i
print(max_N)
print(max_N_i)