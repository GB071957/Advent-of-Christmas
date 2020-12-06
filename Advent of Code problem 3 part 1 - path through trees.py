#   Advent of Code problem 1  Program by Greg Brinks

# Find two numbers in the list of 200 that add to 2020 and multiply them together

from timeit import default_timer as timeit
start= timeit()

import csv

num_captured = 0

pws = []
valid = 0
pwcount = 0
line_length = 31
over = 3
down = 1
trees_hit = 0

with open("Advent of Code problem 3.txt") as tree_file:
    file_contents = csv.reader(tree_file, delimiter='\n')
    
    row = 0
    pos = 1
    for line in file_contents:
        row += 1
        if row == down:
            continue

        pos = (pos+over) % line_length
        if line[0][pos-1] == '#':
            trees_hit += 1
        

print(f'Hit {trees_hit} trees')
end = timeit()
print(f'Solution time: {end-start}')


