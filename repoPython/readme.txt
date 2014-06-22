== CSV File Parser Utility to search Substring ==
Author: Jolly, Mangesh -- Email: mangesh.jolly@gmail.com
Tags: file parser, substring, python, command line param
Requires at least: Python 2.7
Tested on: Python 2.7, emacs 22.1.1
Optional: program works from bash using python interpreter and the emacs python mode.

Description:

The sub string file parser utility allows the user to supply a sub string and/or file(s) source as a command line argument.
The sub string provided by the user can be alpha numeric with special characters.
The sub string in any form (case independent) gets searched in the input file(s).
The sub string can be searched in one single source or in multiple files.
The sub string search result from the first file gets pipelined to second file for further search.


Usage Instructions:

1. Create /temp directory in your root directory.
2. Copy all the files in the zip folder to the /temp directory
3. Modify the /temp directory permissions to all users read/write/execute.
4. Check if the /temp/record1.csv, /temp/record2.csv and the /temp/logfile.csv are present in the temp directory.
5. Sample files are provided along with the python program file.
6. All final output for program is written to logfile.csv


Usage Sample Commands:

# cd pwd
/temp/
# ls
readme.txt
record1.csv
record2.csv
logfile.csv
sample7.py

# python sample7.py -h
#usage: sample7.py [-h] [-i INPUT] [-o OUTPUT] strparam
----UsageHelp: bash# filename.py <stringParam> -i <inputFileName:Required> -o <outputFileName:Optional>

# python sample7.py 3010
['1', '87690', 'mangesh', 'jolly', '(541) 754-3010', '(213) 595 2527', 'mangesh.jolly@gmail.com', 'developer']
['2', '92837', 'elizabeth', 'beaty', '(714) 595 7623', '(714) 595-3010', 'ebeaty@gmail.com', 'staff']
['6', '87690', 'mangeshd', 'jolly', '1 (541) 7543010', '(213) 595 2527', 'mangesh.jolly@gmail.com', 'developer']

# python sample7.py price
['3', '67891', 'megan', 'price', '(415) 234 5890', '(415) 555 8989', 'mprice@gmail.com', 'director']
['4', '67891', 'megan', 'Eprice', '(415) 234-5890', '(415) 555 8989', 'mprice@gmail.com', 'director']
['5', '67891', 'megan', 'PRICE', '(415) 234 5890', '(415)-555-8989', 'mprice@gmail.com', 'director']
['7', '67891', 'megane', 'PRICE', '(415) 234 5890', '(415)-555-8989', 'mprice@gmail.com', 'director']

# python sample7.py -8989 -i /temp/record1.csv
['5', '67891', 'megan', 'PRICE', '(415) 234 5890', '(415)-555-8989', 'mprice@gmail.com', 'director']
['7', '67891', 'megane', 'PRICE', '(415) 234 5890', '(415)-555-8989', 'mprice@gmail.com', 'director']

# python sample7.py 3010 -i /temp/record1.csv -o /temp/record2.csv
['1', '87690', 'mangesh', 'jolly', '(541) 754-3010', '(213) 595 2527', 'mangesh.jolly@gmail.com', 'developer']
['2', '92837', 'elizabeth', 'beaty', '(714) 595 7623', '(714) 595-3010', 'ebeaty@gmail.com', 'staff']
['6', '87690', 'mangeshd', 'jolly', '1 (541) 7543010', '(213) 595 2527', 'mangesh.jolly@gmail.com', 'developer']
[['1', '87690', 'mangesh', 'jolly', '(541) 754-3010', '(213) 595 2527', 'mangesh.jolly@gmail.com', 'developer'], ['2', '92837', 'elizabeth', 'beaty', '(714) 595 7623', '(714) 595-3010', 'ebeaty@gmail.com', 'staff'], ['6', '87690', 'mangeshd', 'jolly', '1 (541) 7543010', '(213) 595 2527', 'mangesh.jolly@gmail.com', 'developer']]

# python sample7.py '714)' -i /temp/record1.csv -o /temp/record2.csv
['2', '92837', 'elizabeth', 'beaty', '(714) 595 7623', '(714) 595-3010', 'ebeaty@gmail.com', 'staff']
[['2', '92837', 'elizabeth', 'beaty', '(714) 595 7623', '(714) 595-3010', 'ebeaty@gmail.com', 'staff']]
['2', '92837', 'elizabeth', 'beaty', '(714) 595 7623', '(714) 595-3010', 'ebeaty@gmail.com', 'staff']

# 
