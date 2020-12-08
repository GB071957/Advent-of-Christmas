#   Advent of Code problem 8 part 1  Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, copy

with open("Advent of Code problem 8 - Boot Code.txt") as bc_file:
    file_contents = csv.reader(bc_file, delimiter='\n')

    code_lines = []
    total_acc = 0
    
    for line in file_contents:
        code_lines.append(line[0])
    
    changed_instruction = 0
    while True:
        working_copy_code = copy.deepcopy(code_lines)
        
        n = 0
        
        #  FIND THE NEXT INSTRUCTION THAT'S A CANDIDATE FOR FIXING THE PROGRAM
        while working_copy_code[changed_instruction][0:3] != 'jmp' and working_copy_code[changed_instruction][0:3] != 'nop':
            changed_instruction += 1
        if working_copy_code[changed_instruction][0] == 'j':
            working_copy_code[changed_instruction] = working_copy_code[changed_instruction].replace('jmp','nop')
        else:
            working_copy_code[changed_instruction] = working_copy_code[changed_instruction].replace('nop','jmp')
        
        #TRY IT OUT
        total_acc = 0
        while n<len(working_copy_code) and working_copy_code[n] != 'stop':
            if working_copy_code[n][0:3] == 'acc':
                total_acc += int(working_copy_code[n][4:len(working_copy_code[n])])
                working_copy_code[n] = 'stop'
                n += 1
            elif working_copy_code[n][0:3] =='jmp':
                working_copy_code[n],n = 'stop',n+int(working_copy_code[n][4:len(working_copy_code[n])])
            else:
                working_copy_code[n] = 'stop'
                n += 1
        if n>=len(working_copy_code):   # we've reached the end of the code without a loop
            break
        changed_instruction += 1

print(f'Accumulator at {total_acc}')
end = timeit()
print(f'Solution time: {end-start}')