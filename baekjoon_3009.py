# 세 점이 주어졌을 때, 
# 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
# 세 점의 좌표가 한 줄에 하나씩 주어진다. 
# 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

# (3, 7)             (10, 7)
# 
# 
# 
# (3, 1)             (10, 1)

x_1, y_1 = map(int, input().split(' '))
x_2, y_2 = map(int, input().split(' '))
x_3, y_3 = map(int, input().split(' '))

w = max(abs(x_1 - x_2), abs(x_2 - x_3), abs(x_1 - x_3))
h = max(abs(y_1 - y_2), abs(y_2 - y_3), abs(y_1 - y_3))
max_x = max(x_1, x_2, x_3)
max_y = max(y_1, y_2, y_3)
p_list = [[max_x, max_y],
          [max_x - w, max_y],
          [max_x, max_y - h],
          [max_x - w, max_y - h]]
[p_list.remove(i) for i in [[x_1, y_1], [x_2, y_2], [x_3, y_3]]]
print(p_list[0][0], p_list[0][1])