#   Advent of Code problem 8 part 1  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv

with open("Advent of Code problem 8 - Boot Code.txt") as bc_file:
    file_contents = csv.reader(bc_file, delimiter='\n')

    code_lines = []
    total_acc = 0
    
    for line in file_contents:
        code_lines.append(line[0])
    n = 0
    while code_lines[n] != 'stop':
        if code_lines[n][0:3] == 'acc':
            total_acc += int(code_lines[n][4:len(code_lines[n])])
            code_lines[n] = 'stop'
            n += 1
        elif code_lines[n][0:3] =='jmp':
            code_lines[n],n = 'stop',n+int(code_lines[n][4:len(code_lines[n])])
        else:
            code_lines[n] = 'stop'
            n += 1

print(f'Accumulator at {total_acc}')
end = timeit()
print(f'Solution time: {end-start}')