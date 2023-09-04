start = input()
end = input()
energy = int(input())

startcords = [int(num1) for num1 in start.split(" ", 1)]
startx = int(startcords[0])
starty = int(startcords[-1])

endcords = [int(num2) for num2 in end.split(" ", 1)]
endx = int(endcords[0])
endy = int(endcords[-1])

tempsum1 = startx - endx
tempsum2 = starty - endy

if tempsum1 < 0:
    tempsum1 *= -1
if tempsum2 < 0:
    tempsum2 *= -1

realsum = tempsum2 + tempsum1

if realsum > energy:
    print("N")
else:

    if realsum % 2 == 0 and energy % 2 == 0:
        print("Y")
    elif realsum % 2 == 1 and energy % 2 == 1:
        print("Y")
    else:
        print("N")
