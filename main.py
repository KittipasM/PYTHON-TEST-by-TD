# Receive input from user
source = input("Enter the Source Address : ")
target = input("Enter the Target Address : ")

# Read "text" file from source and print output to console
infile = open(source)
char_count = 0
for line in infile:
    char = ""
    for e in line:
        if e == "\t":
            char += "_"
        elif e == "\n":
            char = char
        else:
            char += e.lower()
    char_count += len(char)
    print(char)
print("Number of characters :", char_count)
infile.close()

#----------------------------------------------------------------------------------------------------------------------------------------------#

# 1.Read "text" file from source and write it to target
infile = open(source)
outfile = open(target, "w")
char_count = 0
for line in infile:
    char = ""
    for e in line:
        if e == "\t":
            char += "_"
        elif e == "\n":
            char = char
        else:
            char += e.lower()
    char_count += len(char)
    outfile.write(char + "\n")
outfile.write(str(char_count))
infile.close()
outfile.close()

#----------------------------------------------------------------------------------------------------------------------------------------------#

# 1.Read file from database (Assume that we connect to mysql database)
import pymysql
class Config:
  mysql_host = ""
  mysql_port = ""
  mysql_user = ""
  mysql_password = ""
  mysql_db = ""
  mysql_charset = ""
  
connection = pymysql.connect(host = Config.mysql_host,
                             port = Config.mysql_port,
                             user = Config.mysql_user,
                             password = Config.mysql_password,
                             db = Config.mysql_db,
                             charset = Config.mysql_charset,
                             cursorclass = pymysql.cursors.DictCursor)

with connection.cursor() as cursor:
  cursor.execute("select * from data_file")
  result = cursor.fetchall()
  
#----------------------------------------------------------------------------------------------------------------------------------------------#

# 2.Add new statistic calculation (count the number of lines)
infile = open(source)
char_count = 0
line_count = 0
for line in infile:
    char = ""
    for e in line:
        if e == "\t":
            char += "_"
        elif e == "\n":
            char = char
        else:
            char += e.lower()
    char_count += len(char)
    line_count += 1
    print(char)
print("Number of characters :", char_count)
print("Number of lines :", line_count)
infile.close()

#----------------------------------------------------------------------------------------------------------------------------------------------#

# 3.Receive "source" and "target" from config file
!pip install python-dotenv
import os
from dotenv import load_dotenv
load_dotenv()
class Config:
  source = os.getenv("source")
  target = os.getenv("target")
