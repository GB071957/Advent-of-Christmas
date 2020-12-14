#   Advent of Code problem 12 part 1 - Seating System  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv
direction = 'E'
xpos = 0
ypos = 0

def move(compass, amount, x, y):
    if compass == 'N':
        y += amount
    elif compass == 'S':
        y -= amount
    elif compass == 'E':
        x += amount
    elif compass == 'W':
        x -= amount
    return x,y

def change_dir(change,amount, dr):
    dirs = ['N','E','S','W']
    if change == 'L':
        amount = -amount
    return dirs[(dirs.index(dr)+(amount//90))%4]

def advance(amount,dr,x,y):
    if dr == 'N':
        y += amount
    elif dr == 'S':
        y -= amount
    elif dr == 'E':
        x += amount
    elif dr == 'W':
        x -= amount
    return x,y
    

with open("Advent of Code problem 12 - navigation data.txt") as navigation_file:
    file_contents = csv.reader(navigation_file, delimiter='\n')

    for line in file_contents:
        
        action = line[0][0]
        val = int(line[0][1:])
        if action == 'N' or action == 'S' or action == 'E' or action == 'W':
            xpos,ypos = move(action,val,xpos,ypos)
        elif action == 'L' or action == 'R':
            direction = change_dir(action,val,direction)
        elif action == 'F':
            xpos,ypos = advance(val,direction,xpos,ypos)

print(f'Manhattan distance from starting point: {abs(xpos)+abs(ypos)}')
end = timeit()
print(f'Solution time: {end-start}')