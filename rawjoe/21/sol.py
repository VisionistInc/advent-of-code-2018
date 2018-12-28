r0 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
r5 = 0

answers = []

while True:
    r2 = r3 | 65536
    r3 = 1397714
    while True:
        r5 = r2 & 255
        r3 += r5
        r3 &= 16777215
        r3 *= 65899
        r3 &= 16777215
        if 256 > r2:
            if r3 in answers:
                print("Part 1: ", answers[0])
                print("Part 2: ", answers[-1])
                exit()
            answers.append(r3)
            break
        r2 = r2 // 256