def solution(n):
    # bin representation of N
    b = bin(n)[2:]
    # trim zeros from the right
    b = b.strip("0")
    l = b.split("1")    
    return len(max(l, key=len))
    
s = solution(15)
print(s)