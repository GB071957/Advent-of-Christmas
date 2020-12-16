#   Advent of Code problem 15 part 2 - Rambunctious Recitation - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv


#starting_nums = [16,1,0,18,12,14,19]
nums_seen = [16,1,0,18,12,14]
turns_seen = [1,2,4,5,6]

turns = [0]*30000001
for i in range(len(nums_seen)):
    if nums_seen[i] != 0:
        turns[nums_seen[i]] = i+1
        
turn = 7
zero_turns = 3

last_num = 19
while turn<30000000:
    
    #print(f'Turn: {turn} lastnum: {last_num}')
    if last_num == 0:
        
        last_num = turn - zero_turns
        zero_turns = turn
    else:
        if turns[last_num] == 0:
            ln = 0
        else:
            ln = turn - turns[last_num]
        turns[last_num] = turn
        last_num = ln
        
    turn+=1

print(f'Last value spoken: {last_num}')
end = timeit()
print(f'Solution time: {end-start}')