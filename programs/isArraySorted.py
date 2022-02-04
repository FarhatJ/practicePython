#Question:
# Given an array of integers, write a function that will return a boolean that determines if the array is sorted, lowest to highest. 

# Function should return true or false in the following cases:
# [-1, 0, 1]: return true (successful test)
# [-1, 3, 10, 10]: return true (successful test)
# [1, 1, 1]: return true (successful test)
# [0, -1]: return false (successful test)
# [0]: return true (successful test)
# [-1, -3]: return false (successful test)
# []: return true (successful test)
# [-1, 0, 1, 10, 9]: return false (successful test)


def isArraySorted(array):
    if len(array)<= 1:
        return True
        
    for index in range(1, len(array)):
        if array[index - 1] > array[index]:
            return False
      
    return True

arr = [-1, 3, 10, 10]
print(isArraySorted(arr))
    


