word = input()

alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
vowels = "a e i o u".split(" ")

newlist = []

vnum = 1
cnum = 1

for letter in word:
    newlist.append(letter)

    if letter in vowels:
        continue

    else:

        for vowelcheck in range(1000):
            nextvoweladd = alphabet.index(letter) + vnum
            nextvowelsubtract = alphabet.index(letter) - vnum

            if nextvoweladd >= 26:

                if alphabet[nextvowelsubtract] in vowels:
                    newlist.append(alphabet[nextvowelsubtract])
                    vnum = 0
                    break

                else:
                    vnum += 1
                    continue

            elif nextvoweladd < 26:
                if alphabet[nextvowelsubtract] in vowels:
                    newlist.append(alphabet[nextvowelsubtract])
                    vnum = 0
                    break

                elif alphabet[nextvoweladd] in vowels:
                    newlist.append(alphabet[nextvoweladd])
                    vnum = 0
                    break

                else:
                    vnum += 1
                    continue

        if letter == "z":
            newlist.append(alphabet[-1])
            continue

        for consonantcheck in range(100):
            nextconsonantadd = alphabet.index(letter) + cnum

            if alphabet[nextconsonantadd] not in vowels:
                newlist.append(alphabet[nextconsonantadd])
                cnum = 1
                break

            else:
                cnum += 1
                continue

print("".join(newlist))





