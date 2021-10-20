# 문자열 S를 입력받은 후에, 
# 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
# S에는 QR Code "alphanumeric" 문자만 들어있다.
# QR Code "alphanumeric" 문자는 
# 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

total_n = int(input())

for _ in range(total_n):
    repeats, strings = input().split()
    repeats = int(repeats)
    res = ''
    
    for char in strings:
        res = res + (char * repeats)
    print(res)