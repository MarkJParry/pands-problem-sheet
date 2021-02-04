#Filename:  secondString.py
#Author:    Mark Parry
#Created:   03/02/2021
#Purpose:   Read in a string and return it in reverse order skipping every second character.

inString = input("Please enter a message: ")

inStrLen = len(inString)
#This gets the length of the string

inStrIdx = inStrLen
#using the length now as the index  for the string, in this case i want to start at the end of the string

outString = ""
#set up a blank string for the ouput

#loop through the string using the range method starting at the end and working backwards in steps of two
#this way it will skip evey second character

for inStrIdx in range(inStrLen, 0, -2):
    outString += inString[inStrIdx-1:inStrIdx]
    #as python indexes start at 0 and not 1  I have to offset the index by one above to get the starting position of the character i want

print("Your incoming message contained {} characters \nIt is now backwards with every second character skipped and reads: {} \nand is {} characters long".format(inStrLen,outString,len(outString)))
 
