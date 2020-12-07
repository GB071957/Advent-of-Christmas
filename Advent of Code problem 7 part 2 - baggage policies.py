#   Advent of Code problem 7 part 2  Program by Greg Brinks


from timeit import default_timer as timeit
start= timeit()

import csv, re


with open("Advent of Code problem 7 - Baggage Rules.txt") as br_file:
    file_contents = csv.reader(br_file, delimiter='\n')

    bag_contents = {}
    for line in file_contents:
        bag = re.findall(r'(\w+ \w+) bags contain',line[0])
        contents = re.findall(r'(\d) (\w+ \w+) bag',line[0])
        d2 = {}
        for content in contents:
            d2.update({content[1]:int(content[0])})
        bag_contents.update({bag[0]:d2})
    
    sbg_contents = []
    total_bags = 0
    for bag,num in bag_contents['shiny gold'].items():
        sbg_contents.append((bag, int(num)))
        total_bags += int(num)
    
    for combo in sbg_contents:
        for bag,num in bag_contents[combo[0]].items():
            total_bags += int(num)*combo[1]
            sbg_contents.append((bag, int(num)*combo[1]))
            
print(f'The shiny gold bag contains {total_bags} bags')

end = timeit()
print(f'Solution time: {end-start}')


