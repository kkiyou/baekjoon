# 첫째 줄에 알파벳 대문자로 이루어진 단어가 주어진다. 
# 단어의 길이는 2보다 크거나 같고, 15보다 작거나 같다.
# 첫째 줄에 다이얼을 걸기 위해서 필요한 최소 시간을 출력한다.

user = input()

alpha_time_list = [
    3, 3, 3,
    4, 4, 4,
    5, 5, 5,
    6, 6, 6,
    7, 7, 7,
    8, 8, 8, 8,
    9, 9, 9,
    10, 10, 10, 10,
]
res_t_list = []

for char in user:
    res_t_list.append(alpha_time_list[ord(char) - ord('A')])

print(sum(res_t_list))