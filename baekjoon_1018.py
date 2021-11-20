# 지민이는 자신의 저택에서 MN개의 단위 정사각형으로 나누어져 있는 M×N 크기의 보드를 찾았다.
# 어떤 정사각형은 검은색으로 칠해져 있고, 나머지는 흰색으로 칠해져 있다.
# 지민이는 이 보드를 잘라서 8×8 크기의 체스판으로 만들려고 한다.
# 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야 한다.
# 구체적으로, 각 칸이 검은색과 흰색 중 하나로 색칠되어 있고, 
# 변을 공유하는 두 개의 사각형은 다른 색으로 칠해져 있어야 한다.
# 따라서 이 정의를 따르면 체스판을 색칠하는 경우는 두 가지뿐이다.
# 하나는 맨 왼쪽 위 칸이 흰색인 경우, 하나는 검은색인 경우이다.
# 보드가 체스판처럼 칠해져 있다는 보장이 없어서, 
# 지민이는 8×8 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 다시 칠해야겠다고 생각했다.
# 당연히 8*8 크기는 아무데서나 골라도 된다.
# 지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
# 첫째 줄에 N과 M이 주어진다. N과 M은 8보다 크거나 같고, 50보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에는 보드의 각 행의 상태가 주어진다. B는 검은색이며, W는 흰색이다.
# 첫째 줄에 지민이가 다시 칠해야 하는 정사각형 개수의 최솟값을 출력한다.

len_y, len_x = map(int, input().split(' '))
user = []
for y in range(len_y):
    user.append(list(input()))

# (0, 0)이 B일 때와 W일 때의 정답을 찾음
def find_answer(start_color, answer_list):
    end_color = 'B' if start_color == 'W' else 'W'
    odd_row = [start_color, end_color] * (len_x // 2) + [start_color] * (len_x % 2)
    even_row = [end_color, start_color] * (len_x // 2) + [end_color] * (len_x % 2)
    for y in range(len_y):
        answer_list.append(odd_row if y % 2 == 0 else even_row)
    return answer_list

# 유저의 입력값과 정답을 비교해서 다르면 1로 대치한 리스트를 반환함
def error_list(user, answer):
    cal_list = [[0] * len_x for _ in range(len_y)]
    for y in range(len_y):
        for x in range(len_x):
            if user[y][x] != answer[y][x]:
                cal_list[y][x] = 1
            else:
                cal_list[y][x] = 0
    return cal_list

# 8 by 8 배열로 가능한 모든 위치를 탐색하며 오차를 구한 후, 그 중 최소값을 구함
def find_min(error_list):
    temp_sum_list = []
    for y_n, y_last in enumerate(range(8, len_y + 1)):
        for x_n, x_last in enumerate(range(8, len_x + 1)):
            temp_sum = 0
            for i in range(8):
                temp_sum += sum(error_list[y_n:y_last][i][x_n:x_last])
            temp_sum_list.append(temp_sum)
    return min(temp_sum_list)

error_b = error_list(user, find_answer('B', []))
error_w = error_list(user, find_answer('W', []))
print(min(find_min(error_b), find_min(error_w)))