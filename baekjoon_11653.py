# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. 
# N이 1인 경우 아무것도 출력하지 않는다.

# 1000 이하 소수 = 168개
#  100 이하 소수 = 25개
#   10 이하 소수 = 4개

num = int(input())

i = 2
while num != 1:
    if num % i == 0:
        num /= i
        print(i)
    else:
        i += 1