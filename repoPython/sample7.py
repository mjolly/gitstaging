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
# Comment: Function for argument parameter handling and invoking sub functions

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
# function to search for sub string in an developer provided source file  

  if not os.path.exists("/temp/record1.csv"):
    print 'File IO Error :Check filepath/filename'
    return
 
  csv_input_file_obj = open("/temp/record1.csv","r")  # input file object
  cur_reader = csv.reader(csv_input_file_obj, delimiter=',')
  if cur_reader == []:
    print 'IOError: check input file data quality for comma separators'
    return
 
  
  if not os.path.exists("/temp/logfile.csv"):
    print 'File IO Error:Check filepath/filename'
    return

  csv_log_file_obj = open("/temp/logfile.csv", "a") # log file object
  cur_writer = csv.writer(csv_log_file_obj, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)


  cur_writer.writerow(['single_file_parse_result']) 
# code block to search sub string in input file and write results to log file
  for row in cur_reader:
    cur_parse = (' '.join(row)).lower()
    cur_result = cur_parse.find(sub_str)
    if cur_result != -1 :
      print row
      cur_writer.writerow([datetime.datetime.now(), row])
# end of file parse code block      
      
  csv_input_file_obj.close() 
  csv_log_file_obj.close()


def str_parse_file(*file_param ):
  
# sub string search function to parse user provided csv files *limit set to two input files*
  for file_name in file_param[0][1:]:
    if not os.path.exists(str(file_name)):
      print 'File IO Error:Check filepath/filename'
      return

  sub_str = file_param[0][0]
# code to check for single or multiple input files
  if len(file_param[0][1:]) > 1:
    pipe_bit = 1
    input_file = str(file_param[0][1])
    output_file = str(file_param[0][2])
  else:
    input_file = str(file_param[0][1])
    pipe_bit = 0 

# code to check for csv file data quality
  csv_first_file_obj = open(str(input_file),"r")
  cur_reader = csv.reader(csv_first_file_obj, delimiter=',') 
  if cur_reader == []:
    print 'IOError: check input file data quality for comma separators'    
    return

  cur_work_list = []  

  for row in cur_reader:
    cur_work_list.append(row)

# code to check for log file
  if not os.path.exists("/temp/logfile.csv"):
    print 'File IO Error:Check filepath/filename'
    return


  csv_log_file_obj = open("/temp/logfile.csv", "a")
  cur_writer = csv.writer(csv_log_file_obj, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)

  if pipe_bit == 0: # start code block to search sub string in user provided single csv file
    cur_writer.writerow(['first_file_parse_result'])
    for list_record in cur_work_list:
      cur_parse = (' '.join(list_record)).lower()
      cur_result = cur_parse.find(sub_str)
      if  ( cur_result != -1 ): 
        print list_record
        cur_writer.writerow([datetime.datetime.now(), list_record])
    del cur_work_list[:]  
    csv_first_file_obj.close() 
    csv_log_file_obj.close()
  else:  # start code block to search sub string in multiple user provided csv files *uses data pipeline*
    first_file_parse_list = []
    cur_writer.writerow(['first_file_parse_result'])
    for list_record in cur_work_list:
      cur_parse = (' '.join(list_record)).lower()
      cur_result = cur_parse.find(sub_str)
      if  ( cur_result != -1 ): 
        print list_record      
        cur_writer.writerow([datetime.datetime.now(), list_record])
        first_file_parse_list.append(list_record)
    print first_file_parse_list # search result from first csv file


    csv_second_file_obj= open(str(output_file),"r")
    cur_output_reader = csv.reader(csv_second_file_obj, delimiter=',') 
    if cur_output_reader == []:
      print 'IOError: check input file data quality for comma separators'    
      return
    cur_output_work_list = []
    
    for cur_row in cur_output_reader:
      cur_output_work_list.append(cur_row)

    cur_writer.writerow(['second_file_parse_result'])   
    for list_item in first_file_parse_list: # code block that searches results of first csv file in the second csv file
      if list_item in cur_output_work_list:
        print list_item
        cur_writer.writerow([datetime.datetime.now(), list_item])
  
    del cur_work_list[:]  
    del cur_output_work_list[:]
    csv_first_file_obj.close() 
    csv_second_file_obj.close()
    csv_log_file_obj.close()
      

def main():

# command line utlity for input parameters 
  parser = argparse.ArgumentParser()
  parser.add_argument("strparam", help="input string parameter")
  parser.add_argument('-i', '--input', help="input file name", required=False)
  parser.add_argument('-o', '--output',help="Output file name", required=False)
  
 
  try:
    args = parser.parse_args()
  except SystemExit:
    print("----UsageHelp: bash# filename.py <stringParam> -i <inputFileName:Required> -o <outputFileName:Optional>")
    raise
# caller function to command_line(*args) passing reference to command line input parameters
  command_line(sys.argv[1:])


if __name__ == '__main__':
  main()
