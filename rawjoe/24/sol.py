from copy import deepcopy

with open('input', 'r') as file:
    input = file.read()

# clean up the input
input = input.replace(' units each with ','|')
input = input.replace(' hit points (','|')
input = input.replace(' hit points ','|')
input = input.replace(') with an attack that does ','|')
input = input.replace('with an attack that does ','|')
input = input.replace(' damage at initiative ','|')

class Group:
    def __init__(self, props, id):
        props = props.split('|')
        self.id = id
        self.units = int(props[0])
        self.hp = int(props[1])
        self.weak = ''
        self.immune = ''
        traits = props[2].split(';')
        for t in traits:
            if 'weak' in t:
                self.weak = t
            if 'immune' in t:
                self.immune = t
        attack = props[3].split()
        self.power = int(attack[0])
        self.weapon = attack[1]
        self.initiative = int(props[4])
        self.targeting = -1
        self.effective_power = self.power * self.units

immune,infection = input.split('\n\n')

immune_team = []
id = 0
for line in immune.split('\n'):
    if '|' in line:
        immune_team.append(Group(line, id))
        id += 1

infect_team = []
for line in infection.split('\n'):
    if '|' in line:
        infect_team.append(Group(line, id))
        id += 1

orig_immune = deepcopy(immune_team)
orig_infect = deepcopy(infect_team)

def update_ep_target(team):
    for group in team:
        group.effective_power = group.power * group.units
        group.targeting = -1

def target(offense,defense):
    targeted = []
    for i in range(len(offense)):
        aim = -1
        damage = 0
        opp_ep = 0
        opp_init = 0
        # check all enemies
        for group in defense:
            # if enemy already targeted or immune to us, skip
            if group.id in targeted:
                continue
            if offense[i].weapon in group.immune:
                continue
            # determine damage done
            local_damage = offense[i].effective_power
            if offense[i].weapon in group.weak:
                local_damage *= 2
            # if greater, save info
            if local_damage > damage:
                aim = group.id
                damage = local_damage
                opp_ep = group.effective_power
                opp_init = group.initiative
            # if same, check enemy effective power
            elif local_damage == damage:
                # if greater, save
                if group.effective_power > opp_ep:
                    aim = group.id
                    opp_ep = group.effective_power
                    opp_init = group.initiative
                # if same, check enemy initiative 
                elif group.effective_power == opp_ep:
                    if group.initiative > opp_init:
                        aim = group.id
                        opp_init = group.initiative
        # if we found someone to target, add to list
        if aim != -1:
            offense[i].targeting = aim
            targeted.append(aim)

boost = 0

infect_win = True
while infect_win:
    # new round, reset armies
    immune_team = deepcopy(orig_immune)
    infect_team = deepcopy(orig_infect)

    # add bost to this round
    for group in immune_team:
        group.power += boost

    while len(immune_team) > 0 and len(infect_team) > 0:
        # reset info
        update_ep_target(immune_team)
        update_ep_target(infect_team)

        # sort team by who will target first
        immune_team = sorted(immune_team, key=lambda x: (x.effective_power, x.initiative), reverse=True)
        infect_team = sorted(infect_team, key=lambda x: (x.effective_power, x.initiative), reverse=True)

        # perform targeting
        target(immune_team, infect_team)
        target(infect_team, immune_team)

        # group all teams together and sort who will attack first
        all_groups = immune_team + infect_team
        all_groups = sorted(all_groups, key=lambda x: x.initiative, reverse=True)

        # check for stalemate
        stalemate = True
        for group in all_groups:
            if group.targeting != -1:
                stalemate = False
        if stalemate:
            break

        # do the attacking
        for attacker in all_groups:
            defender = attacker.targeting
            for group in all_groups:
                if defender == group.id:
                    ep = attacker.units * attacker.power
                    if attacker.weapon in group.weak:
                        ep *= 2
                    units_killed = ep // group.hp
                    group.units = max(0, group.units-units_killed)

        # remove dead groups
        immune_team = sorted(immune_team, key=lambda x: x.units)
        infect_team = sorted(infect_team, key=lambda x: x.units)
        while len(immune_team) > 0 and immune_team[0].units == 0:
            immune_team.pop(0)
        while len(infect_team) > 0 and infect_team[0].units == 0:
            infect_team.pop(0)

    # done with a round, see who won
    total_units = 0
    if stalemate:
        boost += 1
    elif len(infect_team) > 0:
        for g in infect_team:
            total_units += g.units
        if boost == 0:
            print("Part 1: ", total_units)
        boost += 1
    else:
        for g in immune_team:
            total_units += g.units
        infect_win = False
        print("Part 2: ", total_units)