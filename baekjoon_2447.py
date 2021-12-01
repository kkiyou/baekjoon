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