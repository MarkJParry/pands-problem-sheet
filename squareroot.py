#Filename:  squareroot.py
#Author:    Mark Parry
#Created:   28/02/2021
#Purpose:  finds the square root of a number using the newton square root method
#accept a number and a tolerance , finishes when the tolerance is minimal compared to assumed root)
#iterative formula for square root = .5(x+n/x)
#tried this on paper very cool 
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#https://en.wikipedia.org/wiki/Newton%27s_method
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
#rat run on connections to other things whilst researching(bones babylonian maths prizes etc) but very interesting
#http://www.math.com/school/subject1/lessons/S1U1L9DP.html - simple lesson for manual calc.

#n is the number to find the square root of and t is the toleranace level to enable us to stop calculating "(x-root) < t"
def newton(n,t):
    x = n
    while t < x:
        root = .5 * (x + (n/x))
        if (x - root) < t:
            break
        x = root
    return root

numIn = float(input("Please enter a postive number: "))
result = newton(numIn,.000001)
print("The square root of {} is approx {}".format(numIn, round(result,4)))