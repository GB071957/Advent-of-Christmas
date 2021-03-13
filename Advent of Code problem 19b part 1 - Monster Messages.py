#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

rules_regex = r'(\d+): (\d+)( \d+)?(?: \| )?(?: )?(\d+)? ?(\d+)?'
rules_list = []
messages = []
alpha_ref_rules = []
        
valid_strings= []

def not_all_strings(in_list):
    for i in range(0,len(in_list)):
        if isinstance(in_list[i],list):
            for item in in_list[i]:
                if isinstance(item,str) == False:
                    return True
            #x = in_list[i]
            #if all(isinstance(item,str) for item in x):
            #    continue
            #else:   # an item is not a string
            #    return True
        elif isinstance(in_list[i],str):
            continue
        else:   # there's an item that's not a string
            return True
    return False

def sub_values(in_list,ix):
    val = in_list[ix]
    num_elements_retd = 0
    if len(rules_list[val]) == 1:  #  there's only one element
        return in_list[0:ix] + rules_list[val][0:] + in_list[ix+1:], 1
    else:   # there are two elements
        if isinstance(rules_list[val][0],list):  # there are two lists
            ins0 = [] + rules_list[val][0]
            ins1 = [] + rules_list[val][1]
            return list((in_list[0:ix]+ins0+in_list[ix+1:], \
                    in_list[0:ix]+ins1+in_list[ix+1:])),3
        else:   # there a two non-lists
            return list((in_list[0:ix] + rules_list[val] + in_list[ix+1:])), 2
        
def find_vs():
    vs = []
    strings_to_process = []
    strings_to_process.append(rules_list[0])
    while strings_to_process != []:
        i = 0
        while i<len(strings_to_process[0]):
            if isinstance(strings_to_process[0][i],str):
                i += 1
                continue
            new_value, num_elems = sub_values(strings_to_process[0],i)
            if num_elems == 3:  #  need to create another string_to_process
                strings_to_process.append(new_value[1])
                strings_to_process[0] = new_value[0]
            else:   # there's only one list of values
                strings_to_process[0] = new_value
                
        vs_to_add = "".join(strings_to_process[0])
        vs.append(vs_to_add)
        del strings_to_process[0]
        if len(vs)%1000000 == 0:
            print(f'Valid strings: {len(vs)}, num strings to process: {len(strings_to_process)}')
                        
    return vs
                
def process_list(in_list):
    global valid_strings
    changed_value = in_list
    i = 0
    while i<len(in_list):
    
        if isinstance(in_list[i],str):
            i += 1
            continue
        elif isinstance(in_list[i],list):   # process this list
            new_value = process_list(in_list[i])
            if isinstance(new_value,str):
                valid_strings.append(new_value)
                del in_list[i]
            else:   #  found a valid string and we've evaluated in_list[i] completely
                if new_value == []:
                    del in_list[i]
                else:  #  we still have more evaluation of in_list[i] to do
                    in_list[i] = new_value
                    i += 1
        else:    #  the value is an integer
            new_value,num_elems = sub_values(in_list,i)
            in_list = new_value
            if num_elems == 3:  # new_value is 2 lists
                return in_list
            i += num_elems
    
    if in_list != [] and not not_all_strings(in_list):   #  in_list contains only strings.  combine them
        r = "".join(in_list)
        return r
    else:
        return in_list
            

with open("Advent of Code problem 19 - test2 Monster message data.txt") as mm_file:
    file_contents = csv.reader(mm_file, delimiter='\n')

    
    for line in file_contents:
        
        if line ==[]:
            continue
        elif '"' in line[0]:  # this is a rule that includes a reference to an alphabetic character
            ix = line[0].find(":")
            rules_list.append([int(line[0][0:ix]),line[0][ix+3]])
            #rules_list.append([int(line[0][0:1]),line[0][4]])
            alpha_ref_rules.append(int(line[0][0:ix]))
            #alpha_ref_rules.append(int(line[0][0:1]))
        elif line[0][0] not in ['a','b']:
            fields = re.search(rules_regex,line[0])
            if fields.group(5) != None:
                rules_list.append(list((int(fields.group(1)),[int(fields.group(2)),int(fields.group(3))],[int(fields.group(4)),int(fields.group(5))])))
            elif fields.group(4) != None and fields.group(3) == None:
                rules_list.append(list((int(fields.group(1)),[int(fields.group(2))],[int(fields.group(4))])))
            elif fields.group(4) != None:
                rules_list.append(list((int(fields.group(1)),[int(fields.group(2)),int(fields.group(3)),int(fields.group(4))])))
            elif fields.group(3) != None:
                rules_list.append(list((int(fields.group(1)),int(fields.group(2)),int(fields.group(3)))))
            else:
                rules_list.append(list((int(fields.group(1)),int(fields.group(2)))))
        else:   
            messages.append(line[0])
              
    rules_list = sorted(rules_list)
    for j in range(0,len(rules_list)):
        rules_list[j] = rules_list[j][1:]
        
    valid_strings = find_vs()
      
    num_valid_messages = 0
    for message in messages:
        if message in valid_strings:
            num_valid_messages += 1
            
print(f'Total number of valid messages: {num_valid_messages}')
end = timeit()
print(f'Solution time: {end-start}')