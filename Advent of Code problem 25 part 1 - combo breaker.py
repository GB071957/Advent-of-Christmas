#   Advent of Code problem 25 part 1 - Combo breaker - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import copy

subject = 7
card_loop_size = 0
door_loop_size = 0
mod_num = 20201227
card_public_key = 7573546
door_public_key = 17786549

computed_card_key = 1
computed_door_key = 1

def transform(value,subject,modnum):
    return (value*subject)%modnum

def loop_size(val,key,subject,modnum):
    loopsize = 1
    while val!= key:
        val=transform(val,subject,modnum)
        loopsize += 1
    return loopsize-1


card_loop_size = loop_size(1,card_public_key,subject,mod_num)
print(f'Secret card loop size is {card_loop_size}')

door_loop_size = loop_size(1,door_public_key,subject,mod_num)
print(f'Secret door loop size is {door_loop_size}')

encryption_key = 1
for i in range(1,door_loop_size+1):
    encryption_key = transform(encryption_key,card_public_key,mod_num)
    #print(f'encryption key: {encryption_key}')
    
print(f'encryption key: {encryption_key}')

end = timeit()
print(f'Solution time: {end-start}')