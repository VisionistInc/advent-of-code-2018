tests = ["51589", "01245", "92510", "59414", "635041"]

for test in tests:
    recipes = "37"
    elf1 = 0
    elf2 = 1

    while True:
        elf1Score = int(recipes[elf1])
        elf2Score = int(recipes[elf2])
        recipes += str(elf1Score + elf2Score)
        elf1 = (1 + elf1Score + elf1) % len(recipes)
        elf2 = (1 + elf2Score + elf2)  % len(recipes)
        if recipes[-len(test):] == test:
            break
        elif  elf1Score + elf2Score > 9:
            if recipes[-len(test)-1:-1] == test:
                recipes = recipes[:-1]
                break

    print(len(recipes) - len(test))
