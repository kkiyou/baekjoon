N = int(input())
def ishansu(n):
    if abs(n) < 10:
        return True
    n_list = list(map(int, list(str(n))))
    diff = n_list[1] - n_list[0]
    for i in range(1, len(n_list)):
        if diff == n_list[i] - n_list[i - 1]:
            pass
        else: 
            return False
    return True

res_count = 0
for num in range(1, N + 1):
    if ishansu(num):
        res_count += 1
        
print(res_count)