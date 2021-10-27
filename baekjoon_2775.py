# 이 아파트에 거주를 하려면 조건이 있는데, 
# “a층의 b호에 살려면 
# 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다”
# 는 계약 조항을 꼭 지키고 들어와야 한다.
# 아파트에 비어있는 집은 없고 모든 거주민들이 이 계약 조건을 지키고 왔다고 가정했을 때,
# 주어지는 양의 정수 k와 n에 대해 k층에 n호에는 몇 명이 살고 있는지 출력하라. 
# 단, 아파트에는 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명이 산다.
# 첫 번째 줄에 Test case의 수 T가 주어진다. 그리고 각각의 케이스마다 입력으로 첫 번째 줄에 정수 k, 두 번째 줄에 정수 n이 주어진다

#      .   .   .   .   . 
#      .   .   .   .   . 
#      .   .   .   .   . 
# F4   1   6  21  56  91
# F3   1   5  15  35  70 ...
# F2   1   4  10  20  35 ...
# F1   1   3   6  10  15 ...
# ------------------------
# F0   1   2   3   4   5 ... 14

def num_of_unit_members(floor, unit):
    # 0층 선언
    globals()["floor_0"] = list(range(1, unit + 1))

    # 각 층의 인원 리스트 반환
    def household_members(downstairs_list):
        member_list = []
        for i, members in enumerate(downstairs_list):
            member_list.append(
                (members + member_list[i - 1]) if i != 0 else members
            )
        return member_list

    # 각 층의 인원 리스트를 변수로 할당
    for f in range(1, floor + 1):
        globals()[f"floor_{f}"] = \
            household_members(globals()[f"floor_{f - 1}"])

    # 출력
    print(globals()[f"floor_{floor}"][unit - 1])

test_case = int(input())

for _ in range(test_case):
    floor = int(input())
    unit = int(input())
    num_of_unit_members(floor, unit)
