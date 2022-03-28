if __name__ == '__main__':
    N = int(input())
    output = []
    for i in range(N):
        a = input().split()
        print(a[0])
        if a[0] == "print":
            print(output)
        elif a[0] == "insert":
            output.insert(int(a[1]), int(a[2]))
        elif a[0] == "remove":
            output.remove(int(a[1]))
        elif a[0] == "pop":
            output.pop()
        elif a[0] == "append":
            output.append(int(a[1]))
        elif a[0] == "sort":
            output.sort()
        else:
            output.reverse()