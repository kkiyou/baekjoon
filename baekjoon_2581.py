# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
# 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 
# 둘째 줄에 그 중 최솟값을 출력한다. 
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

# 1000 이하 소수 = 168개
#  100 이하 소수 = 25개
#   10 이하 소수 = 4개

def find_prime_list(min_n, max_n):
    stop_n = int(max_n ** 0.5)
    tf_list = [True] * (max_n - 1)
    for i in range(2, stop_n + 1):
        if tf_list[i - 2] == True:
            for j in range(i * 2, max_n + 1, i):
                tf_list[j - 2] = False
    prime_num = [
        i for i in range(2, max_n + 1)
            if (tf_list[i - 2] == True) & (i >= min_n)
    ]
    return prime_num

min_n = int(input())
max_n = int(input())

p_list = find_prime_list(min_n, max_n)

if len(p_list) < 1:
    print(-1)
else:
    print(sum(p_list))
    print(min(p_list))