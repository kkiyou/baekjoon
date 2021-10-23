# 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 1씩 증가하는 번호를 주소로 매길 수 있다. 
# 숫자 N이 주어졌을 때, 
# 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
# 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 
# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

# 1
# 2 ~ 7(6)
# 8 ~ 19(12)
# 20 ~ 37(18)

def honeycomb_room(number):
    room_n = 1
    max_range_num = 1
    while True:
        if number <= max_range_num:
            print(room_n)
            break
        else:
            max_range_num += 6 * room_n
            room_n += 1

honeycomb_room(int(input()))