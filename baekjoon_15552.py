import sys

n = int(sys.stdin.readline())
for i in range(n):
    A, B = list(map(int, sys.stdin.readline().split(" ")))
    print(A + B)