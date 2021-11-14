# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. 
# (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

def print_prime_num(min_n, max_n):
    stop_n = int(max_n ** 0.5)
    tf_list = [True] * (max_n - 1)
    for i in range(2, stop_n + 1):
        if tf_list[i - 2] == True:
            for j in range(i * 2, max_n + 1, i):
                tf_list[j - 2] = False
    for i in range(2, max_n + 1):
        if (tf_list[i - 2] == True) & (i >= min_n):
            print(i)

min_n, max_n = map(int, input().split(' '))
print_prime_num(min_n, max_n)