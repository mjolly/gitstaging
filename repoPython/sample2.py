'''
  Author: __mjolly__
  email: mangesh.jolly@gmail.com
'''

import sys
import csv
import os.path
import argparse


def command_line(inputstr):
  
  print "enter function command_line(inputstr)"
  try:
    os.path.exists("/temp/record1.csv")
  except IOError:
    print 'DevError:Check filepath/filename'
    exit()
  

  csv_file_reader = open("/temp/record1.csv","r")
  cur_reader = csv.reader(csv_file_reader, delimiter=',') 
  cur_work_list = []

  
  for row in cur_reader:
    cur_work_list.append(row)
  

  for list_record in cur_work_list:
    cur_parse = (' '.join(list_record)).lower()
    cur_result = cur_parse.find(inputstr)
    if  ( cur_result != -1 ): 
      print list_record

   
  csv_file_reader.close()
  return

def command_line(inputstr, file_input_str):
  
  csv_file_reader = open(file_input_str,"r")
  print file_input_str
  print inputstr

  return

def command_line(inputstr, file_input_first, file_input_second):


  print 'Enter two file input mode'
  return


def main():
# print 'String Parser-Analyzer for Files\n'
 
  parser = argparse.ArgumentParser()
  parser.add_argument("strparam", help="input string parameter")
  parser.add_argument('-i', '--input', help="input file name", required=False)
  parser.add_argument('-o', '--output',help="Output file name", required=False)
  
 
  try:
    args = parser.parse_args()
  except SystemExit:
    print("UsageHelp: bash# filename.py <stringParam> -i <inputFileName:Required> -o <outputFileName:Optional>")
   
 
  if len(sys.argv) >= 6:
    search_str = sys.argv[1]
    file_str_first = sys.argv[3]
    file_str_second = sys.argv[5]
    command_line(search_str, file_str_first, file_str_second)
  elif len(sys.argv) >= 4:
    search_str = sys.argv[1]
    file_str_first = sys.argv[3]
    command_line(search_str, file_str_first)
  elif len(sys.argv) >= 2:
    print sys.argv[1]
#    search_str = sys.argv[1]
    command_line(str(sys.argv[1]))
  else:
    print "UsageHelp: bash# filename.py <stringParam> -i <inputFilename:Required> -o <outputFileName:Optional>"


if __name__ == '__main__':
  main()
