#   Advent of Code problem 19 part 1 - Monster Message - Program by Greg Brinks

from timeit import default_timer as timeit
start= timeit()

import csv, re

ing_regex = r'(\w+)'
foods_list = []

def find_ex_allergen(possibilities):
    for i in range(0,len(possibilities)):
        if len(possibilities[i][1]) == 1:# we've determined the exact match
            return i
    return None

def move_allergen(ex_list,poss_list,aller):   #  aller is index in poss_list of allergen to move
    move_list = []
    move_list.append(poss_list[aller][0])
    aller_ing = poss_list[aller][1].pop()
    move_list.append(aller_ing)
    del poss_list[aller]
    ex_list.append(move_list)
    for i in range(len(poss_list)):   #  look at other possibilities and remove the aller_ing
        if aller_ing in poss_list[i][1]:
            poss_list[i][1].remove(aller_ing)
    return ex_list, poss_list          

def all_ings(aller_ings):
    aller_ings = sorted(aller_ings, key=lambda x:x[0])
    ing_list = []
    for i in range(len(aller_ings)):
        ing_list.append(aller_ings[i][1])
    return ing_list

def ings_after_removing_bad(foods,bad):
    tot_ings = 0
    for i in range(len(foods)):
        for j in range(len(bad)):
            if bad[j] in foods[i][1]:
                foods[i][1].remove(bad[j])
        tot_ings += len(foods[i][1])
    return tot_ings


with open("Advent of Code problem 21 - Allergen Assessment data.txt") as aa_file:
    file_contents = csv.reader(aa_file, delimiter='\n')

    i = 0
    for line in file_contents:
        
        fields = re.findall(ing_regex,line[0])
        ix = fields.index('contains')
        foods_data = []
        foods_data.append(i)
        foods_data.append(set(fields[0:ix]))
        foods_data.append(set(fields[ix+1:]))
        foods_list.append(foods_data)
        i += 1
        
    poss_allergen_list = []
    exact_allergen_list = []
    evaled_allergens = []
    for i in range(0,len(foods_list)):
        for allergen in foods_list[i][2]:
            if allergen in evaled_allergens:
                continue
            evaled_allergens.append(allergen)
            allergen_list = []
            for food in foods_list:
                if allergen in food[2]:
                    allergen_list.append(food[0])
            allergen_possibilities = foods_list[allergen_list[0]][1]
            for i in range(1,len(allergen_list)):
                allergen_possibilities = allergen_possibilities & foods_list[allergen_list[i]][1]
            #ex_allergen = []
            poss_allergen = []
            #if len(allergen_possibilities) == 1:
            #   ex_allergen.append(allergen)
            #    ex_allergen.append(allergen_possibilities.pop())
            #    exact_allergen_list.append(ex_allergen)
            #else:
            poss_allergen.append(allergen)
            poss_allergen.append(set(allergen_possibilities))
            poss_allergen_list.append(poss_allergen)
            
    ex_aller_list = []
    
    while True:     #   LOOK AT THIS SOME MORE FOR WAYS TO REMOVE MATCHED ALLERGENS FROM POSSIBILITIES
        ex_aller = find_ex_allergen(poss_allergen_list)
        if ex_aller == None:
            break
        ex_aller_list, poss_allergen_list = move_allergen(ex_aller_list,poss_allergen_list,ex_aller)
        
    bad_ings = all_ings(ex_aller_list)
    remaining_ings = ings_after_removing_bad(foods_list,bad_ings)  
                  
print(f'Total remaining non-bad ingredients: {remaining_ings}')
bad_ing_str = ''
for bad_ing in bad_ings:
    bad_ing_str = bad_ing_str+bad_ing+','
print(f'Bad ingredients: {bad_ing_str}')
end = timeit()
print(f'Solution time: {end-start}')