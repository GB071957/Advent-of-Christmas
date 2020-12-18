#   Advent of Code problem 16 part 1 - Shuttle search - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

rules_regex = r'(\d+)-(\d+) or (\d+)-(\d+)'
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
                rf = [int(fields.group(1)),int(fields.group(2)),int(fields.group(3)),int(fields.group(4))]
                rules_fields.append(rf)
        elif (line == [] or line[0]=='your ticket:') and in_my_ticket_section:
            continue
        elif in_my_ticket_section:
            my_ticket_fields = list(int(s) for s in line[0].split(','))
            in_my_ticket_section = False
            in_nearby_ticket_section = True
        elif (line == [] or line[0]=='nearby tickets:') and in_nearby_ticket_section:
            continue
        elif in_nearby_ticket_section:
            nearby_ticket_fields.append(list(int(s) for s in line[0].split(',')))

invalid_tix = 0
number_of_rules = len(rules_fields)
for tick in nearby_ticket_fields:
    rules_broken = 0
    for num in tick:
        for rule in rules_fields:
            if (rule[0]>num or num>rule[1]) and (rule[2]>num or num>rule[3]):
                rules_broken += 1
        if rules_broken == number_of_rules:
            invalid_tix += num
            break
                    
print(f'Ticket scanning error rate: {invalid_tix}')
end = timeit()
print(f'Solution time: {end-start}')