
#In [138]:
# Setup.
import copy
import csv
import os
from pprint import pprint
os.chdir('/home/user/temp')



#In [139]:
# Import csv files into list.
csv_file_list = []
for file_num in [1, 2]:
    filename = ''.join(['my_csv_file', str(file_num), '.csv'])
    with open(filename, 'r') as cur_file:
        cur_reader = csv.reader(cur_file, delimiter=';')
        cur_file_list = []
        for row in cur_reader:
            cur_file_list.append(row)
    csv_file_list.append(cur_file_list)
pprint('List of all CSV files:')
pprint(csv_file_list)
print ''
pprint('List of CSV file 1:')
pprint(csv_file_list[1])
print ''

#Out [139]:
'List of all CSV files:'
[[['1', 'Rich', 'M', 'Kinder'],
  ['2', 'John', 'Steven', 'Doe'],
  ['3', 'Jim', '', 'Smith'],
  ['4', 'Jess', 'Q', 'White'],
  ['5', 'Sue', 'R', 'White']],
 [['1', 'George', '', 'Michaels'],
  ['2', 'Sally', 'Q', 'Person'],
  ['3', 'Jason', '', 'Bourne'],
  ['4', 'Richie', 'Michael', 'Kinder'],
  ['5', 'Mary', 'X', 'White'],
  ['6', 'Sue', 'R', 'White']]]

'List of CSV file 1:'
[['1', 'George', '', 'Michaels'],
 ['2', 'Sally', 'Q', 'Person'],
 ['3', 'Jason', '', 'Bourne'],
 ['4', 'Richie', 'Michael', 'Kinder'],
 ['5', 'Mary', 'X', 'White'],
 ['6', 'Sue', 'R', 'White']]



#In [140]:
# Import csv files into tuples.
csv_file_list = []
for file_num in [1, 2]:
    filename = ''.join(['my_csv_file', str(file_num), '.csv'])
    with open(filename, 'r') as cur_file:
        cur_reader = csv.reader(cur_file, delimiter=';')
        cur_file_list = []
        for row in cur_reader:
            cur_file_list.append(tuple(row))
    csv_file_list.append(tuple(cur_file_list))
csv_file_list = tuple(csv_file_list)

pprint('List of all CSV files:')
pprint(csv_file_list)
print ''
pprint('List of CSV file 1:')
pprint(csv_file_list[1])
print ''

#Out [140]:
'List of all CSV files:'
((('1', 'Rich', 'M', 'Kinder'),
  ('2', 'John', 'Steven', 'Doe'),
  ('3', 'Jim', '', 'Smith'),
  ('4', 'Jess', 'Q', 'White'),
  ('5', 'Sue', 'R', 'White')),
 (('1', 'George', '', 'Michaels'),
  ('2', 'Sally', 'Q', 'Person'),
  ('3', 'Jason', '', 'Bourne'),
  ('4', 'Richie', 'Michael', 'Kinder'),
  ('5', 'Mary', 'X', 'White'),
  ('6', 'Sue', 'R', 'White')))

'List of CSV file 1:'
(('1', 'George', '', 'Michaels'),
 ('2', 'Sally', 'Q', 'Person'),
 ('3', 'Jason', '', 'Bourne'),
 ('4', 'Richie', 'Michael', 'Kinder'),
 ('5', 'Mary', 'X', 'White'),
 ('6', 'Sue', 'R', 'White'))



#In [141]:
# Collect all last name matches into a third file.
first_file_list = csv_file_list[0]
second_file_list = csv_file_list[1]
third_file_list = []
for x in first_file_list:
    for y in second_file_list:
        # If the last name matches, add both to the third file
        # if they aren't already there, and indicate their
        # source file (first or second).
        if x[3] == y[3]:
            new_x = ('first',) + x
            new_y = ('second',) + y
            if new_x not in third_file_list:
                third_file_list.append(new_x)
            if new_y not in third_file_list:
                third_file_list.append(new_y)
third_file_list = sorted(third_file_list)
pprint(third_file_list)

#Out [141]:
[('first', '1', 'Rich', 'M', 'Kinder'),
 ('first', '4', 'Jess', 'Q', 'White'),
 ('first', '5', 'Sue', 'R', 'White'),
 ('second', '4', 'Richie', 'Michael', 'Kinder'),
 ('second', '5', 'Mary', 'X', 'White'),
 ('second', '6', 'Sue', 'R', 'White')]



#In [142]:
# Import csv files into dict.
csv_file_dict = {}
for file_num in [1, 2]:
    filename = ''.join(['my_csv_file', str(file_num), '.csv'])
    with open(filename, 'r') as cur_file:
        cur_reader = csv.reader(cur_file, delimiter=';')
        cur_file_dict = {}
        for row in cur_reader:
            cur_file_dict[row[3]] = row[:3]

            
    csv_file_dict[file_num] = cur_file_dict
    #my_dict[key] = value

pprint('Dictionary of all CSV files:')
pprint(csv_file_dict)
print ''
pprint('Dictionary of CSV file 1:')
pprint(csv_file_dict[1])
print ''
pprint('Keys of file 1:')
pprint(csv_file_dict[1].keys())
print ''
pprint('Values of file 1:')
pprint(csv_file_dict[1].values())
print ''
pprint('Items of file 1:')
pprint(csv_file_dict[1].items())
print ''

#Out [142]:
'Dictionary of all CSV files:'
{1: {'Doe': ['2', 'John', 'Steven'],
     'Kinder': ['1', 'Rich', 'M'],
     'Smith': ['3', 'Jim', ''],
     'White': ['5', 'Sue', 'R']},
 2: {'Bourne': ['3', 'Jason', ''],
     'Kinder': ['4', 'Richie', 'Michael'],
     'Michaels': ['1', 'George', ''],
     'Person': ['2', 'Sally', 'Q'],
     'White': ['6', 'Sue', 'R']}}

'Dictionary of CSV file 1:'
{'Doe': ['2', 'John', 'Steven'],
 'Kinder': ['1', 'Rich', 'M'],
 'Smith': ['3', 'Jim', ''],
 'White': ['5', 'Sue', 'R']}

'Keys of file 1:'
['Kinder', 'White', 'Smith', 'Doe']

'Values of file 1:'
[['1', 'Rich', 'M'],
 ['5', 'Sue', 'R'],
 ['3', 'Jim', ''],
 ['2', 'John', 'Steven']]

'Items of file 1:'
[('Kinder', ['1', 'Rich', 'M']),
 ('White', ['5', 'Sue', 'R']),
 ('Smith', ['3', 'Jim', '']),
 ('Doe', ['2', 'John', 'Steven'])]



#In [143]:
# Identify keys in common hopefully in O(n) by using sets.
dict_1_keys_set = set(csv_file_dict[1].keys())
dict_2_keys_set = set(csv_file_dict[2].keys())
intersection = dict_1_keys_set.intersection(dict_2_keys_set)
pprint('Dictionary 1 keys set:')
pprint(dict_1_keys_set)
pprint('Dictionary 2 keys set:')
pprint(dict_2_keys_set)
pprint('Intersection:')
pprint(intersection)

#Out [143]:
'Dictionary 1 keys set:'
set(['Doe', 'Kinder', 'Smith', 'White'])
'Dictionary 2 keys set:'
set(['Bourne', 'Kinder', 'Michaels', 'Person', 'White'])
'Intersection:'
set(['Kinder', 'White'])


