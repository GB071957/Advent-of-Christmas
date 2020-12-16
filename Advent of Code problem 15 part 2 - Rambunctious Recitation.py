#   Advent of Code problem 15 part 2 - Rambunctious Recitation - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv


starting_nums = [16,1,0,18,12,14,19]
nums_seen = [16,1,18,12,14]
turns_seen = [1,2,4,5,6]
turn = 7
zero_turns = 3

last_num = 19
while turn<300000:
    
    print(f'Turn: {turn} lastnum: {last_num}')
    if last_num in nums_seen:
        ix = nums_seen.index(last_num)
        last_num = turn-turns_seen[ix]
        turns_seen[ix] = turn
    else:
        nums_seen.append(last_num)
        turns_seen.append(turn)
        last_num = turn+1-zero_turns
        zero_turns = turn+1
        turn+=1        
    turn+=1

print(f'Last value spoken: {last_num}')
end = timeit()
print(f'Solution time: {end-start}')