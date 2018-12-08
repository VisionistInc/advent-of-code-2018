twiceCounter = 0
thriceCounter = 0

with open('./input.txt') as file:
    for line in file:
        incTwice = False
        incThrice = False
        for letter in line:
            if line.count(letter) == 2:
                incTwice = True
            elif line.count(letter) == 3:
                incThrice = True
        if (incTwice == True): twiceCounter += 1
        if (incThrice == True): thriceCounter += 1

print(twiceCounter * thriceCounter)