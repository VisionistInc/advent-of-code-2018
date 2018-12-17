import re

with open('input', 'r') as file:
    input = file.read()

top_half, bot_half = input.split('\n\n\n\n')

regs = [0,0,0,0]

def addr(a,b,c):
    regs[c] = regs[a] + regs[b]

def addi(a,b,c):
    regs[c] = regs[a] + b

def mulr(a,b,c):
    regs[c] = regs[a] * regs[b]

def muli(a,b,c):
    regs[c] = regs[a] * b

def banr(a,b,c):
    regs[c] = regs[a] & regs[b]

def bani(a,b,c):
    regs[c] = regs[a] & b

def borr(a,b,c):
    regs[c] = regs[a] | regs[b]

def bori(a,b,c):
    regs[c] = regs[a] | b

def setr(a,b,c):
    regs[c] = regs[a]

def seti(a,b,c):
    regs[c] = a

def gtir(a,b,c):
    if a > regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

def gtri(a,b,c):
    if regs[a] > b:
        regs[c] = 1
    else:
        regs[c] = 0

def gtrr(a,b,c):
    if regs[a] > regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

def eqir(a,b,c):
    if a == regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

def eqri(a,b,c):
    if regs[a] == b:
        regs[c] = 1
    else:
        regs[c] = 0

def eqrr(a,b,c):
    if regs[a] == regs[b]:
        regs[c] = 1
    else:
        regs[c] = 0

examples = top_half.split('\n\n')

func_list = [addi,addr,muli,mulr,bani,banr,bori,borr,setr,seti,gtir,gtri,gtrr,eqri,eqir,eqrr]

known = [None] * 16
unknown = list(func_list)

match_three_count = 0
for example in examples:
    nums = re.findall(r'-?\d+', example)
    before = [ int(x) for x in nums[:4] ]
    inst   = [ int(x) for x in nums[4:8] ]
    after  = [ int(x) for x in nums[8:] ]

    match_count = 0
    for func in func_list:
        regs = list(before)
        func(inst[1], inst[2], inst[3])
        if regs == after:
            match_count += 1
    
    if match_count >= 3:
        match_three_count += 1

print("Part 1: ", match_three_count)

known = [None] * 16
unknown = list(func_list)

while len(unknown) > 0:
    for example in examples:
        nums = re.findall(r'-?\d+', example)
        before = [ int(x) for x in nums[:4] ]
        inst   = [ int(x) for x in nums[4:8] ]
        after  = [ int(x) for x in nums[8:] ]

        # if we already know what this opcode is, skip
        if known[inst[0]] != None:
            continue

        match_list = []
        # test against all unknown functions
        for func in unknown:
            regs = list(before)
            func(inst[1], inst[2], inst[3])
            if regs == after:
                match_list.append(func)
        
        # if there is only one match to unknown
        if len(match_list) == 1:
            unknown.remove(match_list[0])
            known[inst[0]] = match_list[0]

regs=[0,0,0,0]

for line in bot_half.split('\n'):
    n = line.split()
    n = [ int(x) for x in n ]
    known[n[0]](n[1],n[2],n[3])

print("Part 2: ", regs[0])