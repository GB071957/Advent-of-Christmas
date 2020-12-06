#   Advent of Code problem 2 Part 2  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

num_captured = 0

pws = []
valid = 0
pwcount = 0

with open("Advent of Code problem 2.txt") as pw_file:
    file_contents = csv.reader(pw_file, delimiter='\n')

    for line in file_contents:
        pwcount += 1
        pwstring = line[0]
        minnum = int(pwstring[0:pwstring.find('-')])
        maxnum = int(pwstring[pwstring.find('-')+1:pwstring.find(' ')])
        pw = pwstring[pwstring.find(':')+2:]
        letter = pwstring[pwstring.find(':')-1]
        if (pw[minnum-1]==letter or pw[maxnum-1]==letter) and not (pw[minnum-1]==letter and pw[maxnum-1]==letter):
            valid += 1

print(f'There are {valid} valid passwords out of {pwcount} passwords')
end = timeit()
print(f'Solution time: {end-start}')


