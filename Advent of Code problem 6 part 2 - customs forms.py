#   Advent of Code problem 6 part 1  Program by Greg Brinks

# Decode Seat Data


from timeit import default_timer as timeit
start= timeit()

import csv

total_yes_answers = 0
firstline = True

with open("Advent of Code problem 6 - customs data.txt") as customs_file:
    file_contents = csv.reader(customs_file, delimiter='\n')

    customsfields = set()
    for line in file_contents:
        if line == []:
            total_yes_answers += len(customsfields)
            customsfields = set()
            firstline = True
            continue
        if customsfields == set() and firstline:
            customsfields = set(line[0])
            firstline = False
        else:
            customsfields = customsfields.intersection(set(line[0]))
        
total_yes_answers += len(customsfields)

print(f'Total ""yes"" answers: {total_yes_answers}')
end = timeit()
print(f'Solution time: {end-start}')


