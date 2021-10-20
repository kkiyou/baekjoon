A = int(input())
B = int(input())
C = int(input())
split_num_list = list(map(int, list(str(A * B * C))))
for n in range(0, 10):
    print(split_num_list.count(n))