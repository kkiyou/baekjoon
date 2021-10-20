def dn(n):
    n_list = list(map(int, list(str(n))))
    return (n + sum(n_list))
self_num_list = list(range(1, 10001))
for num in range(1, 10001):
    n = dn(num)
    try:
        self_num_list.remove(n)
    except:
        pass
for num in self_num_list:
    print(num)