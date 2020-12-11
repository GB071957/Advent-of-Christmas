#   Advent of Code problem 11 part 1 - Seating System  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, copy

def seat_count(seatmap,row,col):
    num = 0
    for i in range(max(0,row-1),min(len(seatmap),row+2)):
        num += seatmap[i][max(0,col-1):min(len(seatmap[i]),col+2)].count('#')
    return num - seatmap[row][col].count('#')

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
                filled_seats += seat_count(seat_data,i,j)
                if seat_data[i][j] == '#' and filled_seats>=4: 
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