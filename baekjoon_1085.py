# 한수는 지금 (x, y)에 있다. 
# 직사각형은 각 변이 좌표축에 평행하고, 
# 왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 x, y, w, h가 주어진다.


# (0, h) (1, h) (2, h) ... (w, h)
#   ...    ...    ...  ...   ...
# (0, 3) (1, 3) (2, 3) ... (w, 3)
# (0, 2) (1, 2) (2, 2) ... (w, 2)
# (0, 1) (1, 1) (2, 1) ... (w, 1)
# (0, 0) (1, 0) (2, 0) ... (w, 0)

x, y, w, h = map(int, input().split(' '))

print(min(x, w - x, y, h - y))