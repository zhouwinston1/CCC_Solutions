bowl1 = int(input())
bowl2 = int(input())
bowl3 = int(input())

if bowl2 < bowl1 < bowl3:
    print(bowl1)
elif bowl2 > bowl1 > bowl3:
    print(bowl1)
elif bowl1 < bowl2 < bowl3:
    print(bowl2)
elif bowl1 > bowl2 > bowl3:
    print(bowl2)
elif bowl1 < bowl3 < bowl2:
    print(bowl3)
elif bowl1 > bowl3 > bowl2:
    print(bowl3)