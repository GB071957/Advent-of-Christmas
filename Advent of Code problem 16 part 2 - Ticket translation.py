#   Advent of Code problem 16 part 2 - Shuttle search - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

def valid_tickets(rules,tix):
    invalid_tix = 0
    number_of_rules = len(rules_fields)
    valid_tix = []
    for tick in nearby_ticket_fields:
        
        tick_is_valid = True
        for num in tick:
            rules_broken = 0
            for rule in rules_fields:
                if (rule[0]>num or num>rule[1]) and (rule[2]>num or num>rule[3]):
                    rules_broken += 1
            if rules_broken < number_of_rules:   # num is in at least one valid range
                continue
            else:    #num is not in any valid range -- the ticket is invalid
                tick_is_valid = False
                break
        if tick_is_valid:
            valid_tix.append(tick)
    return valid_tix

rules_regex = r'(\w+ ?\w*): (\d+)-(\d+) or (\d+)-(\d+)'
rule_names = []
rules_fields = []
nearby_ticket_fields = []

with open("Advent of Code problem 16 - ticket data.txt") as ticket_file:
    file_contents = csv.reader(ticket_file, delimiter='\n')
        
    line_count = 0
        
    in_rule_data_section = True
    in_my_ticket_section = False
    in_nearby_ticket_section = False

    for line in file_contents:
        if in_rule_data_section:
            if line == []:
                in_rule_data_section = False
                in_my_ticket_section = True
            else:
                fields = re.search(rules_regex,line[0])
                rf = [int(fields.group(2)),int(fields.group(3)),int(fields.group(4)),int(fields.group(5))]
                rules_fields.append(rf)
                rule_names.append(fields.group(1))
        elif (line == [] or line[0]=='your ticket:') and in_my_ticket_section:
            continue
        elif in_my_ticket_section:
            lin = line[0]
            my_ticket_fields = list(int(st) for st in lin.split(','))
            in_my_ticket_section = False
            in_nearby_ticket_section = True
        elif (line == [] or line[0]=='nearby tickets:') and in_nearby_ticket_section:
            continue
        elif in_nearby_ticket_section:
            nearby_ticket_fields.append(list(int(s) for s in line[0].split(',')))

valids = valid_tickets(rules_fields,nearby_ticket_fields)

#  allow for each number field to represent each possible rule
poss_rules = []
for i in range(0,len(rules_fields)):
    pr = []
    for j in range(0,len(rules_fields)):
        pr.append(j)
    poss_rules.append(pr)

#  now go through nearby ticket data, eliminating possible rules for each field
for tick in valids:
    for field in range(0,len(tick)):
        for j in range(0,len(rules_fields)):
            if j in poss_rules[field] and (tick[field]<rules_fields[j][0] or tick[field]>rules_fields[j][1]) and \
               (tick[field]<rules_fields[j][2] or tick[field]>rules_fields[j][3]):  #  this field is not field j
                #print(f'tick: {tick}, field: {field}, j: {j}')
                poss_rules[field].remove(j)
                
final_positions = [-1]*len(poss_rules)

while True:
    singular_rule = -1
    for i in range(0,len(poss_rules)):   # i represent field numbers on tickets
        if len(poss_rules[i]) == 1:
            singular_rule = i
            rule_num = poss_rules[i][0]
            break
    if singular_rule <0:
        break
    else:
        for j in range(0,singular_rule):
            if rule_num in poss_rules[j]:
                poss_rules[j].remove(rule_num)
        for j in range(singular_rule+1,len(poss_rules)):
            if rule_num in poss_rules[j]:
                poss_rules[j].remove(rule_num)
        final_positions[singular_rule] = rule_num
        poss_rules[singular_rule] = []

#  Multiply together the values on my ticket relate to departures
my_value = 1
for m in range(0,len(rule_names)):
    if 'departure' in rule_names[m]:
        ix = final_positions.index(m)
        my_value *= my_ticket_fields[ix]
        

print(f'My value: {my_value}')
end = timeit()
print(f'Solution time: {end-start}')