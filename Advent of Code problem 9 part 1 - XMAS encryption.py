#   Advent of Code problem 9 part 1  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

with open("Advent of Code problem 9 - port output.txt") as po_file:
    file_contents = csv.reader(po_file, delimiter='\n')

    num_series = []

    
    for line in file_contents:
        num_series.append(int(line[0]))
        
    n = 25
    all_valid = True
    while all_valid:
        all_valid = False
        next_num = num_series[n]
        for i in range(n-25,n):
            if next_num - num_series[i] in num_series[i:n]:
                n += 1
                all_valid = True
                break
            
                
print(f'First invalid output a position {n}: {next_num}')
end = timeit()
print(f'Solution time: {end-start}')