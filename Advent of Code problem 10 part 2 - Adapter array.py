#   Advent of Code problem 10 part 1 - Adapter Array  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

with open("Advent of Code problem 10 - adapter data.txt") as ad_file:
    file_contents = csv.reader(ad_file, delimiter='\n')
        
    num_series = []
    
    for line in file_contents:
        num_series.append(int(line[0]))

    num_series = sorted(num_series)
    path_count_array = [0]*(num_series[-1]+1)   # set up array to hold path counts for each possible number up to the list max
    
    path_count_array[0] = 1
            
    for i in range(1,len(path_count_array)):
        if i in num_series:
            path_count_array[i] = sum(path_count_array[max(0,i-3):i])
                
print(f'Number of paths: {path_count_array[-1]}')
end = timeit()
print(f'Solution time: {end-start}')