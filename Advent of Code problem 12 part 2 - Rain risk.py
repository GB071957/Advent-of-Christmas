#   Advent of Code problem 12 part 2 - Rain risk  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv
direction = 'E'
waypoint = [10,1]      # location relative to ship
xpos = 0
ypos = 0

def move(compass, amount, wp):
    if compass == 'N':
        wp[1] += amount
    elif compass == 'S':
        wp[1] -= amount
    elif compass == 'E':
        wp[0] += amount
    elif compass == 'W':
        wp[0] -= amount
    return wp

def change_dir(change,amount, wp):

    if amount == 180:
        wp = [-wp[0],-wp[1]]
    elif (amount == 90 and change == 'L') or (amount == 270 and change == 'R'):
        wp = [-wp[1],wp[0]]
    elif (amount == 90 and change == 'R') or (amount == 270 and change == 'L'):
        wp = [wp[1],-wp[0]]
    return wp

def advance(amount,wp,x,y):
    
    return x+wp[0]*amount,y+wp[1]*amount
    

with open("Advent of Code problem 12 - navigation data.txt") as navigation_file:
    file_contents = csv.reader(navigation_file, delimiter='\n')

    for line in file_contents:
        
        action = line[0][0]
        val = int(line[0][1:])
        if action == 'N' or action == 'S' or action == 'E' or action == 'W':
            waypoint = move(action,val,waypoint)
        elif action == 'L' or action == 'R':
            waypoint = change_dir(action,val,waypoint)
        elif action == 'F':
            xpos,ypos = advance(val,waypoint,xpos,ypos)

print(f'Manhattan distance from starting point: {abs(xpos)+abs(ypos)}')
end = timeit()
print(f'Solution time: {end-start}')