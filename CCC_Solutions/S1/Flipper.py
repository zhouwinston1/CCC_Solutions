text = input().split()
flips = [str(num) for num in str(text)]

arr1 = [1, 2]
temp1 = 0
arr2 = [3, 4]
temp2 = 0

for check in flips:
    if check == "V":
        temp1 = arr1[-1]
        arr1[-1] = arr1[0]
        arr1[0] = temp1
        temp2 = arr2[-1]
        arr2[-1] = arr2[0]
        arr2[0] = temp2
    elif check == "H":
        temp1 = arr2[0]
        arr2[0] = arr1[0]
        arr1[0] = temp1
        temp2 = arr2[-1]
        arr2[-1] = arr1[-1]
        arr1[-1] = temp2
print(str(arr1[0]) + " " + str(arr1[-1]))
print(str(arr2[0]) + " " + str(arr2[-1]))