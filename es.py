#Filename:  es.py
#Author:    Mark Parry
#Created:   04/03/2021
#Purpose:   Weekly task 7 program that reads in a text file and outputs the number of e's it contains, gets the filename from the command line i.e. $ python es.py moby-dick.txt, makes use of the regular exprssions module (re)
#references: https://www.w3schools.com/python/python_regex.asp
#            https://www.tutorialspoint.com/python/python_command_line_arguments.htm

#no error checking in this yet
import sys
import re

filename = sys.argv[1]


with open(filename) as infile:
    data = infile.read()

count = len(re.findall("e",data))


print(count)