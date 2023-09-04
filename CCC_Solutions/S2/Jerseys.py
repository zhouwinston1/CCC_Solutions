num_of_jerseys = int(input())
num_of_players = int(input())


possible_jerseys = {}
for i in range(1, num_of_jerseys + 1):
    possible_jerseys[i] = input()

wanted_jerseys = {}
for i in range(num_of_players):
    temp = input().split(" ")
    temp2 = temp[0]
    temp3 = int(temp[-1])

    if temp3 in wanted_jerseys.keys():
        temp4 = wanted_jerseys[temp3]
        wanted_jerseys[temp3] = temp4, temp2
    else:
        wanted_jerseys[temp3] = temp2

satisfied = 0
used_jerseys = {}
#
# print(possible_jerseys)
# print(wanted_jerseys)

for jersey_number, jersey_size in wanted_jerseys.items():
    for another_jersey in wanted_jerseys[jersey_number]:
        if another_jersey == possible_jerseys[jersey_number]:
            if wanted_jerseys[jersey_number] in used_jerseys:
                continue
            satisfied += 1
            used_jerseys[jersey_number] = jersey_number

print(satisfied)