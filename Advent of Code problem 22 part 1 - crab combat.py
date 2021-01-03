#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv


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
    
while deck[0]!=[] and deck[1]!=[]:
    winner,loser = (0,1) if deck[0][0]>deck[1][0] else (1,0)
    deck[winner].append(deck[winner][0])
    deck[winner].append(deck[loser][0])
    del deck[winner][0]
    del deck[loser][0]
        
total_score = 0
for i in range(-1,-len(deck[winner])-1,-1):
    total_score -= i*deck[winner][i]
                  
print(f'Final score: {total_score}')
end = timeit()
print(f'Solution time: {end-start}')