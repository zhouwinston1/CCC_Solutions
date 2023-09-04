def j4():
    violated = 0

    x = int(input())
    must_groups = {}
    len1 = 0
    for i in range(x):
        must_groups[i] = input().split()
        len1 += 1

    y = int(input())
    not_groups = {}
    len2 = 0
    for i in range(y):
        not_groups[i] = input().split()
        len2 += 1

    g = int(input())
    groups = {}
    counter = 0

    for i in range(g):
        groups[i] = input().split()
        counter += 1

    def in_group(people, groups):
        for key, group in groups.items():
            group.sort()
            people = set(people)
            sorted(people)

            if set(people).issubset(group):
                return True
        return False

    if len1 > len2:
        temp = len1
        temp2 = len2
    else:
        temp = len2
        temp2 = len1

    for i in range(temp):
        if i <= temp2 - 1:
            if not in_group(must_groups[i], groups):
                violated += 1
            if in_group(not_groups[i], groups):
                violated += 1
        else:
            if temp == len2:
                if in_group(not_groups[i], groups):
                    violated += 1
            else:
                if not in_group(must_groups[i], groups):
                    violated += 1

    print(violated)


j4()