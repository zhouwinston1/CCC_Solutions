rows = int(input())
cols = int(input())

canvas = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append("B")
    canvas.append(row)

golds = 0

for i in range(int(input())):
    row_or_col, index = input().split()
    index = int(index) - 1

    if row_or_col == 'R':
        for j in range(cols):
            if canvas[index][j] == 'G':
                canvas[index][j] = "B"
                golds -= 1
            else:
                canvas[index][j] = "G"
                golds += 1
    else:
        for j in range(rows):
            if canvas[j][index] == 'G':
                canvas[j][index] = "B"
                golds -= 1
            else:
                canvas[j][index] = "G"
                golds += 1

print(golds)


def q5():
    rows = int(input())
    cols = int(input())
    num_lins = int(input())

    row_swipes = [False] * (rows + 1)
    col_swipes = [False] * (cols + 1)

    for i in range(num_lins):
        raw_line_info = input()
        raw_line_info = raw_line_info.split(" ")
        index = int(raw_line_info[-1])
        if raw_line_info[0] == "R":
            row_swipes[index] = not row_swipes[index]
        else:
            col_swipes[index] = not col_swipes[index]

    canvas = [[False] * (cols + 1) for i in range((rows + 1))]

    for i in range(1, rows + 1):
        if row_swipes[i]:
            for j in range(1, cols + 1):
                canvas[i][j] = not canvas[i][j]

    for i in range(1, cols + 1):
        if col_swipes[i]:
            for j in range(1, rows + 1):
                canvas[j][i] = not canvas[j][i]

    count = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if canvas[i][j]:
                count += 1

    print(count)


q5()

def good_groups():
    freinds = {}
    enemies = {}
    groups = []
    temp = []
    constraints = 0
    for i in range(int(input())):
        temp = input().split()
        if temp[0] in freinds:
            freinds[temp[0]].append(temp[1])
        else:
            freinds[temp[0]] = [temp[1]]
        if temp[1] in freinds:
            freinds[temp[1]].append(temp[1])
        else:
            freinds[temp[1]] = [temp[0]]
    for i in range(int(input())):
        temp = input().split()
        if temp[0] in enemies:
            enemies[temp[0]].append(temp[1])
        else:
            enemies[temp[0]] = [temp[1]]
        if temp[1] in enemies:
            enemies[temp[1]].append(temp[0])
        else:
            enemies[temp[1]] = [temp[0]]
    for i in range(int(input())):
        groups = input().split()
        for j in range(len(groups)):
            if groups[j] in enemies and enemies[groups[j]] in groups:
                constraints += 1
            if groups[j] in freinds and freinds[groups[j]] not in groups:
                constraints += 1
    return constraints//2


print(good_groups())