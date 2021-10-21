# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 
# 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, 
# kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, 
# aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 단어의 개수 N이 들어온다. 
# N은 100보다 작거나 같은 자연수이다. 
# 둘째 줄부터 N개의 줄에 단어가 들어온다. 
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

def is_group_word(word):
    # 연속된 문자열 제거
    continuous_alpha = []
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            continuous_alpha.append(word[i])
    continuous_alpha.append(word[-1])

    # 중복된 값이 있으면 False
    deduplication_alpha = list(set(continuous_alpha))
    if len(deduplication_alpha) != len(continuous_alpha):
        return False
    else:
        return True

user_n = int(input())
result = 0

for _ in range(user_n):
    user = input()
    if is_group_word(user):
        result += 1
print(result)