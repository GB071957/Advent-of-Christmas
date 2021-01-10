#   Advent of Code problem 18 part 2 - Operation Order - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

operators = ['*','+','(',')']
numerals = ['1','2','3','4','5','6','7','8','9']
    
def eval_exp(in_string):
    
    def clear_parens(ops,nums):
        oper = oplist.pop()
        while oper!='(':
            y = nums.pop()
            z = nums.pop()
            if oper == '*':
                nums.append(y*z)
            else:  #  oper is +
                nums.append(y+z)
            oper = ops.pop()
        if ops!= [] and ops[-1] == '+':
            y = nums.pop()
            z = nums.pop()
            nums.append(y+z)
            oper = ops.pop()
        return ops,nums
        
        
    answer = 0
    oplist = []
    operands = []
    
    if in_string[0] in operators:
        oplist.append(in_string[0])
    else:
        operands.append(int(in_string[0]))
    i=1
    
    while i<len(in_string):
        x = in_string[i]
        if x == ' ':
            i += 1
            continue
        if x == '(':
            oplist.append(x)
        elif x==')':
            (oplist,operands) = clear_parens(oplist,operands)
        elif x == '*':
            if oplist!=[] and oplist[-1]==x:
                y = operands.pop()
                z = operands.pop()
                operands.append(y*z)   #  leave the last operator as *
            else:
                oplist.append(x)
        elif x in numerals:
            if oplist!=[] and oplist[-1]=='+':
                y = operands.pop()
                operands.append(int(x)+y)
                oplist.pop()
            else:
                operands.append(int(x))
        else:   #  x is +
            oplist.append(x)
        i += 1
        
    if oplist!=[]:   #  there is still one or more operation to be performed
        while oplist!=[]:
            oper = oplist.pop()
            y = operands.pop()
            z = operands.pop()
            if oper == '*':
                operands.append(y*z)
            else:
                operands.append(y+z)
        
    return operands[0]
                

with open("Advent of Code problem 18 - Operation Order data.txt") as oo_file:
    file_contents = csv.reader(oo_file, delimiter='\n')
    
    tot_answers = 0
    i = 0
    
    for line in file_contents:
        
        tot_answers += eval_exp(line[0])
        i+=1
   
print(f'Total of answers: {tot_answers}')
end = timeit()
print(f'Solution time: {end-start}')