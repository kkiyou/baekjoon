N = int(input())
for _ in range(N):
    score_list = list(map(int, input().split(" ")))
    student_n = score_list.pop(0)
    mean_score = sum(score_list) / student_n
    over_mean_student_n = 0
    for score in score_list:
        if mean_score < score:
            over_mean_student_n += 1
    ratio = round((over_mean_student_n / student_n) * 100, 3)
    print("{:.3f}%".format(ratio))