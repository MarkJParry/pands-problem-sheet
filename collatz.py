#Filename:  collatz.py
#Author:    Mark Parry
#Created:   08/02/2021
#Purpose:   Program that asks the user to input any positive integer and outputs the successive values of the following calculation

#Notes:     At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply 
#           it by three and add one. The program will end if the current value is one.



#ask the user to input a number
numIn = abs(int(input("Please enter any positive  number: ")))

#initialise variables for calculation and output

calc = 0
strOut = str(numIn)

#loop until the calculation is 1
while calc != 1:
    
    if numIn % 2 == 0:			
        calc = int(numIn / 2)		#do this if it is even 
    else:						
        calc = int((numIn * 3) + 1)	#do this if it is odd

    strOut += " " + str(calc)	#append the calculation result to the output string
    numIn = calc				#switch numIn with the calculated number otherwise you have an infinite loop as numIn will always be the user inputted number

#print the string of calculations         
print(strOut)



