#   Advent of Code problem 20 part 1 - Jurassic Jigsaw - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

tile_num_regex = r'Tile (\d+):'

piece_data = []
with open("Advent of Code problem 20 -test2 Jurassic Jigsaw data.txt") as mm_file:
    file_contents = csv.reader(mm_file, delimiter='\n')

    dataline_num = 0
    datalines = []
    top_border_code = ''
    left_border_code = ''
    right_border_code = ''
    bottom_border_code = ''
    for line in file_contents:
        
        if line ==[]:
            dataline_num = 0
            top_border_code = ''
            left_border_code = ''
            right_border_code = ''
            bottom_border_code = ''
            continue
        elif "Tile" in line[0]:  # Title line
            field = re.search(tile_num_regex,line[0])
            tilenum = field.group(1)
        else:  #  this is a data line
            if dataline_num == 0:
                left_border_code += '0' if line[0][0] == "." else '1'
                right_border_code += '0' if line[0][-1] == "." else '1'
                for character in line[0]:
                    if character == ".":
                        top_border_code += '0'
                    else:
                        top_border_code += '1'
            else:
                left_border_code += '0' if line[0][0] == "." else '1'
                right_border_code += '0' if line[0][-1] == "." else '1'
                if dataline_num == 9:
                    for character in line[0]:
                        if character == ".":
                            bottom_border_code += '0'
                        else:
                            bottom_border_code += '1'
                    dl = [int(tilenum)]
                    dl.append(list((top_border_code,right_border_code, \
                              bottom_border_code,left_border_code)))
                    for i in range(0,4):
                        dl.append(dl[1][i][-1::-1])
                    dl1 = []
                    dl1.append(dl[0])
                    for i in range(0,4):
                        dl1.append(dl[1][i])
                    for i in range(2,6):
                        dl1.append(dl[i])
                    datalines.append(dl1)
            dataline_num += 1

    corner_pieces = []   #  NEED TO DISTINGUISH TO DETERMINE THAT ADJACENT CODES ARE FOUND
    for j in range(0,len(datalines)):
        entries_found = [0]*len(datalines[j])
        for k in range(0,j):
            for m in range(1,len(datalines[j])):
                if datalines[j][m] in datalines[k]:
                    entries_found[m] = 1
        for k in range(j+1,len(datalines)):
            for m in range(1,len(datalines[j])):
                if datalines[j][m] in datalines[k]:
                    entries_found[m] = 1
        #print(f'{datalines[j]}')
        #print(f'{entries_found}')
        if sum(entries_found)<=6 and datalines[j][0] not in corner_pieces:

            if entries_found[1]==0 and entries_found[4]==0:
                corner_pieces.append(datalines[j][0])
            else:
                for n in range(1,8):
                    if entries_found[n] == 0 and entries_found[n+1]==0:
                        corner_pieces.append(datalines[j][0])
                        break
                    if n<4 and entries_found[n]==0 and entries_found[n+5]==0:
                        corner_pieces.append(datalines[j][0])
                        break

prod_corner_piece_nums = 1
for corner_piece in corner_pieces:
    prod_corner_piece_nums *= corner_piece
           
print(f'Product of corner piece numbers: {prod_corner_piece_nums}')
end = timeit()
print(f'Solution time: {end-start}')