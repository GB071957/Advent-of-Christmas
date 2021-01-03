#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, copy

game = 0
rnd = 0

def play_game(deck):
    global game, rnd
    
    game +=1
    
    deck_tracker = [[[0][0]]]

    while deck[0]!=[] and deck[1]!=[]:
        rnd += 1
        #print(f'Game: {game}, round: {rnd}')
        if deck in deck_tracker:
            winner,loser = (0,1)
            break
        deck_tracker.append(copy.deepcopy(deck))
        if len(deck[0])>=deck[0][0]+1 and len(deck[1])>=deck[1][0]+1:  #play a recursive game
            r_deck = []
            r_deck.append(deck[0][1:deck[0][0]+1])
            r_deck.append(deck[1][1:deck[1][0]+1])
            r_deck,winner = play_game(r_deck)
            loser = (winner+1)%2
        else:
            winner,loser = (0,1) if deck[0][0]>deck[1][0] else (1,0)
        deck[winner].append(deck[winner][0])
        deck[winner].append(deck[loser][0])
        del deck[winner][0]
        del deck[loser][0]
    return deck,winner
    

with open("Advent of Code problem 22 - Crab Combat data.txt") as cc_file:
    file_contents = csv.reader(cc_file, delimiter='\n')

    i = 0
    deck = []
    for line in file_contents:
        
        if line == []:
            continue
        elif line[0][0:4] == 'Play':
            i += 1
            deck.append([])
        else:
            deck[i-1].append(int(line[0]))
            
deck,winner = play_game(deck)
        
total_score = 0
for i in range(-1,-len(deck[winner])-1,-1):
    total_score -= i*deck[winner][i]
                  
print(f'Final score: {total_score}')
end = timeit()
print(f'Solution time: {end-start}')