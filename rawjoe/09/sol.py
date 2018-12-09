with open('input', 'r') as file:
    input = file.read()

parts = input.split()

players = int(parts[0])
max_marble = int(parts[6])

# at first i used python lists
# big mistake for part 2
class Node:
    def __init__(self, val, prev):
        self.val = val
        if prev == None:
            self.prev=self
            self.next =self
        else:
            self.prev = prev
            self.next = prev.next
            prev.next.prev = self
            prev.next = self
    
    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev


def solve(num_players, last_marble):
    score = [0] * num_players
    cur_player = 0

    cur_node = Node(0,None)

    for i in range(1, last_marble+1):
        if i % 23 == 0:
            score[cur_player] += i
            for _x in range(7):
                cur_node = cur_node.prev
            score[cur_player] += cur_node.val
            cur_node.remove()
            cur_node = cur_node.next
        else:
            cur_node = cur_node.next
            cur_node = Node(i, cur_node)

        cur_player = (cur_player + 1) % num_players
    
    return max(score)

print("Part 1: ", solve(players, max_marble))
print("Part 2: ", solve(players, max_marble*100))
