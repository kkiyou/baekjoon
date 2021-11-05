# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 
# 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

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

repeat_n = int(input())
num_list = list(map(int, input().split(' ')))

max_num = max(num_list)
p_list = find_prime_list(max_num)

for i in num_list:
    if i in p_list:
        pass
    else:
        repeat_n -= 1

print(repeat_n)

