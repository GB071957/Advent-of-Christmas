#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import copy

full_cups = list('459672813')
full_cups = [int(i) for i in full_cups]
list_len = 1000001

pointers = [0]*(len(full_cups)+1)

for i in range(0,len(full_cups)-1):
    pointers[full_cups[i]] = full_cups[i+1]
pointers[0] = full_cups[0]
pointers[full_cups[-1]] = len(full_cups)+1
#pointers[full_cups[-1]] = full_cups[0]    # FOR TEST ONLY
rest = [j+1 for j in range(len(full_cups)+1,list_len)]
pointers = pointers + rest
pointers[-1] = pointers[0]

cc_ix = pointers[0]
for k in range(0,10000000):
    
    move_cups = [pointers[cc_ix]]
    for m in range(1,3):
        move_cups.append(pointers[move_cups[m-1]])
    dc_ix = cc_ix - 1 if cc_ix>1 else list_len-1
    while dc_ix in move_cups:
        dc_ix = dc_ix-1 if dc_ix>1 else list_len-1
    
    x = pointers[cc_ix]
    pointers[cc_ix] = pointers[move_cups[-1]]
    pointers[move_cups[-1]]=pointers[dc_ix]
    pointers[dc_ix] = x
    cc_ix = pointers[cc_ix]

                  
print(f'Result: {pointers[1]*pointers[pointers[1]]}')
end = timeit()
print(f'Solution time: {end-start}')