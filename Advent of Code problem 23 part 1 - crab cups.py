#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import copy

full_cups = list('459672813')
full_cups = [int(i) for i in full_cups]
list_len = len(full_cups)
rest = [i for i in range(list_len+1,1001)]
full_cups = full_cups + rest
rest = []
list_len = 100
partial_cups = []
cc_ix = 0
cc_val = full_cups[cc_ix]
dc_ix = 0
dc_val = 0
cups_to_move = []

for i in range(0,10000):    #STILL NOT RIGHT
    if cc_ix>=list_len-3:
        cups_to_move = full_cups[cc_ix+1:]+full_cups[0:4-(list_len-cc_ix)]
    else:
        cups_to_move = full_cups[cc_ix+1:cc_ix+4]
    for j in range(0,3):
        full_cups.remove(cups_to_move[j])
        
    dc_val = (cc_val-1) if cc_val>1 else cc_val-1+list_len
    while dc_val in cups_to_move:
        dc_val -= 1
        if dc_val <=0:
            dc_val = max(full_cups)
    dc_ix = full_cups.index(dc_val)
    
    full_cups = full_cups[0:dc_ix+1]+cups_to_move+full_cups[dc_ix+1:]
    cc_ix = (full_cups.index(cc_val) +1) % list_len
    cc_val = full_cups[cc_ix]

starting_point = (full_cups.index(1)+1) % list_len
final_list = full_cups[starting_point:]+full_cups[0:starting_point-1]
                  
print(f'Final cup labels: {"".join([str(integer) for integer in final_list])}')
end = timeit()
print(f'Solution time: {end-start}')