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
    
    diff_by_one = 0
    diff_by_three = 1   #  the diff between last adapter and my device is 3
    if num_series[0] == 1:
        diff_by_one += 1
    elif num_series[0] == 3:
        diff_by_three += 1
        
    for i in range(1,len(num_series)):
        if num_series[i]-num_series[i-1] == 1:
            diff_by_one += 1
        elif num_series[i]-num_series[i-1] == 3:
            diff_by_three += 1
                
print(f'Number of differences by 1: {diff_by_one}, by 3: {diff_by_three}, product: {diff_by_one*diff_by_three}')
end = timeit()
print(f'Solution time: {end-start}')