#   Advent of Code problem 5 part 1  Program by Greg Brinks

# Decode Seat Data


from timeit import default_timer as timeit
start= timeit()

import csv, re


def rownum(rowchars):
    rowchars = rowchars.replace('F','0')
    rowchars = rowchars.replace('B','1')
    return int(rowchars,2)

def colnum(colchars):
    colchars = colchars.replace('R','1')
    colchars = colchars.replace('L','0')
    return int(colchars,2)

maxseat = 0

with open("Advent of Code problem 5 - seat data.txt") as seat_file:
    file_contents = csv.reader(seat_file, delimiter='\n')

    for line in file_contents:
        row = rownum(line[0][0:7])
        col = colnum(line[0][8:11])
        seatid = 8*row+col
        maxseat = max(seatid,maxseat)
        

print(f'Maximum seat is {maxseat}')
end = timeit()
print(f'Solution time: {end-start}')


