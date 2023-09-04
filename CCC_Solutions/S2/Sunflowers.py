def q4():
    my_arr = []
    for i in range(int(input())):
        temp = list(map(int, input().split(" ")))
        my_arr.append(temp)

    my_min = float('inf')
    row_index = 0
    col_index = 0

    row_len = len(my_arr)
    col_len = len(my_arr[0])

    for i in range(row_len):
        for j in range(col_len):
            if my_min > my_arr[i][j]:
                my_min = my_arr[i][j]
                row_index = i
                col_index = j

                # print(row_index, col_index)

    # 1. If rotate 360 degreee, row and col no change
    if row_index == 0 and col_index == 0:
        for i in range(row_len):
            for j in range(col_len):
                print(my_arr[i][j], end=" ")
            print()

    # 2. If rotate 90 degree, row index change but col index no change
    if row_index > 0 and col_index == 0:
        for j in range(col_len):
            for i in range(row_len - 1, -1, -1):
                print(my_arr[i][j], end=" ")
            print()

    # 3. If rotate 180 degree, row and col all change
    if row_index > 0 and col_index > 0:
        for i in range(row_len - 1, -1, -1):
            for j in range(col_len - 1, -1, -1):
                print(my_arr[i][j], end=" ")
            print()

    # 4. If rotate 270 degree, row no change only col change
    if row_index == 0 and col_index > 0:
        for j in range(col_len - 1, -1, -1):
            for i in range(row_len):
                print(my_arr[i][j], end=" ")
            print()


q4()







