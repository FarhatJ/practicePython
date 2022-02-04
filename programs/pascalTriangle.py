
#Question:
#Write a program that outputs the first 6 lines of Pascal's Triangle. 

#//1 
#//1 1 
#//1 2 1 
#//1 3 3 1 
#//1 4 6 4 1 
#//1 5 10 10 5 1

#//Each row begins and ends with the number one. The remaining numbers are obtained by summing the two numbers that lie directly above that number on the previous row and the number that preceeds it. So, in order to find the numbers in the nth row of the triangle, we need the values of the (n-1) the row. Let's say that we have computed the fourth row - 1 3 3 1. Now, the fifth# row has five elements. The first and the last element would be one. The remaining elements would be (1+3), (3+3), (3+1) = 4, #6, 4. So, the complete fifth row would be 1 4 6 4 1.

#// A generic pascal's triangle function would accept a number of lines, and pass the following tests:
#// (in all cases below, we are just showing the last row, but a correct result would include all prior rows)
# 1 returns [1] (passed)
# 2 returns [1, 1] (which is result of [1, 1]) (passed)
# 3 returns [1, 2, 1] (which is result of [1, (1 + 1), 1] (passed)
# 4 returns [1, 3, 3, 1] (which is result of [1, (2+1), (1+2), 1]) (passed)
# 5 returns [1, 4, 6, 4, 1] (which is result of [1, (3 + 1), (3 + 3), (1 + 3), 1] (passed)
# 6 returns [1, 5, 10, 10, 5, 1] (which is result of [1, (4 + 1), (6 + 4), (4 + 6), (1 + 4), 1] (passed)
# 0 returns undefined (passed)

 #this function will just build the triangle, another function will print it out - keep out side effects




def pascalTriangle(lines):
    
    if lines == 0:
        print("undefined")

    for i in range(1, lines + 1):
        m = 1
        for j in range(1, i + 1):
            print(m, end = " ")
            m = int(m * (i - j)/ j)
        print("")



pascalTriangle(int(input("Enter number of rows you want to print: \n")))