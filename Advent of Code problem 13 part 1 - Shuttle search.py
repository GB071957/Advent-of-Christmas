#   Advent of Code problem 13 part 1 - Shuttle search - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

with open("Advent of Code problem 13 - shuttle data.txt") as shuttle_file:
    file_contents = csv.reader(shuttle_file, delimiter='\n')

    sched_data = []
    for line in file_contents:
        sched_data.append(line[0])
        
    departure = int(sched_data[0])
    buses = sched_data[1].split(',')
    
first_depart = 10**15
bus_to_take = 0
for bus in buses:
    if bus == 'x':
        continue
    bus = int(bus)
    next_depart = departure + bus-departure%bus
    if next_depart < first_depart:
        first_depart = next_depart
        bus_to_take = bus

print(f'First departure time: {first_depart}, answer: {(first_depart-departure)*bus_to_take}')
end = timeit()
print(f'Solution time: {end-start}')