#   Advent of Code problem 3 Part 2  Program by Greg Brinks


from timeit import default_timer as timeit
start= timeit()

import csv
import numpy as np

over = [1,3,5,7,1]
down = [1,1,1,1,2]
line_length = 31

trees_hit = [0,0,0,0,0]

with open("Advent of Code problem 3.txt") as tree_file:
    file_contents = list(csv.reader(tree_file, delimiter='\n'))
    
    for i in range(len(over)):
        
        row = 0
        pos = 1
        for line in file_contents:
            row += 1
            if row == 1 or (row+1)%down[i]!=0:
                continue

            pos = (pos+over[i]) % line_length
            if line[0][pos-1] == '#':
                trees_hit[i] += 1
        

print(f'Product of number of trees hit in each path is {np.prod(trees_hit)}')
end = timeit()
print(f'Solution time: {end-start}')


