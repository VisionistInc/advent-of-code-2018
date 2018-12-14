with open('input', 'r') as file:
    input = file.read()

lines = input.split('\n')

# creating a map from the input
# if a cart is present, put its details next to the road
# like direction and which way it is supposed to turn next
paths = []
count = 0
for line in lines:
    row = []
    for c in line:
        if c == '^':
            row.append('|^L')
            count += 1
        elif c == 'v':
            row.append('|vL')
            count += 1
        elif c == '<':
            row.append('-<L')
            count += 1
        elif c == '>':
            row.append('->L')
            count += 1
        else:
            row.append(c)
    paths.append(list(row))

HEIGHT = len(paths)
WIDTH = len(paths[0])

first_crash = True

def assign_cart(x,y, cart):
    '''
    This helper function takes a new road and puts a cart
    on it, checking for crashes
    '''
    global first_crash

    new_loc = paths[y][x]

    # if the new location already has a cart
    # display crash info and remove cart info
    if len(new_loc) > 1:
        if first_crash:
            print("Part 1: ",x,y)
            first_crash = False
        else:
            print("Crash at: ",x,y)
        paths[y][x] = new_loc[:1]
        return
    
    # break string up
    cart = list(cart)

    # determine cart direction based on new location
    if new_loc == '\\':
        if cart[0] == '<':
            cart[0] = '^'
        elif cart[0] == '^':
            cart[0] = '<'
        elif cart[0] == '>':
            cart[0] = 'v'
        else:
            cart[0] = '>'
    elif new_loc == '/':
        if cart[0] == '<':
            cart[0] = 'v'
        elif cart[0] == 'v':
            cart[0] = '<'
        elif cart[0] == '>':
            cart[0] = '^'
        else:
            cart[0] = '>'
    elif new_loc == '+':
        if cart[1] == 'L':
            cart[1] = 'S'
            if cart[0] == '<':
                cart[0] = 'v'
            elif cart[0] == 'v':
                cart[0] = '>'
            elif cart[0] == '>':
                cart[0] = '^'
            else:
                cart[0] = '<'
        elif cart[1] == 'S':
            cart[1] = 'R'
        else:
            cart[1] = 'L'
            if cart[0] == '<':
                cart[0] = '^'
            elif cart[0] == '^':
                cart[0] = '>'
            elif cart[0] == '>':
                cart[0] = 'v'
            else:
                cart[0] = '<'

    # join string back up
    cart = ''.join(cart)

    # append cart data to new location
    # we add an * to indicate we alrady saw it this pass
    paths[y][x] = new_loc + cart + '*'

count = 0

# until we get down to 1 cart
while count != 1:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # if spot is only 1 long, it doesn't have a cart
            if len(paths[y][x]) == 1:
                continue
            # if spot has an * it has a cart already moved this round
            if '*' in paths[y][x]:
                continue
            # remove cart data from this spot
            cart = paths[y][x][1:]
            paths[y][x] = paths[y][x][:1]

            # assign cart data to the new spot
            if cart[0] == '^':
                assign_cart(x,y-1, cart)
            elif cart[0] == 'v':
                assign_cart(x,y+1, cart)
            elif cart[0] == '<':
                assign_cart(x-1,y, cart)
            else:
                assign_cart(x+1,y, cart)
    
    # count how many carts are left
    # and clear out any * so the car will get
    # evaluated the next round
    count = 0
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if len(paths[y][x]) == 4:
                count += 1
                saved_x = x
                saved_y = y
                paths[y][x] = paths[y][x][:3]
    
print("Part 2: ", saved_x, saved_y)