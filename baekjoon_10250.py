group = int(input())

for _ in range(group):
    height, width, order = map(int, input().split(' '))
    yy = order % height
    xx = order // height + 1
    if yy == 0:
        yy = height
        xx -= 1 
    # print(f"""{yy}{format(xx, "0>2")}""")
    print(f"{yy}{str(xx).rjust(2, '0')}") # 더 빠름
