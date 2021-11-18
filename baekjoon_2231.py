# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 
# 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 
# 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# 첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

n = int(input())

def constructor(n):
    res_lis = [n]
    while n != 0:
        res_lis.append(n % 10)
        n //= 10
    return sum(res_lis)

available_list = list(range(n - len(str(n) * 9), n))
available_list = [i for i in available_list if i > 0]
res = []
for i in available_list:
    if constructor(i) == n:
        res.append(i)
if len(res) == 0:
    print(0)
else:
    print(min(res))