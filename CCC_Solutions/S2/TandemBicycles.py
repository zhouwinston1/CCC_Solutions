question_type = int(input())
pairs_needed = int(input())

bikes1 = list(map(int, input().split(" ")))
bikes2 = list(map(int, input().split(" ")))

if question_type == 2:
    bikes1.extend(bikes2)
    sum_of_speeds = 0

    for i in range(pairs_needed):
        sum_of_speeds += bikes1.pop(bikes1.index(max(bikes1)))

    print(sum_of_speeds)

else:
    sum_of_speeds = 0

    for i in range(pairs_needed):
        temp1 = bikes1.pop(bikes1.index(max(bikes1)))
        temp2 = bikes2.pop(bikes2.index(max(bikes2)))
        if temp1 > temp2:
            sum_of_speeds += temp1
        else:
            sum_of_speeds += temp2

    print(sum_of_speeds)