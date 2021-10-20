N = int(input())
num_list = list(map(int, input().split(" ")))
num_min = num_list[0]
num_max = num_list[0]
for num in num_list[1:]:
    if num < num_min:
        num_min = num
    if num_max < num:
        num_max = num
print(num_min, num_max)