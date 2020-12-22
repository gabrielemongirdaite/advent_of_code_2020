import time
import copy


def one_round(deck_1, deck_2):
    if deck_1[0] > deck_2[0]:
        deck_1.extend([deck_1[0]])
        deck_1.extend([deck_2[0]])
    else:
        deck_2.extend([deck_2[0]])
        deck_2.extend([deck_1[0]])
    return deck_1[1:], deck_2[1:]


def find_winner(deck_1, deck_2, which_round):
    while len(deck_1) != 0 and len(deck_2) != 0:
        deck_1, deck_2 = which_round(deck_1, deck_2)
    if len(deck_1) == 0:
        winner = 'player_2'
    else:
        winner = 'player_1'
    return deck_1+deck_2, winner


def find_winner_part_2(deck_1, deck_2, which_round):
    pairs1 = []
    pairs2 = []
    while len(deck_1) != 0 and len(deck_2) != 0:
        if deck_1 in pairs1 and deck_2 in pairs2:
            winner = 'player_1'
            return deck_1+deck_2, winner
        else:
            pairs1.append(copy.deepcopy(deck_1))
            pairs2.append(copy.deepcopy(deck_2))
            deck_1, deck_2 = which_round(deck_1, deck_2, which_round)

    if len(deck_1) == 0:
        winner = 'player_2'
    else:
        winner = 'player_1'
    return deck_1+deck_2, winner


def one_round_part_2(dck_1, dck_2, which_round):
    if (len(dck_1[1:]) >= dck_1[0] and len(dck_2[1:]) >= dck_2[0]):
        win = find_winner_part_2(copy.deepcopy(dck_1[1:dck_1[0]+1]), copy.deepcopy(dck_2[1:dck_2[0]+1]), which_round)[1]
        if win == 'player_2':
            dck_2.extend([dck_2[0]])
            dck_2.extend([dck_1[0]])
        else:
            dck_1.extend([dck_1[0]])
            dck_1.extend([dck_2[0]])
    elif dck_1[0] > dck_2[0]:
        dck_1.extend([dck_1[0]])
        dck_1.extend([dck_2[0]])
    else:
        dck_2.extend([dck_2[0]])
        dck_2.extend([dck_1[0]])
    return dck_1[1:], dck_2[1:]


player_1 = [31, 33, 27, 43, 29, 25, 36, 11, 15, 5, 14, 34, 7, 18, 26, 41, 19, 45, 12, 1, 8, 35, 44, 30, 50]
player_2 = [42, 40, 6, 17, 3, 16, 22, 23, 32, 21, 24, 46, 49, 48, 38, 47, 13, 9, 39, 20, 10, 2, 37, 28, 4]

start_time = time.time()
winner = find_winner(copy.deepcopy(player_1), copy.deepcopy(player_2), one_round)[0]
answer = 0
for idx, i in enumerate(winner):
    answer += i * (len(winner) - idx)

print('1st part answer: ', answer)
print("--- %s seconds for 1st part---" % (time.time() - start_time))

winner = find_winner_part_2(player_1, player_2, one_round_part_2)[0]

answer = 0
for idx, i in enumerate(winner):
    answer += i * (len(winner) - idx)

print('2nd part answer: ', answer)
print("--- %s seconds for 2nd part---" % (time.time() - start_time))