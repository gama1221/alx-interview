#!/usr/bin/python3
import sys

possibilties = []
for line in sys.stdin:
    try:
        possibilties.append(eval(line))
    except Exception as e:
        pass

def check_two_queens(new_queen_position, other_queen_position):
    if new_queen_position[0] == other_queen_position[0] or new_queen_position[1] == other_queen_position[1]:
        return False
    if new_queen_position[0] + new_queen_position[1] == other_queen_position[0] + other_queen_position[1]:
        return False
    if new_queen_position[0] - new_queen_position[1] == other_queen_position[0] - other_queen_position[1]:
        return False
    return True


def possibilty_already_done(possibilty, possibilties_done):
    if len(possibilties_done) == 0:
        return False
    for possibilty_done in possibilties_done:
        nb_similar = 0
        for position in possibilty:
            nb_similar += 1 if position in possibilty_done else 0
        if nb_similar == len(possibilty_done):
            return True
    return False

result = True
possibilties_done = []
for possibilty in possibilties:
    i = 0
    while i < len(possibilty) -1:
        j = i + 1
        while j < len(possibilty):
            result = check_two_queens(possibilty[i], possibilty[j])
            if not result:
                break
            j += 1
        i += 1
        if not result:
            break
    if not result:
        break
    else:
        # good possibilty
        if possibilty_already_done(possibilty, possibilties_done):
            result = False
        else:
            possibilties_done.append(possibilty)

    if not result:
        break
    

if result:
    print("OK")
else:
    print("NOK")
print(len(possibilties))