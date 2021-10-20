H, M = map(int, input().split())

if 45 <= M and M < 60:
    print(H, M - 45)
elif M < 45 and H == 0:
    print(24 - 1, M + 15)
else:
    print(H -1, M + 15)