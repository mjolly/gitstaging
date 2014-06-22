import sys
import csv
import os.path

def command_line(inputstr):
  
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
  print 'String Parser-Analyzer for Files\n'
  print   

  if len(sys.argv) == 4:
    searchstr = sys.argv[1]
    file_str_first = str(sys.argv[2])
    file_str_second = str(sys.argv[3])
    command_line(searchstr, file_str_first, file_str_second)
  elif len(sys.argv) == 3:
    searchstr = sys.argv[1]
    file_str_first = str(sys.argv[2])
    command_line(searchstr, file_str_first)  
  elif len(sys.argv) == 2:
    searchstr = sys.argv[1]
    command_line(searchstr)
  else:
    print 'DevError: undefined function'

if __name__ == '__main__':
  main()
