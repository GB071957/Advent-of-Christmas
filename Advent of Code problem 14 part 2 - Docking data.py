#   Advent of Code problem 14 part 2 - Shuttle search - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv
import bisect

def get_mem_locs(location,mask):
    locations = []
    location = bin(location)[2:].zfill(36)
    num_xs = mask.count('X')
    for j in range(0,2**num_xs):   #  create 2**num_xs addresses
        newmask = mask
        newloc = ''
        bin_num = bin(j)[2:].zfill(num_xs)
        # for j in range(0,num_xs):
        #     newmask = newmask.replace('X',bin_num[j])
        ix = 0
        for i in range(36):
            if newmask[i] == '0':
                newloc = newloc + location[i]
            elif newmask[i] == '1':
                newloc = newloc + '1'
            else:   # newmask[i] must be 'X'
                newloc = newloc + bin_num[ix]
                ix += 1
        locations.append(int(newloc,2))       
    return locations

def update_value(loc,val,memlocs,memvals):
    if loc in memlocs:
        ix = memlocs.index(loc)
        memvals[ix] = val
    else:
        bisect.insort(memlocs,loc)
        ix = memlocs.index(loc)
        memvals = memvals[:ix]+ [val] + memvals[ix:]
    return memlocs, memvals
    

memory_locs = []
memory_values = []

with open("Advent of Code problem 14 - docking data.txt") as docking_file:
    file_contents = csv.reader(docking_file, delimiter='\n')

    for line in file_contents:
        if line[0][:4] == 'mask':
            mask = line[0][7:]
        else:
            mem_loc = line[0][4:9]  
            if mem_loc[4] == ' ':   #  3 digit number
                mem_loc = int(mem_loc[:3])
            elif mem_loc[4] == ']':   #  4-digit number
                mem_loc = int(mem_loc[:4])
            else:                      # 5-digit number
                mem_loc = int(mem_loc)    
                
            mem_value = int(line[0][line[0].find('= ')+2:])
            locations = get_mem_locs(mem_loc,mask)
            for location in locations:
                memory_locs, memory_values = update_value(location,mem_value, memory_locs,memory_values)
                

         

print(f'Sum of memory values: {sum(memory_values)}')
end = timeit()
print(f'Solution time: {end-start}')