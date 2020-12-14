#   Advent of Code problem 14 part 1 - Shuttle search - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv
import bisect

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
            mvb = bin(mem_value)[2:].zfill(36)
            newmvb = ''
            for i in range(36):
                if mask[i] == 'X':
                    newmvb = newmvb + mvb[i]
                else:
                    newmvb = newmvb + mask[i]
            memval = int(newmvb,2)
            if mem_loc in memory_locs:
                ix = memory_locs.index(mem_loc)
                memory_values[ix] = memval
            else:
                bisect.insort(memory_locs,mem_loc)
                ix = memory_locs.index(mem_loc)
                memory_values = memory_values[:ix]+ [memval] + memory_values[ix:]
         

print(f'Sum of memory values: {sum(memory_values)}')
end = timeit()
print(f'Solution time: {end-start}')