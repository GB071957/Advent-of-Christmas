#   Advent of Code problem 15 part 1 - Rambunctious Recitation - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv


starting_nums = [16,1,0,18,12,14,19]
nums_seen = []
turns_seen = []

game_nums = starting_nums[::-1]
turn = 7
while turn<20200:
    if game_nums[0] in game_nums[1:]:
        ix = game_nums[1:].index(game_nums[0])
        game_nums.insert(0,ix+1)
    else:
        game_nums.insert(0,0)
    turn+=1

print(f'Last value spoken: {game_nums[0]}')
end = timeit()
print(f'Solution time: {end-start}')