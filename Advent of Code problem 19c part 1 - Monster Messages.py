#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks
#  revising approach to use reg exes and to explore some of solution ideas from mebeim (another AOC member)

from timeit import default_timer as timeit
start= timeit()

import csv, re, copy

def parse_input(mm_array):
    
    rules = {}

    for line in map(str.rstrip, mm_array):
        if not line:
            break
        
        if ":" in line:
            

        rule_id, options = line.split(': ')
        rule_id = int(rule_id)

        if '"' in options:
            rule = options[1:-1]
        else:
            rule = []
            for option in options.split('|'):
                rule.append(tuple(map(int, option.split())))

        rules[rule_id] = rule
    return rules

def build_regexp(rules, rule=0):
    rule = rules[rule]
    if type(rule) is str:
        return rule

    options = []
    for option in rule:
        option_regex = ''
        for sub_rule in option:
            option_regex += build_regexp(rules, sub_rule)
        options.append(option_regex)

    return '(' + '|'.join(options) + ')'

def match(rules, string, rule=0, index=0):
    # If we are past the end of the string, we can't match anything anymore
    if index >= len(string):
        return []

    # If the current rule is a simple character, match that literally
    rule = rules[rule]
    if type(rule) is str:
        # If it matches, advance 1 and return this information to the caller
        if string[index] == rule:
            return [index + 1]
        # Otherwise fail, we cannot continue matching
        return []

    # If we get here, we are in the case `X: A B | C D`
    matches = []

    # For each option
    for option in rule:
        # Start matching from the current position
        sub_matches = [index]

        # For any rule of this option
        for sub_rule in option:
            # Get all resulting positions after matching this rule from any of the
            # possible positions we have so far.
            new_matches = []
            for idx in sub_matches:
                new_matches += match(rules, string, sub_rule, idx)

            # Keep the new positions and continue with the next rule, trying to match all of them
            sub_matches = new_matches

        # Collect all possible matches for the current option and add them to the final result
        matches += sub_matches

    # Return all possible final indexes after matching this rule
    return matches
    
with open('Advent of Code problem 19 - Monster message data.txt') as mm_file:
    mm_array = mm_file.readlines()

rules = parse_input(mm_array)
rules2 = copy.deepcopy(rules)
rules2[8]  = [(42,), (42, 8)]
rules2[11] = [(42, 31), (42, 11, 31)]
#rexps = re.compile('^' + build_regexp(rules) + '$')

num_valid_messages1 = 0
num_valid_messages2 = 0
for msg in map(str.rstrip, mm_array):
    if len(msg) in match(rules,msg):
        num_valid_messages1 += 1
    if len(msg) in match(rules2,msg):
        num_valid_messages2 += 1
#    if rexps.match(msg):
#        num_valid_messages += 1
            
print(f'Total number of valid messages part 1: {num_valid_messages1}')
print(f'Total number of valid messages part 2: {num_valid_messages2}')
end = timeit()
print(f'Solution time: {end-start}')


