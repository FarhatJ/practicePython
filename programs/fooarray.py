

def foo(list, n):
    
    for index in range(0, n):
        if (index + 1) % 2 == 1:  #for odd position
            list[index] += 1
        else:
            list[index] -= 1    # for even position
            
    return list        
            
list = [10, 10, 10, 10, 10]
n = len(list)
print(foo(list, n))