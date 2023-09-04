def brute_force():
    rows = int(input())
    cols = int(input())

    temp = []

    for loop in range(rows):
        temp2 = input().split(" ")
        for i in range(len(temp2)):
            temp2[i] = int(temp2[i])
        temp.append(temp2)

    def is_prime(n):
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    dontRun = False
    num = temp[0][0]
    if is_prime(num) == True and num > cols:
        print("no")
        dontRun = True
    counter = 0
    wrong = []

    while True and not dontRun:
        found = False
        counter += 1
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        for check in range(len(factors)):
            for check2 in range(len(factors)):
                if factors[check] * factors[check2] == num:
                    if factors[check] <= rows and factors[check2] <= cols:
                        if temp[factors[check] - 1][factors[check2] - 1] not in wrong:
                            num = temp[factors[check] - 1][factors[check2] - 1]
                            found = True

        if not found:
            num = temp[0][0]

        if num == temp[-1][-1]:
            print("yes")
            break


def factors(x, dont_search):
    result = []
    i = 1
    while i * i <= x:
        if x % i == 0:
            if [i, x / i] not in dont_search.values():
                result.append([i, x / i])
        i += 1
    return result


def optimized():
    rows = int(input())
    cols = int(input())

    room = []
    for i in range(rows):
        room.append(list(map(int, input().split(" "))))

    found = False

    cur_row = 0
    cur_col = 0
    index = 0
    searched = {}

    times_ran = 0
    while not found:
        times_ran += 1
        num = room[cur_row][cur_col]
        searched[index] = [cur_row, cur_col]
        index += 1

        num_factors = factors(num, searched)

        for factor in num_factors:
            try:
                cur_row = int(factor[0] - 1)
                cur_col = int(factor[-1] - 1)
                num = room[cur_row][cur_col]
            except IndexError or ValueError:
                continue

        if cur_row == rows - 1 and cur_col == cols - 1:
            print("yes")
            found = True
        if times_ran > 1000:
            print("no")
            found = True
optimized()
