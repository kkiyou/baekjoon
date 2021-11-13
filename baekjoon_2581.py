# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 
# 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 
# 둘째 줄에 그 중 최솟값을 출력한다. 
# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

# 1000 이하 소수 = 168개
#  100 이하 소수 = 25개
#   10 이하 소수 = 4개

def find_prime_list(num):
    prime_list = list(range(2, num + 1))
    i = 0
    while i < len(prime_list):
        temp_num = prime_list[i]
        i += 1
        for n in prime_list[i:]:
            if n % temp_num == 0:
                prime_list.remove(n)
    return prime_list

min_num = int(input())
max_num = int(input())

p_list = find_prime_list(max_num)
prime_mm = [x for x in p_list if x >= min_num]

if len(prime_mm) < 1:
    print(-1)
else:
    print(sum(prime_mm))
    print(min(prime_mm))