#   Advent of Code problem 11 part 2 - Seating System  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, copy

def seat_count(seatmap,row,col):
    num = 0
    i,j = row,col
    for dir in [(-1,-1),(-1,0),(-1,1,),(0,1),(1,1,),(1,0),(1,-1),(0,-1)]:
        i += dir[0]
        j += dir[1]
        while 0<=i<len(seatmap) and 0<=j<len(seatmap[row]):
            if seatmap[i][j] == '#':
                num += 1
                break
            elif seatmap[i][j] == 'L':
                break
            i += dir[0]
            j += dir[1]
        i, j = row, col
    return num 

with open("Advent of Code problem 11 - seat data.txt") as seat_file:
    file_contents = csv.reader(seat_file, delimiter='\n')
    
    seat_data = []
    
    for line in file_contents:
        seat_data.append(list(line[0]))
    
    new_seat_data = []
    while new_seat_data != seat_data:
        if new_seat_data == []:    # this is the first time through the code
            new_seat_data = copy.deepcopy(seat_data)
        else:
            seat_data = copy.deepcopy(new_seat_data)
        for i in range(0,len(seat_data)):
            filled_seats = 0
            for j in range(0,len(seat_data[i])):
                if seat_data[i][j] == '.':
                    continue
                filled_seats += seat_count(seat_data,i,j)
                if seat_data[i][j] == '#' and filled_seats>=5: 
                    new_seat_data[i][j] = 'L'
                elif seat_data[i][j] == 'L' and filled_seats == 0:
                    new_seat_data[i][j] = '#'
                filled_seats = 0
        

total_filled = 0
for row in new_seat_data:
    total_filled += row.count('#')

print(f'Number of seats filled: {total_filled}')
end = timeit()
print(f'Solution time: {end-start}')