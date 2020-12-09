#   Advent of Code problem 9 part 1  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

with open("Advent of Code problem 9 - port output.txt") as po_file:
    file_contents = csv.reader(po_file, delimiter='\n')

    num_series = []

    
    for line in file_contents:
        num_series.append(int(line[0]))
        
    n = 0
    not_found = True

    while not_found:
        not_found = False
        i = n+1
        while sum(num_series[n:i])< 144381670:
            i += 1
        if sum(num_series[n:i]) > 144381670:
            not_found = True
            n += 1

min_num = min(num_series[n:i])
max_num = max(num_series[n:i])
                
print(f'Encryption weakness = {min_num + max_num}')
end = timeit()
print(f'Solution time: {end-start}')