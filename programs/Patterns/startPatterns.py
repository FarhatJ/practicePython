"""
Program 1: Print Dynamic NxN Square * Pattern with n rows:

* * * *            ****   <- (To get this as your output uncomment the second print and comment the first print.)
* * * *     OR     ****     
* * * *            ****
* * * *            ****       

n is user input integer.
"""

print("Program1: Print Square Pattern.")

def squarePattern(n):
    for row in range(n):
        for col in range(n):
            print("* ",end="")
            #print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
squarePattern(n) # function call

print("\n----------------------------------------------------\n")
"""
Program 2: Print Dynamic Left Sided Triangle * Pattern with n rows:

*                  *      <- (To get this as your output uncomment the second print and comment the first print.)
* *         OR     **
* * *              *** 
* * * *            **** 

n is user input integer.
"""

print("\nProgram2: Print Left Sided Triangle Pattern. ")

def leftTriPattern(n):
    for row in range(n):
        for col in range(row+1):
            print("* ",end="")
            #print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
leftTriPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 3: Print Dynamic Reverse Left Sided Triangle * Pattern with n rows:

* * * *            ****    <- (To get this as your output uncomment the second print and comment the first print.)
* * *       OR     ***    
* *                ** 
*                  *

n is user input integer.
"""

print("\nProgram3: Print Reverse Left Sided Triangle Pattern. ")

def leftRevTriPattern(n):
    for row in range(n):
        for col in range(row, n):
            print("* ",end="")
            #print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
leftRevTriPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 4: Print Dynamic Right sided triangle * Pattern with n rows:

   *
  **  
 ***
****	

n is user input integer.
"""

print("Program4: Print Right Sided Triangle Pattern.")

def rightTriPattern(n):
    for row in range(n):
        for space in range(row,n):
            print(" ",end="")
        for col in range(row+1):
            print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
rightTriPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 5: Print Dynamic Right Sided Reverse Triangle * Pattern with n rows:

 ****
  ***
   **
    *

n is user input integer.
"""

print("Program5: Print Right Sided Reverse Triangle Pattern. ")

def rightRevTriPattern(n):
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row, n):
            print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
rightRevTriPattern(n) # function call


print("\n----------------------------------------------------\n")

"""
Program 6: Print Dynamic Hill or Pyramid * Pattern with n rows:
 
       * 
      ***  
     ***** 
    *******
	
n is user input integer.
"""

print("Program6: Print Hill or Pyramid Pattern.")

def hillPattern(n):
    for row in range(n):
        for space in range(row,n):
            print(" ",end="")
        for col in range(row):
            print("*",end="")
        for col in range(row+1):
            print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
hillPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 7: Print Dynamic Reverse Hill or Pyramid * Pattern with n rows:

  *******
   *****
    *** 
     *   
	
n is user input integer.
"""

print("Program7: Print Reverse Hill or Pyramid Pattern.")

def revHillPattern(n):
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row,n-1):
            print("*",end="")
        for col in range(row, n):
            print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
revHillPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 8: Print Dynamic Left Sided Pyramid * Pattern with n rows:

*     
**
*** 
**** 
***
**
*

n is user input integer.
"""

print("\nProgram8: Print Left Sided Pyramid Pattern. ")

def leftPyramidPattern(n):
    for row in range(n-1):
        for col in range(row+1):
            print("*",end="")
        print(" ")
    for row in range(n):
        for col in range(row,n):
            print("*",end="")
            
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
leftPyramidPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 9: Print Dynamic Right Sided Pyramid * Pattern with n rows:

       *     
      **
     *** 
    **** 
     ***
      **
       *

n is user input integer.
"""

print("\nProgram9: Print Right Sided Pyramid Pattern. ")

def rightPyramidPattern(n):
    for row in range(n-1):
        for space in range(row, n):
            print(" ",end="")
        for col in range(row+1):
            print("*",end="")
        print(" ")
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row, n):
            print("*",end="")
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
rightPyramidPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 10: Print Dynamic Diamond * Pattern with n rows:

     * 
    ***  
   *****
  ******* 
   *****
    *** 
     *  
	
n is user integer input
"""

print("Program10: Print Diamond Pattern.")

def diamondPattern(n):
    for row in range(n-1):
        for space in range(row,n):
            print(" ",end="")
        for col in range(row):
            print("*",end="")
        for col in range(row+1):
            print("*",end="")
        
        print(" ")
        
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row,n-1):
            print("*",end="")
        for col in range(row, n):
            print("*",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
diamondPattern(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 11: Print Variation of Diamond * Pattern with n rows:
    
     *
    * * *                 (make sure to give one space on right side of * to be printed in both the loops.)
   * * * * *
  * * * * * * *
   * * * * *
    * * *
     *

n is user integer input
"""

print("Program11: Print Variation of Diamond Pattern 1.")

def diamondPattern1(n):
    for row in range(n-1):
        for space in range(row,n):
            print(" ",end="")
        for col in range(row):
            print("* ",end="")
        for col in range(row+1):
            print("* ",end="")
        
        print(" ")
        
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row,n-1):
            print("* ",end="")
        for col in range(row, n):
            print("* ",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
diamondPattern1(n) # function call


print("\n----------------------------------------------------\n")
"""
Program 12: Print Variation of Diamond * Pattern with n rows:

      *
    *  *  *                          (make sure to give one space on either side of * to be printed in both the loops.)
   *  *  *  *  *
  *  *  *  *  *  *  *
   *  *  *  *  *
    *  *  *
     *
	
n is user integer input
"""

print("Program12: Print Variation of Diamond Pattern 2.")

def diamondPattern2(n):
    for row in range(n-1):
        for space in range(row,n):
            print(" ",end="")
        for col in range(row):
            print(" * ",end="")
        for col in range(row+1):
            print(" * ",end="")
        
        print(" ")
        
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row,n-1):
            print(" * ",end="")
        for col in range(row, n):
            print(" * ",end="")
        
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
diamondPattern2(n) # function call



print("\n----------------------------------------------------\n")
"""
Program 13: Print Dynamic Sandglass * Pattern with n rows:

* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

n is user input integer.
"""

print("\nProgram13: Print Sandglass Pattern. ")

def sandGlassPattern(n):
    for row in range(n):
        for space in range(row+1):
            print(" ",end="")
        for col in range(row, n-1):
            print("*",end="")
        for col in range(row,n):
            print("*",end="")
        print(" ")
    for row in range(n):
        for space in range(row, n):
            print(" ",end="")
        for col in range(row):
            print("*",end="")
        for col in range(row+1):
            print("*",end="")
        print(" ")

n = int(input("Enter number of rows you want to print:\n\n")) # take user input
sandGlassPattern(n) # function call


