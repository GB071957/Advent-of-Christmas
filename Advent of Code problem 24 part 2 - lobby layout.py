#   Advent of Code problem 24 part 2 - Lobby Layout - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, copy

def flip(tiles):
    new_layout = copy.deepcopy(tiles)
    for row in range(0,len(tiles)):    
        for tile in range(0,len(tiles[row])):
            black_count = 0
            tiles_to_check = []
            for x in range(tile-1,tile+2):
                if x<0 or x>=len(tiles[row]):
                    continue
                for y in range(row-1,row+2):
                    if y<0 or y>=len(tiles) or (x<tile and y<row) or (x==tile and y==row) \
                                            or (x>tile and y>row):
                        continue
                    black_count += tiles[y][x]
            if tiles[row][tile] == 1 and (black_count==0 or black_count>2):
                new_layout[row][tile] = 0
            elif tiles[row][tile] == 0 and black_count==2:
                new_layout[row][tile] = 1
    return new_layout

def count_black(tiles):
    num_black = 0    
    for row in tiles:
        num_black += sum(row)
    return num_black            

def expanded(tiles):  # add a row and column of 0s around the existing layout of tiles
    new_tiles = []
    tile_row = [0]*(len(tiles[0])+2)
    new_tiles.append(tile_row)
    for row in tiles:
        tile_row = [0]+row+[0]
        new_tiles.append(tile_row)
    tile_row = [0]*(len(tiles[0])+2)
    new_tiles.append(tile_row)
    return new_tiles

with open("Advent of Code problem 24 - Lobby Layout data.txt") as ll_file:
    file_contents = csv.reader(ll_file, delimiter='\n')

    i = 0
    instructions = []
    max_moves = 0
    for line in file_contents:
        
        codes = line[0]
        i = 0
        inst_list = []
        while i < len(codes):
            if codes[i]=="e" or codes[i]=="w":
                inst_list.append(codes[i])
                i += 1
            else:
                inst_list.append(codes[i:i+2])
                i += 2
        max_moves = max(max_moves,len(inst_list))
        instructions.append(inst_list)
        
#for inst in instructions:
#   print(inst)
    
layout = [[0]*(45)]
for i in range(0,44):
    layout.append([0]*(45))
    
for inst in instructions:  #DOES NOT ACCOUNT FOR HEXAGONAL SHAPES
    x = y = 21
    #x += (inst.count("e") + inst.count("se") + inst.count("ne") - inst.count("w") - inst.count("nw") - inst.count("sw"))
    #y += (inst.count("ne") + inst.count("nw") - inst.count("se") - inst.count("sw"))
    for move in inst:
        if move=="e" or move=="se":
            x += 1
        elif move=="w" or move=="nw":
            x -=1    

        if "n" in move:
            y += 1
        elif "s" in move:
            y -= 1
    #print(f'({x},{y}) before changing: {layout[x][y]}')
    layout[y][x] = (layout[y][x] + 1)%2

#  find size of non-zero portion of layout
minrow = mincol = 1000
maxrow = maxcol = 0
for row in range(0,len(layout)):
    if sum(layout[row]) > 0:
        minrow = min(minrow,row)
        maxrow = max(maxrow,row)
    else:
        continue
    for col in range(0,len(layout[row])):
        if layout[row][col]==1:
            mincol = min(mincol,col)
            maxcol = max(maxcol,col)
small_layout = []            
for row in (range(min(minrow,mincol),max(maxrow,maxcol)+1)):
    small_layout.append(copy.deepcopy(layout[row][min(minrow,mincol):max(maxrow,maxcol)+1]))
layout = expanded(copy.deepcopy(small_layout))

print(f'Initial number of black tiles: {count_black(layout)}')


#print(f'Initial count: {count_black(layout)}')
#for i in range(26,15,-1):    
#    print(f'{i}: {layout[i][15:26]}')
   
for days in range(1,101):
    layout = flip(layout)
#    for i in range(26,15,-1):    
#        print(f'{i}: {layout[i][15:26]}')
    num_black = count_black(layout)
    if days>=10 and days%10==0:
        print(f'After day {days}, there are {num_black} black tiles')
    layout = expanded(layout)
    
    

#print(f'Black tiles: {num_black}')
end = timeit()
print(f'Solution time: {end-start}')