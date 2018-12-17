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

totalCount = 0

A = 1
B = 2
C = 3


for before, instruction, after in instructions:
    curInstructionCount = 0

    #addr
    if before[instruction[A]] + before[instruction[B]] == after[instruction[C]]:
        curInstructionCount += 1
    #addi
    if before[instruction[A]] + instruction[B] == after[instruction[C]]:
        curInstructionCount += 1
    #mulr
    if before[instruction[A]] * before[instruction[B]] == after[instruction[C]]:
        curInstructionCount += 1
    #muli
    if before[instruction[A]] * instruction[B] == after[instruction[C]]:
        curInstructionCount += 1
    #banr
    if before[instruction[A]] & before[instruction[B]] == after[instruction[C]]:
        curInstructionCount += 1
    #bani
    if before[instruction[A]] & instruction[B] == after[instruction[C]]:
        curInstructionCount += 1
    #borr
    if before[instruction[A]] | before[instruction[B]] == after[instruction[C]]:
        curInstructionCount += 1
    #bori
    if before[instruction[A]] | instruction[B] == after[instruction[C]]:
        curInstructionCount += 1
    #setr
    if before[instruction[A]] == after[instruction[C]]:
        curInstructionCount += 1
    #seti
    if instruction[A] == after[instruction[C]]:
        curInstructionCount += 1
    #gtir
    if ((instruction[A] > before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((instruction[A] <= before[instruction[B]]) and after[instruction[C]] == 0):
        curInstructionCount += 1
    #gtri
    if ((before[instruction[A]] > instruction[B]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] <= instruction[B]) and after[instruction[C]] == 0):
        curInstructionCount += 1
    #gtrr
    if ((before[instruction[A]] > before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] <= before[instruction[B]]) and after[instruction[C]] == 0):
        curInstructionCount += 1
    #eqir
    if ((instruction[A] == before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((instruction[A] != before[instruction[B]]) and after[instruction[C]] == 0):
        curInstructionCount += 1
    #eqri
    if ((before[instruction[A]] == instruction[B]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] != instruction[B]) and after[instruction[C]] == 0):
        curInstructionCount += 1
    #eqrr
    if ((before[instruction[A]] == before[instruction[B]]) and after[instruction[C]] == 1) or \
       ((before[instruction[A]] != before[instruction[B]]) and after[instruction[C]] == 0):
        curInstructionCount += 1

    if curInstructionCount >= 3:
        totalCount += 1

print(totalCount)