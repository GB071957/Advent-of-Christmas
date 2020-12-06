#   Advent of Code problem 1  Program by Greg Brinks

# Find two numbers in the list of 200 that add to 2020 and multiply them together

from timeit import default_timer as timeit
start= timeit()

import csv

num_captured = 0

expenses = []

with open("Advent of Code problem 1.txt") as expense_file:
    file_contents = csv.reader(expense_file, delimiter='\n')

    for line in file_contents:
        expenses.append(int(line[0]))

for i in range(len(expenses)):
    for j in range(i,len(expenses)):
        if expenses[i] + expenses[j] == 2020:
            print(f'Expenses {expenses[i]} and {expenses[j]} sum to 2020 and multiplied equal {expenses[i]*expenses[j]}')
            break

