# 0보다 크거나 같은 정수 N이 주어진다. 
# 이때, N!을 출력하는 프로그램을 작성하시오.

def factorial(n):
    if n != 0:
        return n * factorial(n - 1)
    else:
        return 1

print(factorial(int(input())))