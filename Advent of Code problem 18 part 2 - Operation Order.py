#   Advent of Code problem 18 part 2 - Operation Order - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

def eval_addition(in_string):   # replace 'x + y' with '(x + y)'
    regex = r'(\d+)\+(\d+)'
    while True:
        additions = re.findall(regex,in_string)
        if additions == []:
            break
        while additions != []:
            for j in range(0,len(additions)):
                in_string = in_string.replace(additions[j][0]+'+'+additions[j][1],str(int(additions[j][0])+int(additions[j][1])))
            additions = re.findall(regex,in_string)
    return in_string
    

def eval_simple_string(in_string):    #  assumes string is made up of digits, + and *
    regex = r'(\d+\d)'
    if '+' in in_string:
        in_string = eval_addition(in_string)
    answer = int(in_string[0])
    i = 1
    while i < len(in_string):
        if in_string[i] == '+':
            i += 1
            numstr = ''
            while i<len(in_string) and in_string[i] in ['0','1','2','3','4','5','6','7','8','9']:
                numstr += in_string[i]
                i += 1
            answer += int(numstr)
        elif in_string[i] == '*':
            i += 1
            numstr = ''
            while i<len(in_string) and in_string[i] in ['0','1','2','3','4','5','6','7','8','9']:
                numstr += in_string[i]
                i += 1
            answer *= int(numstr)
        else:
            answer = int(str(answer) + in_string[i])
            i += 1
    return answer

def paren_string(numstr):  #assume first character is "(".  Return stuff between it and it's mate
    i = 1
    answer = ''
    while i<len(numstr) and numstr[i] != ")":   #<=???
        if numstr[i] == "(":
            p_string,j = paren_string(numstr[i:])
            i += j
            answer += p_string
        else:
            answer += numstr[i]
            i += 1    #  should this be unindented to apply to both cases?
    if i<len(numstr) and numstr[i]==")":
        i+=1
    answer = eval_exp(answer)
    return str(answer),min(i,len(numstr))
 
    
def eval_exp(in_string):
    answer = 0
    stored_string = ''
    i = 0
    while i<len(in_string):
        if in_string[i] == '(':        
            p_string,j = paren_string(in_string[i:])
            i += j
            stored_string += str(eval_exp(p_string))
            #i += len(p_string)+2   #???
        elif in_string[i] == ')':
            stored_string = str(eval_simple_string(stored_string))   #evaluate expression in stored_string
            i += 1
        else:    #  store additional characters
            while i<len(in_string) and in_string[i] not in ['(', ')']:  # store digit and operator
                if in_string[i] == ' ':
                    i += 1
                else:
                    stored_string += in_string[i]
                    i += 1
    return eval_simple_string(stored_string)
                

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