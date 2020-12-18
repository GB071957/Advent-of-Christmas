#   Advent of Code problem 17 part 2 - Conway cubes - Program by Greg Brinks

#  Consider in the input puzzle data that the point in the 5th row at the fifth position to reside at
#   (x,y,z) = (0,0,0).  Given that there will be six cycles.  The eventual size of the matrix will be 20x20x13.  For
#   ease of dealing with things, we'll think of it as being 21x21x13 with x and y ranging from -10 to 10 and z
#   ranging from -6 to 6.  We'll consider row 5 and column 5 of the input data to lie on the x-y axis at z=0.


from timeit import default_timer as timeit
start= timeit()

import csv, copy
    
def neighbors_active(x,y,z,w,mat):
    active = 0
    if mat[x][y][z][w] == '#':
        active -= 1
    for i in range(max(x-1,0),min(x+2,21)):
        for j in range(max(y-1,0),min(y+2,21)):
            for k in range(max(z-1,0),min(z+2,13)):
                for l in range(max(w-1,0),min(w+2,13)):
                #if i>len(mat):
                #    print(f'{i} is longer than len(mat)')
                #if j>len(mat[i]):
                #    print(f'i = {i}, {j} is longer than len(mat[i])')
                #if k>len(mat[i][j]):
                #    print(f'i = {i}, {j}, {k} is longer than len(mat[i][j])')
                    if mat[i][j][k][l] == '#':
                        active +=1
    return active
                

xyzwmatrix = []

n = 0
for x in range(-10,11):
    yzwmatrix = []
    for y in range(-10,11):
        zwmatrix = []
        for z in range(-6,7,1):
            zmatrix = []
            for w in range(-6,7,1):
                zmatrix.append('.')
            
            zwmatrix.append(zmatrix)
        yzwmatrix.append(zwmatrix)
    xyzwmatrix.append(yzwmatrix)

xylow = 6
xyhigh = 14
zwlow = 6
zwhigh = 6


with open("Advent of Code problem 17 - satellite data.txt") as satellite_file:
    file_contents = csv.reader(satellite_file, delimiter='\n')
    
    x = xylow
    y = xyhigh
    z = w = zwlow
    for line in file_contents:
        
        for i in range(0,len(line[0])):
            xyzwmatrix[x+i][y][z][w] = line[0][i]
        y -= 1
    
#    print(f'At beginning:')
#    for z in range(zwlow,zwhigh+1):
#        for w in range(zwlow,zwhigh+1):
#            print(f'z={z}, w={w}, xylow={xylow}, xyhigh={xyhigh}')
#            for y in range(xyhigh,xylow-1,-1):
#                for x in range(xylow,xyhigh+1):
#                    print(xyzwmatrix[x][y][z][w], end=" ")
#                print('')

for circuits in range(0,6):   # change 3 to 6
    xyzwcopy = copy.deepcopy(xyzwmatrix)
    xylow -= 1
    xyhigh += 1
    zwlow -= 1
    zwhigh += 1
    for x in range(xylow,xyhigh+1):
        for y in range(xylow,xyhigh+1):
            for z in range(zwlow,zwhigh+1):
                for w in range(zwlow,zwhigh+1):
                    #print(f'{x}, {y}, {z}')
                    n_active = neighbors_active(x,y,z,w,xyzwmatrix)
                    if xyzwmatrix[x][y][z][w] == '#':
                        if (2<=n_active<=3):
                            continue
                        else:
                            #print(f'Changed {x}, {y}, {z} to inactive')
                            xyzwcopy[x][y][z][w] = '.'
                    else:
                        if n_active == 3:
                            #print(f'Changed {x}, {y}, {z} to active')
                            xyzwcopy[x][y][z][w] = '#'

#    for z in range(zwlow,zwhigh+1):
#        for w in range(zwlow,zwhigh+1):
#            print(f'z={z}, w={w}, xylow={xylow}, xyhigh={xyhigh}')
#            for y in range(xyhigh,xylow-1,-1):
#                for x in range(xylow,xyhigh+1):
#                    print(xyzwcopy[x][y][z][w], end=" ")
#                print('')

    xyzwmatrix = copy.deepcopy(xyzwcopy)

total_active = 0
for x in range(xylow,xyhigh+1):
    for y in range(xylow,xyhigh+1):
        for z in range(zwlow,zwhigh+1):
            for w in range(zwlow,zwhigh+1):
                if xyzwmatrix[x][y][z][w] == '#':
                    total_active += 1
   
print(f'Total active: {total_active}')
end = timeit()
print(f'Solution time: {end-start}')