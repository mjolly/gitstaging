'''
  Author: __mjolly__
  email: mangesh.jolly@gmail.com
'''

import sys
import csv
import datetime
import os.path
import argparse


def command_line(*args):


  try:
    if len(args[0]) == 1:
      str_parse(args[0][0])
    elif len(args[0]) >= 3 and len(args[0]) <= 5:
      str_parse_file(args[0][0::2])
    else:
      print 'Error: Unexpected arguments type'
  except SyntaxError:
    print 'Exception: Unexpected arguments type'
    print 'Arguments : ' + str(args)
  

def str_parse(sub_str):
  

  try:
    os.path.exists("/temp/record1.csv")
  except IOError:
    print 'DevError:Check filepath/filename'
    exit()

  
  try:
    csv_file_reader = open("/temp/record1.csv","r")
    cur_reader = csv.reader(csv_file_reader, delimiter=',') 
    cur_work_list = []
  except IOError:
    print 'IOError: check input file data quality'
    exit()

  
  for row in cur_reader:
    cur_work_list.append(row)


  try:
    os.path.exists("/temp/logfile.csv")
  except IOError:
    print 'DevError:Check filepath/filename for logfile'
    exit()


  csv_file_writer = open("/temp/logfile.csv", "a")
  cur_writer = csv.writer(csv_file_writer, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


  for list_record in cur_work_list:
    cur_parse = (' '.join(list_record)).lower()
    cur_result = cur_parse.find(sub_str)
    if  ( cur_result != -1 ): 
      print list_record
      cur_writer.writerow([datetime.datetime.now(), list_record])
      
      
  csv_file_writer.close() 
  csv_file_reader.close()
  return

def str_parse_file(*file_param ):
  

  for index in range(len(file_param[0][1:])):
    try:
      os.path.exists(str(file_param[0][1:]))
      continue
    except IOError:
      print 'DevError:Check filepath/filename'
      exit()


  sub_str = file_param[0][0]
  
  if len(file_param[0][1:]) > 1:
    pipe_bit = 1
    input_file = str(file_param[0][1])
    output_file = str(file_param[0][2])
  else:
    input_file = str(file_param[0][1])
    pipe_bit = 0 


  try:
    csv_file_reader = open(str(input_file),"r")
    cur_reader = csv.reader(csv_file_reader, delimiter=',') 
  except IOError:
    print 'IOError: check input file data quality'
    exit()

  cur_work_list = []  

  for row in cur_reader:
    cur_work_list.append(row)


  try:
    os.path.exists("/temp/logfile.csv")
  except IOError:
    print 'DevError:Check filepath/filename for logfile'
    exit()


  csv_file_writer = open("/temp/logfile.csv", "a")
  cur_writer = csv.writer(csv_file_writer, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

  if pipe_bit == 0:
    for list_record in cur_work_list:
      cur_parse = (' '.join(list_record)).lower()
      print cur_parse
      cur_result = cur_parse.find(sub_str)
      if  ( cur_result != -1 ): 
        print list_record
        cur_writer.writerow([datetime.datetime.now(), list_record])
        print 'if'
    del cur_work_list[:]  
    csv_file_writer.close() 
    csv_file_reader.close()
  else:
    first_file_parse_list = []
    cur_writer.writerow(['first_file_parse_result'])
    for list_record in cur_work_list:
      cur_parse = (' '.join(list_record)).lower()
      cur_result = cur_parse.find(sub_str)
      if  ( cur_result != -1 ): 
        print list_record      
        cur_writer.writerow([datetime.datetime.now(), list_record])
        first_file_parse_list.append(list_record)
    print first_file_parse_list


    try:
      csv_output_file_reader = open(str(output_file),"r")
      cur_output_reader = csv.reader(csv_output_file_reader, delimiter=',') 
    except IOError:
      print 'IOError: check input file data quality'
      exit()
    cur_output_work_list = []
    
    for cur_row in cur_output_reader:
      cur_output_work_list.append(cur_row)

    cur_writer.writerow(['second_file_parse_result'])   
    for list_item in first_file_parse_list:
      if list_item in cur_output_work_list:
        print list_item
        cur_writer.writerow([datetime.datetime.now(), list_item])
  
    del cur_work_list[:]  
    del cur_output_work_list[:]
    csv_file_writer.close() 
    csv_output_file_reader.close()
    csv_file_reader.close()
      

def main():

 
  parser = argparse.ArgumentParser()
  parser.add_argument("strparam", help="input string parameter")
  parser.add_argument('-i', '--input', help="input file name", required=False)
  parser.add_argument('-o', '--output',help="Output file name", required=False)
  
 
  try:
    args = parser.parse_args()
  except SystemExit:
    print("----UsageHelp: bash# filename.py <stringParam> -i <inputFileName:Required> -o <outputFileName:Optional>")
    exit()
   
  command_line(sys.argv[1:])


if __name__ == '__main__':
  main()
