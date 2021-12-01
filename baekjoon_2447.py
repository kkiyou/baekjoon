# 재귀적인 패턴으로 별을 찍어 보자. 
# N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 
# 크기 N/3의 패턴으로 둘러싼 형태이다. 
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 
# 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

n = int(input())
result_list = [['*'] * n for _ in range(n)]

def divide(start_x, start_y, size, shape):
    """
    각 사이즈 별로 분할함
    """
    if (start_x == 0) & (start_y == 0) & (size // 3 != 1):
        for y in range(0, n, size // 3):
            for x in range(0, n, size // 3):
                divide(x, y, size // 3, shape)
    blank_square(start_x, start_y, size, shape)
    
def blank_square(start_x, start_y, size, shape):
    """
    가운데를 공백으로 만듦
    """
    blank_size = size // 3
    for y in range(start_y + blank_size, start_y + blank_size * 2):
        for x in range(start_x + blank_size, start_x + blank_size * 2):
            shape[y][x] = ' '

divide(0, 0, n, result_list)

for lis in result_list:
    for i in lis:
        print(i, sep='', end='')
    print()