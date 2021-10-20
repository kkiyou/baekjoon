# 첫째 줄에 최대 100글자의 단어가 주어진다. 
# 알파벳 소문자와 '-', '='로만 이루어져 있다.
# 단어는 크로아티아 알파벳으로 이루어져 있다.
# 문제 설명의 표에 나와있는 알파벳은 변경된 형태로 입력된다.
# 입력으로 주어진 단어가 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.

user = input()
croatia_alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

c_alpha_count = 0
for c_alpha in croatia_alpha:
    c_alpha_count += user.count(c_alpha)
    user = user.replace(c_alpha, ' ')

print(len(user.replace(' ', '')) + c_alpha_count)