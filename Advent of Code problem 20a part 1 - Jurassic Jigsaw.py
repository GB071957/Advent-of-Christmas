#   Advent of Code problem 20a part 1 - Jurassic Jigsaw - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

tile_num_regex = r'Tile (\d+):'

def parse_input(jj_array):
    
    def edge_data(tile):
        edges = [tile[0]]
        left = []
        right = []
        for i in range(0,len(tile)):
            left.append(tile[i][0])
            right.append(tile[i][-1])
        edges.append("".join(right))
        edges.append(tile[-1])
        edges.append("".join(left))
        for i in range(0,4):
            edges.append(edges[i][-1::-1])
        return edges
 
    tiles = {}
    edges = {}
    
    tile_data = []
    for line in map(str.rstrip, jj_array):
        if not line:
            tiles[tile_id]=tile_data
            edges[tile_id] = edge_data(tile_data)
            tile_data = []
        elif ":" in line:
            label, tile_id = line.split(' ')
            tile_id = int(tile_id[0:4])
        else:
            tile_data.append(line)
    tiles[tile_id]=tile_data
    edges[tile_id] = edge_data(tile_data)
    tile_data = []

    return tiles, edges

def find_corners(edge_data):
    corners = []
    for tile in edge_data:
        edges_found = [0,0,0,0,0,0,0,0]
        for i in range(len(edge_data[tile])):
            for oth_tile in edge_data:
                if oth_tile == tile:
                    continue
                elif edge_data[tile][i] in edge_data[oth_tile]:
                    edges_found[i] = 1
                    break

        if sum(edges_found)<=6 and tile not in corners:
            if edges_found[0]==0 and edges_found[3]==0:
                corners.append(tile)
            else:
                for n in range(0,7):
                    if edges_found[n] == 0 and edges_found[n+1]==0:
                        corners.append(tile)
                        print(f'tile {tile}: {edge_data[tile]}')
                        print(f'{edges_found}')
                        if len(corners)==4:
                            return corners
                        break
                    if n<3 and edges_found[n]==0 and edges_found[n+5]==0:
                        corners.append(tile)
                        print(f'tile {tile}: {edge_data[tile]}')
                        print(f'{edges_found}')
                        if len(corners)==4:
                            return corners
                        break                  
    
    return corners      

piece_data = []
with open("Advent of Code problem 20 -test2 Jurassic Jigsaw data.txt") as jj_file:
    camera_array = jj_file.readlines()
    
tiles, edges = parse_input(camera_array)

corners = find_corners(edges)

prod_corner_piece_nums = 1
for corner_piece in corners:
    prod_corner_piece_nums *= corner_piece
           
print(f'Product of corner piece numbers: {prod_corner_piece_nums}')
end = timeit()
print(f'Solution time: {end-start}')