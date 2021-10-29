# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

a, b = input().split(' ')

max_len = max(len(a), len(b))
a = format(a, f"0>{max_len}")
b = format(b, f"0>{max_len}")
result = 0
temp_1 = 0
for indices, i in enumerate(range(max_len - 1, -1, -1)):
    result += ((int(a[i]) + int(b[i]) + temp_1) % 10) * (10 ** indices)
    temp_1 = (int(a[i]) + int(b[i]) + temp_1) // 10
if temp_1 == 1:
    result += (10 ** max_len)

print(result)