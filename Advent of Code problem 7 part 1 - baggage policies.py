#   Advent of Code problem 7 part 1  Program by Greg Brinks



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
        
    contain_shiny_gold = []
    for bag,contents in bag_contents.items():
        if 'shiny gold' in contents:
            contain_shiny_gold.append(bag)
    for winner in contain_shiny_gold:
        for bag,contents in bag_contents.items():
            if winner in contents and bag not in contain_shiny_gold:
                contain_shiny_gold.append(bag)

print(f'There are {len(contain_shiny_gold)} bags that contain a shiny gold bag')

end = timeit()
print(f'Solution time: {end-start}')


