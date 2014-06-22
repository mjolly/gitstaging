'''
  Author: __mjolly__
  email: mangesh.jolly@gmail.com
'''

import sys
import csv
import datetime
import os.path
import argparse
import pdb


def command_line(*args):


  try:
    if len(args[0]) == 1:
      str_parse(args[0][0])
    elif len(args[0]) >= 3 and len(args[0]) <= 5:
      str_parse_file(args[0][0::2])
    else:
      print 'Error: Unexpected arguments type'
  except SyntaxError:
    print 'RaiseError: Unexpected argument type or File IOError :  ' + str(args)
    raise  


def str_parse(sub_str):
  

  if not os.path.exists("/temp/record1.csv"):
    print 'File IO Error :Check filepath/filename'
    return
 
  csv_input_file_obj = open("/temp/record1.csv","r")
  cur_reader = csv.reader(csv_input_file_obj, delimiter=',')
  if cur_reader == []:
    print 'IOError: check input file data quality for comma separators'
    return
 
  cur_work_list = []
  
  for row in cur_reader:
    cur_work_list.append(row)

  
  if not os.path.exists("/temp/logfile.csv"):
    print 'File IO Error:Check filepath/filename'
    return

  csv_log_file_obj = open("/temp/logfile.csv", "a")
  cur_writer = csv.writer(csv_log_file_obj, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


  for list_record in cur_work_list:
    cur_parse = (' '.join(list_record)).lower()
    cur_result = cur_parse.find(sub_str)
    if cur_result != -1 : 
      print list_record
      cur_writer.writerow([datetime.datetime.now(), list_record])
      
      
  csv_input_file_obj.close() 
  csv_log_file_obj.close()
  return


def str_parse_file(*file_param ):
  

  for file_name in file_param[0][1:]:
    if not os.path.exists(str(file_name)):
      print 'File IO Error:Check filepath/filename'
      return

  sub_str = file_param[0][0]
  
  if len(file_param[0][1:]) > 1:
    pipe_bit = 1
    input_file = str(file_param[0][1])
    output_file = str(file_param[0][2])
  else:
    input_file = str(file_param[0][1])
    pipe_bit = 0 


  csv_first_file_obj = open(str(input_file),"r")
  cur_reader = csv.reader(csv_first_file_obj, delimiter=',') 
  if cur_reader == []:
    print 'IOError: check input file data quality for comma separators'    
    return

  cur_work_list = []  

  for row in cur_reader:
    cur_work_list.append(row)


  if not os.path.exists("/temp/logfile.csv"):
    print 'File IO Error:Check filepath/filename'
    return


  csv_log_file_obj = open("/temp/logfile.csv", "a")
  cur_writer = csv.writer(csv_log_file_obj, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

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
    csv_first_file_obj.close() 
    csv_log_file_obj.close()
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


    csv_second_file_obj= open(str(output_file),"r")
    cur_output_reader = csv.reader(csv_second_file_obj, delimiter=',') 
    if cur_out_reader == []
      print 'IOError: check input file data quality for comma separators'    
      return
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
    csv_first_file_obj.close() 
    csv_second_file_obj.close()
    csv_log_file_obj.close()
      

def main():

 
  parser = argparse.ArgumentParser()
  parser.add_argument("strparam", help="input string parameter")
  parser.add_argument('-i', '--input', help="input file name", required=False)
  parser.add_argument('-o', '--output',help="Output file name", required=False)
  
 
  try:
    args = parser.parse_args()
  except SystemExit:
    print("----UsageHelp: bash# filename.py <stringParam> -i <inputFileName:Required> -o <outputFileName:Optional>")
    raise
   
  command_line(sys.argv[1:])


if __name__ == '__main__':
  main()
