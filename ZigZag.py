def zigzag(size):
    for i in range(size):
        for j in range(i+1):
            print(" ",end="")
        print(">")
    for i in range(size):
        for j in range(size -i -1):
            print("",end="")
        print("<")
size = int(input("enter the size of the sign:"))
zigzag(size)
        