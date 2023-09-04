import math

checking = True
A = 0
B = 0

while checking:
    userinput = input().split()
    if userinput[0] == "1":
        if userinput[1] == "A":
            A = int(userinput[-1])
        else:
            B = int(userinput[-1])
    elif userinput[0] == "2":
        if userinput[1] == "A":
            print(A)
        else:
            print(B)
    elif userinput[0] == "3":
        if userinput[1] == "A":
            A += B
        else:
            B += A
    elif userinput[0] == "4":
        if userinput[1] == "A":
            A *= B
        else:
            B *= A
    elif userinput[0] == "5":
        if userinput[1] == "A":
            A -= B
        else:
            B -= A
    elif userinput[0] == "6":
        if userinput[1] == "A":
            A = math.floor(A / B)
        else:
            B = math.floor(B / A)
    else:
        break
