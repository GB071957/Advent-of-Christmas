#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

rules_regex = r'(\d+): (\d+) ?(\d+)?(?: \| )?(\d+)? ?(\d+)?'
rules_list = []
messages = []
alpha_ref_rules = []

def find_rules_with_all_strings(rules,as_rules):
    all_string_rules = set()
    for i in range(0,len(rules)):
        if i in as_rules:
            continue
        if all(isinstance(item,list) for item in rules[i]):
            all_alpha = True
            for subrule in rules[i]:
                all_alpha = all_alpha & all(isinstance(item,str) for item in subrule)
            if all_alpha:
                all_string_rules.add(i)
        elif all(isinstance(item,str) for item in rules[i]):
            all_string_rules.add(i)
    return all_string_rules-set(as_rules)

def replace_refs_to_rules_with_strings(rules,string_ref_rules):
    for i in range(0,len(rules)):
        for str_ref_rule in string_ref_rules:
            if all(isinstance(item,list) for item in rules[i]):
                for j in range(0,len(rules[i])):
                    for k in range(0,len(rules[i][j])):
                        if str_ref_rule == rules[i][j][k]:
                            #rules[i][j][k] = rules[str_ref_rule][0]
                            rules[i][j][k] = rules[str_ref_rule]
            else:  # rule consists of pair of entries
                for j in range(0,len(rules[i])):
                    if rules[i][j] == str_ref_rule:
                        rules[i][j] = rules[str_ref_rule][0] 
    return rules
        
   

with open("Advent of Code problem 19 - Monster message data.txt") as mm_file:
    file_contents = csv.reader(mm_file, delimiter='\n')

    
    for line in file_contents:
        
        if line ==[]:
            continue
        elif '"' in line[0]:  # this is a rule that includes a reference to an alphabetic character
            rules_list.append([int(line[0][0:2]),line[0][5]])
            alpha_ref_rules.append(int(line[0][0:2]))
        elif line[0][0] not in ['a','b']:
            fields = re.search(rules_regex,line[0])
            if fields.group(5) != None:
                rules_list.append(list((int(fields.group(1)),[int(fields.group(2)),int(fields.group(3))],[int(fields.group(4)),int(fields.group(5))])))
            #elif fields.group(4) != None:
            #    rules_list.append(list((int(fields.group(1)),int(fields.group(2)),int(fields.group(3)),int(fields.group(4)))))
            elif fields.group(3) != None:
                rules_list.append(list((int(fields.group(1)),int(fields.group(2)),int(fields.group(3)))))
            else:
                rules_list.append(list((int(fields.group(1)),int(fields.group(2)))))
        else:   
            messages.append(line[0])
              
    rules_list = sorted(rules_list)
    for j in range(0,len(rules_list)):
        rules_list[j] = rules_list[j][1:]
    
    #new_string_ref_rules = set()
    #for alpha_ref_rule in alpha_ref_rules:
    #    for rule in rules_list:
    #        if alpha_ref_rule in rule:
    #            rule[rule.index(alpha_ref_rule)] = rules_list[alpha_ref_rule][0]
        
    new_string_ref_rules = set(alpha_ref_rules)
    all_alpha_ref_rules = set()
    
    #while not all(isinstance(item,str) for item in rules_list[0]):
    while new_string_ref_rules != set():
        all_alpha_ref_rules = all_alpha_ref_rules | new_string_ref_rules
        rules_list = replace_refs_to_rules_with_strings(rules_list,new_string_ref_rules)
        new_string_ref_rules = find_rules_with_all_strings(rules_list,all_alpha_ref_rules)
        #print(f'k={k}, new_string_ref_rules = {new_string_ref_rules}')
        #for rule in new_string_ref_rules:
        #    print(f'{rules_list[rule]}')
        
    print(f'All alpha rules: \n{all_alpha_ref_rules}')
    
                
    
 
#print(f'Total of answers: {tot_answers}')
end = timeit()
print(f'Solution time: {end-start}')