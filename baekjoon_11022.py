repeat = int(input())
for i in range(1, (repeat + 1)):
    A, B = list(map(int, input().split(" ")))
    print(f"Case #{i}: {A} + {B} = {A + B}")