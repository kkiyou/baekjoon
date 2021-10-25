# 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 
# 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
# X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 분수를 출력한다.

#  1   2   6   7  15  
#  3   5   8  14
#  4   9  13
# 10  12
# 11 

user_num = int(input())
distance_n = 0
s_sum = 0

while user_num > s_sum:
    distance_n += 1
    s_sum += distance_n

a = distance_n - (s_sum - user_num)
b = distance_n - a + 1

if distance_n % 2 == 0:
    print(f"{a}/{b}")
else:
    print(f"{b}/{a}")
