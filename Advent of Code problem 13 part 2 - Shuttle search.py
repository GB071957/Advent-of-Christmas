#   Advent of Code problem 13 part 2 - Shuttle search - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv
import math

def max_bus(bus_data):
    max_bus = 0
    for j in range(1,len(bus_data)):
        if bus_data[j][0]>bus_data[max_bus][0]:
            max_bus = j
    return max_bus

def poss_first_time(depart,add_bus,spacing,increment):
    found_first_time = False
    while not found_first_time:
        if (depart + spacing) % add_bus == 0:
            found_first_time = True
        else:
            depart += increment
    return depart

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

with open("Advent of Code problem 13 - shuttle data.txt") as shuttle_file:
    file_contents = csv.reader(shuttle_file, delimiter='\n')

    sched_data = []
    for line in file_contents:
        sched_data.append(line[0])
    
    #depart = int(sched_data[0])
    buses = sched_data[1].split(',')

found_first_time = False
first_bus = int(buses[0])
depart = 100000000000000
#depart = 0

#  get list of buses and spread of departure times:
rel_departs = []
for i in range(1,len(buses)):
    if buses[i] == 'x':
        continue
    rel_departs.append((int(buses[i]),i))

depart = depart + first_bus - depart%first_bus
incr=first_bus

while rel_departs != []:     # go through list of buses from longest route to shortest
                             # add the next longest route bus to solution
    next_bus_ix = max_bus(rel_departs)   # find the next longest route bus
    next_bus,gap = rel_departs[next_bus_ix][0], rel_departs[next_bus_ix][1]
    depart = poss_first_time(depart,next_bus,gap,incr)   # find departure time with this new bus
    incr = lcm(next_bus,incr)   # determine increment for testing new poss departure times
    del rel_departs[next_bus_ix]   #  delete the found bus from the list of buses to add 

print(f'First departure time: {depart}')
end = timeit()
print(f'Solution time: {end-start}')