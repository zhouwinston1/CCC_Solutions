playlist = ["A", "B", "C", "D", "E"]
checking = True


def buttonOne():
    playlist[0], playlist[1], playlist[2], playlist[3], playlist[4] = playlist[1], playlist[2], playlist[3], playlist[4], playlist[0]


def buttonTwo():
    playlist[0], playlist[1], playlist[2], playlist[3], playlist[4] = playlist[4], playlist[0], playlist[1], playlist[2], playlist[3]


def buttonThree():
    playlist[0], playlist[1] = playlist[1], playlist[0]


while checking:
    b = int(input())
    n = int(input())

    if b == 1:
        for loop1 in range(n):
            buttonOne()

    elif b == 2:
        for loop2 in range(n):
            buttonTwo()

    elif b == 3:
        for loop3 in range(n):
            buttonThree()

    elif b == 4:
        print(" ".join(playlist))
        break
