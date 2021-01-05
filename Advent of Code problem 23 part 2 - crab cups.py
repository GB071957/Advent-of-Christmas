#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import copy

full_cups = list('459672813')
full_cups = [int(i) for i in full_cups]
list_len = len(full_cups)
rest = [i for i in range(list_len+1,1000001)]
full_cups = full_cups + rest
rest = []
list_len = len(full_cups)
partial_cups = []
cc_ix = 0
cc_val = full_cups[cc_ix]

cups_to_move = []

for i in range(0,10000000):    #STILL NOT RIGHT
    move_cups = full_cups[cc_ix+1:cc_ix+4]
    dc_val = cc_val-1 if cc_val>1 else list_len
    while dc_val in move_cups:
        dc_val = dc_val-1 if dc_val>1 else list_len
        
    dc_ix = full_cups.index(dc_val)
    
    if dc_ix < cc_ix and dc_ix >0:
        full_cups = full_cups[0:dc_ix+1]+move_cups+full_cups[dc_ix+1:cc_ix+1]+full_cups[cc_ix+4:]
    elif cc_ix < dc_ix and cc_ix>0:
        full_cups = full_cups[0:cc_ix+1]+[dc_val]+move_cups+full_cups[cc_ix+4:dc_ix]+full_cups[dc_ix+1:]
    elif dc_ix<cc_ix and dc_ix==0:
        full_cups = [dc_val] + move_cups + full_cups[1:cc_ix+1]+full_cups[cc_ix+4:]
    else:   # cc_ix < dc_ix and cc_ix == 0
        full_cups = [cc_val]+full_cups[4:dc_ix+1]+move_cups+full_cups[dc_ix+1:]
    cc_ix += 1
    if cc_ix>list_len-3:
        full_cups = full_cups[cc_ix:]+full_cups[0:cc_ix]
        cc_ix = 0
    cc_val = full_cups[cc_ix]



starting_point = (full_cups.index(1)+1) % list_len
if starting_point + 1 < list_len:
    result = full_cups[starting_point]*full_cups[starting_point+1]
else:
    result = full_cups[-1]*full_cups[0]
                  
print(f'Result: {result}')
end = timeit()
print(f'Solution time: {end-start}')