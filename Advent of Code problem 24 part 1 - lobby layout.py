#   Advent of Code problem 24 part 1 - Lobby Layout - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

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
    
layout = [[0]*(50)]
for i in range(0,50):
    layout.append([0]*(50))
    
for inst in instructions:  #DOES NOT ACCOUNT FOR HEXAGONAL SHAPES
    x = y = 25
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
    layout[x][y] = (layout[x][y] + 1)%2
    
num_black = 0    
for row in layout:
    num_black += sum(row)

print(f'Black tiles: {num_black}')
end = timeit()
print(f'Solution time: {end-start}')