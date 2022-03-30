"""
Print Pattern 1 as displayed below:

	# # # #
	# # # #
	# # # #
	# # # #
    
"""
print("Print Patterns Program 1: \n")
for i in range(4):
    for j in range(4):
        print("# ",end="")
    print()
 
 
    
"""
Print Pattern 2 as displayed below:

# 
# # 
# # # 
# # # #


"""
print()  # ignore this
print()  # ignore this

print("Print Patterns Program 2: \n")
for i in range(4):
    for j in range(i+1):
        print("# ",end="")
    print()
    
   
   
"""
Print Pattern 4 as displayed below:

          #
        # #
	  # # #
	# # # #

"""
print()  # ignore this
print()  # ignore this 

print("Print Patterns Program 3: \n")

for i in range(4):
    for j in range(4-i):
        print("# ",end="")
    print()



"""
Print Pattern 3 as displayed below:

# # # #
# # # 
# # 
# 

"""
print()  # ignore this
print()  # ignore this 

print("Print Patterns Program 3: \n")

for i in range(1,4+1):
    for j in range(4-i):
        print(" ",end="")
    while i>0:
        print("#",end="")
        i -=1
    print("")
