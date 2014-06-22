'''
  Author: __mjolly__
  email: mangesh.jolly@gmail.com
'''

import sys
import csv
import datetime
import os.path
import argparse


#def command_line(input_str, *args):
def command_line(*args):

#  print input_str
#  print args[0]
#  param_list = []
#  print args[0][1]
#  print len(args)
#  param_list = list(args)
#  print len(param_list[0])
  
#  print param_list
#  exit() 
 # second = args[2]
#  print len(args)
#  for var in range(len(args)):
#    print var, args[var]
#  exit()
  #newlist = args

  try:
    if len(args[0]) == 1:
      str_parse(args[0][0])
    elif len(args[0]) == 3:
      str_parse_first_file(args[0][0], args[0][2])
    elif len(args[0]) == 5:
      str_parse_first_second_file(args[0][0], args[0][2], args[0][4])
    else:
      print 'DevError: Incorrect argument length'
      exit()
  except:
    print 'Unexpected arguments type'
    print args
    exit()


def str_parse(sub_str):
  
#  print "enter function command_line(inputstr)"
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


def str_parse_first_file(sub_str, input_file ):
  

  try:
    os.path.exists(str(input_file))
  except IOError:
    print 'DevError:Check filepath/filename'
    exit()
  

  try:
    csv_file_reader = open(str(input_file),"r")
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


def str_parse_first_second_file(sub_str, file_input_first, file_input_second):


  print 'Enter two file input mode'
  return


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

'''
  if len(sys.argv) >= 6:
#  command_line(str(sys.argv[1:]))
    command_line(str(sys.argv[1]), str(sys.argv[3]), str(sys.argv[5]))
  elif len(sys.argv) >= 4:
    command_line(str(sys.argv[1]), str(sys.argv[3]))
  elif len(sys.argv) >= 2:
    command_line(str(sys.argv[1]))
  else:
    print "UsageHelp: bash# filename.py <stringParam> -i <inputFilename:Required> -o <outputFileName:Optional>"
'''

if __name__ == '__main__':
  main()
