tests = [9, 5, 18, 2018, 635041]



for test in tests:
    recipes = "37"
    elf1 = 0
    elf2 = 1
    while len(recipes) < test + 10:
        elf1Score = int(recipes[elf1])
        elf2Score = int(recipes[elf2])
        recipes += str(elf1Score + elf2Score)
        elf1 = (1 + elf1Score + elf1) % len(recipes)
        elf2 = (1 + elf2Score + elf2)  % len(recipes)
    print(recipes[test:test+10])