fp = open("input.txt")

instructions = []

for curLine in fp:
    if len(curLine) < 9:
        break
    before = list(map(int, curLine[9:-2].split(', ')))
    instruction = list(map(int, fp.readline()[:-1].split(' ')))
    after = list(map(int, fp.readline()[9:-2].split(', ')))
    fp.readline()

    instructions.append((before, instruction, after))

OPCODE = 0
A = 1
B = 2
C = 3

opcodeMap = [range(16)] * 16
ADDR_MAP = 0
ADDI_MAP = 1
MULR_MAP = 2
MULI_MAP = 3
BANR_MAP = 4
BANI_MAP = 5
BORR_MAP = 6
BORI_MAP = 7
SETR_MAP = 8
SETI_MAP = 9
GTIR_MAP = 10
GTRI_MAP = 11
GTRR_MAP = 12
EQIR_MAP = 13
EQRI_MAP = 14
EQRR_MAP = 15


for before, instruction, after in instructions:
    possibleInstrs = []

    #addr
    if before[instruction[A]] + before[instruction[B]] == after[instruction[C]]:
        possibleInstrs.append(ADDR_MAP)
    #addi
    if before[instruction[A]] + instruction[B] == after[instruction[C]]:
        possibleInstrs.append(ADDI_MAP)
    #mulr
    if before[instruction[A]] * before[instruction[B]] == after[instruction[C]]:
        possibleInstrs.append(MULR_MAP)
    #muli
    if before[instruction[A]] * instruction[B] == after[instruction[C]]:
        possibleInstrs.append(MULI_MAP)
    #banr
    if before[instruction[A]] & before[instruction[B]] == after[instruction[C]]:
        possibleInstrs.append(BANR_MAP)
    #bani
    if before[instruction[A]] & instruction[B] == after[instruction[C]]:
        possibleInstrs.append(BANI_MAP)
    #borr
    if before[instruction[A]] | before[instruction[B]] == after[instruction[C]]:
        possibleInstrs.append(BORR_MAP)
    #bori
    if before[instruction[A]] | instruction[B] == after[instruction[C]]:
        possibleInstrs.append(BORI_MAP)
    #setr
    if before[instruction[A]] == after[instruction[C]]:
        possibleInstrs.append(SETR_MAP)
    #seti
    if instruction[A] == after[instruction[C]]:
        possibleInstrs.append(SETI_MAP)
    #gtir
    if ((instruction[A] > before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((instruction[A] <= before[instruction[B]]) and after[instruction[C]] == 0):
        possibleInstrs.append(GTIR_MAP)
    #gtri
    if ((before[instruction[A]] > instruction[B]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] <= instruction[B]) and after[instruction[C]] == 0):
        possibleInstrs.append(GTRI_MAP)
    #gtrr
    if ((before[instruction[A]] > before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] <= before[instruction[B]]) and after[instruction[C]] == 0):
        possibleInstrs.append(GTRR_MAP)
    #eqir
    if ((instruction[A] == before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((instruction[A] != before[instruction[B]]) and after[instruction[C]] == 0):
        possibleInstrs.append(EQIR_MAP)
    #eqri
    if ((before[instruction[A]] == instruction[B]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] != instruction[B]) and after[instruction[C]] == 0):
        possibleInstrs.append(EQRI_MAP)
    #eqrr
    if ((before[instruction[A]] == before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] != before[instruction[B]]) and after[instruction[C]] == 0):
        possibleInstrs.append(EQRR_MAP)

    opcodeMap[instruction[OPCODE]] = [x for x in possibleInstrs if x in opcodeMap[instruction[OPCODE]]]
    if len(opcodeMap[instruction[OPCODE]]) == 1:
        for i in range(16):
            if i != instruction[OPCODE]:
                opcodeMap[i] = [x for x in opcodeMap[i] if x != opcodeMap[instruction[OPCODE]][0]]

programText = []

for curLine in fp:
    if len(curLine) >  7:
        programText.append(tuple(map(int, curLine.strip().split(' '))))

regs = [0, 0, 0, 0]

for instruction in programText:
    if opcodeMap[instruction[OPCODE]][0] == ADDR_MAP:
        regs[instruction[C]] = regs[instruction[A]] + regs[instruction[B]]
    elif opcodeMap[instruction[OPCODE]][0] == ADDI_MAP:
        regs[instruction[C]] = regs[instruction[A]] + instruction[B]
    elif opcodeMap[instruction[OPCODE]][0] == MULR_MAP:
        regs[instruction[C]] = regs[instruction[A]] * regs[instruction[B]]
    elif opcodeMap[instruction[OPCODE]][0] == MULI_MAP:
        regs[instruction[C]] = regs[instruction[A]] * instruction[B]
    elif opcodeMap[instruction[OPCODE]][0] == BANR_MAP:
        regs[instruction[C]] = regs[instruction[A]] & regs[instruction[B]]
    elif opcodeMap[instruction[OPCODE]][0] == BANI_MAP:
        regs[instruction[C]] = regs[instruction[A]] & instruction[B]
    elif opcodeMap[instruction[OPCODE]][0] == BORR_MAP:
        regs[instruction[C]] = regs[instruction[A]] | regs[instruction[B]]
    elif opcodeMap[instruction[OPCODE]][0] == BORI_MAP:
        regs[instruction[C]] = regs[instruction[A]] | instruction[B]
    elif opcodeMap[instruction[OPCODE]][0] == SETR_MAP:
        regs[instruction[C]] = regs[instruction[A]]
    elif opcodeMap[instruction[OPCODE]][0] == SETI_MAP:
        regs[instruction[C]] = instruction[A]
    elif opcodeMap[instruction[OPCODE]][0] == GTIR_MAP:
        if instruction[A] > regs[instruction[B]]:
            regs[instruction[C]] = 1
        else:
            regs[instruction[C]] = 0
    elif opcodeMap[instruction[OPCODE]][0] == GTRI_MAP:
        if regs[instruction[A]] > instruction[B]:
            regs[instruction[C]] = 1
        else:
            regs[instruction[C]] = 0
    elif opcodeMap[instruction[OPCODE]][0] == GTRR_MAP:
        if regs[instruction[A]] > regs[instruction[B]]:
            regs[instruction[C]] = 1
        else:
            regs[instruction[C]] = 0
    elif opcodeMap[instruction[OPCODE]][0] == EQIR_MAP:
        if instruction[A] == regs[instruction[B]]:
            regs[instruction[C]] = 1
        else:
            regs[instruction[C]] = 0
    elif opcodeMap[instruction[OPCODE]][0] == EQRI_MAP:
        if regs[instruction[A]] == instruction[B]:
            regs[instruction[C]] = 1
        else:
            regs[instruction[C]] = 0
    elif opcodeMap[instruction[OPCODE]][0] == EQRR_MAP:
        if regs[instruction[A]] == regs[instruction[B]]:
            regs[instruction[C]] = 1
        else:
            regs[instruction[C]] = 0

print(regs[0])
